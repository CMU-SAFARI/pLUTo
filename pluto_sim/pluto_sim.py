import math
import os

import numpy as np

from memory_models import DDR4, HMC
from pluto_core import Operations, pluto_configs, Workloads
from workload_data import WorkloadsData
from workload_instructions import InstructionQueues
from workload_luts import get_workload_luts

mem_configs = [DDR4(), HMC()]


class pLUTo:
    config = ""
    parallelism = 1
    tXAW = 13.328
    activation_limit = 4
    memory = None
    workload = ""
    InstructionQueue = None
    Data = None
    LUTS = None
    AP_queue = None
    AP_queue_fast = []

    def __init__(self, config, workload, memory, parallelism, tXAW=13.328):
        if config in pluto_configs:
            self.config = config
        else:
            raise ValueError("Invalid config!")

        self.workload = workload
        self.memory = memory
        self.parallelism = parallelism
        self.tXAW = tXAW

        self.Data = WorkloadsData[self.workload]
        self.InstructionQueue = InstructionQueues[self.workload]
        self.LUTS = get_workload_luts(workload, memory, parallelism)
        for i in self.InstructionQueue:
            if i.op == Operations.pLUTo:
                i.LUT = self.LUTS[i.LUT_ix]

    def generate_header(self):
        return [
            "".join(["// Workload: ", self.workload.name]),
            "".join(["// Memory: ", self.memory.name]),
            "".join(["// Parallelism: ", str(self.parallelism)]),
            "",
        ]

    def throttle_AP(self, queue, tXAW=-1, activation_limit=-1):
        if tXAW == -1:
            tXAW = self.tXAW

        if activation_limit == -1:
            activation_limit = self.activation_limit

        if tXAW == 0:
            activation_limit = float("inf")

        throttled_AP = []
        time = 0
        for batch in queue:
            ix = 0
            to_schedule = len(batch)
            while to_schedule > activation_limit:
                throttled_AP.append((time, batch[ix : ix + activation_limit]))
                to_schedule -= activation_limit
                time += tXAW
            if to_schedule > 0:
                throttled_AP.append((time, batch[ix:]))
                time += self.memory.FundamentalLatencies[Operations.ACT]

        return (time, throttled_AP)

    def throttle_AP_fast(self, queue, tXAW=-1, activation_limit=-1):
        if tXAW == -1:
            tXAW = self.tXAW
        if activation_limit == -1:
            activation_limit = self.activation_limit

        tACT = self.memory.FundamentalLatencies[Operations.ACT]
        parallelism = min(self.parallelism, self.memory.num_subarrays())

        if tXAW != 0 and parallelism > activation_limit:
            # Queue to succession of ns
            queue = [tACT * q for q in queue] + [tXAW * (q // activation_limit) for q in queue]
        else:
            # Queue to succession of ns
            queue = [tACT * q for q in queue]

        return sum(queue)

    def get_execution_time(self):
        # self.AP_queue = []
        self.AP_queue_fast = []
        time_cpu = 0
        # for ix, i in enumerate(self.InstructionQueue):
        for i in self.InstructionQueue:
            # print(ix, " of ", len(self.InstructionQueue))
            num_bytes = i.input_size_bytes
            num_rows = num_bytes / self.memory.row_size_bytes
            actual_parallelism = min(
                self.parallelism,
                math.ceil(i.input_size_bytes / self.memory.row_size_bytes),
            )

            if i.op == Operations.Reduction:
                time_cpu += num_bytes / self.memory.cpu_clock / 4
            else:
                # self.AP_queue.append(self.memory.getAPqueue(i, num_rows, actual_parallelism))
                self.AP_queue_fast.append(
                    self.memory.getAPqueue_fast(
                        self.config,
                        i,
                        num_rows,
                        actual_parallelism,
                    )
                )

        exec_time = self.throttle_AP_fast(self.AP_queue_fast)

        return (exec_time + time_cpu, time_cpu)

    def get_energy(self):
        s = 0
        for i in self.InstructionQueue:
            num_bytes = i.input_size_bytes
            num_rows = num_bytes / self.memory.row_size_bytes

            if i.op == Operations.pLUTo:
                if self.config == pluto_configs[0]:
                    energy_nJ = 2 * i.LUT.num_entries * self.memory.Energy[Operations.AP] * num_rows
                elif self.config == pluto_configs[1]:
                    energy_nJ = i.LUT.num_entries * self.memory.Energy[Operations.AP] * num_rows
                elif self.config == pluto_configs[2]:
                    energy_nJ = (
                        i.LUT.num_entries * self.memory.Energy[Operations.ACT] * num_rows
                        + self.memory.Energy[Operations.PRE] * num_rows
                    )
                else:
                    raise ValueError("Invalid config!")
            elif i.op == Operations.Reduction:
                reduction_time_s = num_bytes / self.memory.cpu_clock / 4
                energy_nJ = reduction_time_s * self.memory.cpu_tdp * 1e9
            else:
                energy_nJ = self.memory.Energy[i.op] * num_rows

            s += energy_nJ

        return s


def main():
    directory = "pysim"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for pluto_config in pluto_configs:
        print("Evaluating pLUTo-", pluto_config)

        filename = "".join(["pysim_", pluto_config, ".csv"])
        with open(os.path.join(directory, filename), "w") as f:
            f.write("workload, memory, parallelism, tXAW, energy (nJ), execution time (ns)\n")

            for m in mem_configs:
                print("Evaluating memory ", m, "...")
                for w in Workloads:
                    print("Running workload ", w.name, "...")
                    parallelism = m.parallelism
                    for p in parallelism:
                        print("Testing parallelism ", p, "...")
                        for tXAW in np.linspace(0, 13.328, num=3):
                            print("Testing tXAW ", tXAW, "...")

                            pluto = pLUTo(pluto_config, w, m, p, tXAW)
                            print("\n---\n")
                            print("- pLUTo " + pluto_config, end=", ")
                            print("Workload: " + w.name)
                            print("Parallelism: " + str(p))
                            print("tXAW: " + str(tXAW))

                            # Generate Program
                            # pluto.generate_c()

                            # Get Energy
                            print(
                                "Estimated energy consumption (nJ): ",
                                pluto.get_energy(),
                            )

                            # Get Execution Time
                            print(
                                "Estimated execution time (ns): ",
                                pluto.get_execution_time()[0],
                            )
                            f.write(
                                f"{w.name}, {m.name}, {p}, {tXAW}, {pluto.get_energy():.4f}, {pluto.get_execution_time()[0]:.4f}\n"
                            )


if __name__ == "__main__":
    main()

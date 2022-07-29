from pluto_core import Operations
from pluto_core import pluto_configs


class Memory:
    # HMC-specific
    n_vaults = -1
    clock_speed = -1

    # Generic Parameters
    name = ""
    total_memory_bytes = -1
    row_size_bytes = -1
    rows_per_subarray = -1
    n_banks = 16

    def num_subarrays(self):
        return int(
            self.total_memory_bytes / self.row_size_bytes / self.rows_per_subarray
        )

    def subarray_memory_bytes(self):
        return int(self.total_memory_bytes / self.num_subarrays())

    def adjacent_row_offset(self):
        return int(self.row_size_bytes * self.n_banks)

    def adjacent_subarray_offset(self):
        return int(self.rows_per_subarray * self.adjacent_row_offset())

    Energy = {
        Operations.ACT: -1,  # nJ
        Operations.READ: -1,  # nJ
        Operations.WRITE: -1,  # nJ
        Operations.PRE: -1,  # nJ
        Operations.AP: -1,  # nJ
        Operations.AAP: -1,  # nJ
        Operations.NOT: -1,  # nJ
        Operations.SHIFT: -1,  # nJ
        Operations.AND: -1,  # nJ
        Operations.OR: -1,  # nJ
        Operations.XOR: -1,  # nJ
    }

    FundamentalLatencies = {
        Operations.ACT: -1,  # ns
        Operations.READ: -1,  # ns
        Operations.WRITE: -1,  # ns
        Operations.PRE: -1,  # ns
    }

    def FundamentalLatenciesAsAP(self):
        return {
            Operations.ACT: [Operations.ACT],  # ns
            Operations.READ: [Operations.ACT],  # ns
            Operations.WRITE: [Operations.ACT],  # ns
            Operations.PRE: [Operations.PRE],  # ns
        }

    def AAPLatencies(self):
        return {
            Operations.AP: 1 * self.FundamentalLatencies[Operations.ACT]
            + 1 * self.FundamentalLatencies[Operations.PRE],  # ns
            Operations.AAP: 2 * self.FundamentalLatencies[Operations.ACT]
            + 1 * self.FundamentalLatencies[Operations.PRE],  # ns
        }

    def AAPLatenciesAsAP(self):
        return {
            Operations.AP: [Operations.ACT, Operations.PRE],  # ns
            Operations.AAP: [Operations.ACT, Operations.ACT, Operations.PRE],  # ns
        }

    def DerivedLatencies(self):
        return {
            Operations.NOT: 1 * self.AAPLatencies()[Operations.AAP],  # ns
            Operations.SHIFT: 1 * self.AAPLatencies()[Operations.AAP],  # ns
            Operations.AND: 4 * self.AAPLatencies()[Operations.AAP],  # ns
            Operations.OR: 4 * self.AAPLatencies()[Operations.AAP],  # ns
            Operations.XOR: 5 * self.AAPLatencies()[Operations.AAP]
            + 2 * self.AAPLatencies()[Operations.AP],  # ns
            Operations.XNOR: 6 * self.AAPLatencies()[Operations.AAP]
            + 2 * self.AAPLatencies()[Operations.AP],  # ns
        }

    def DerivedLatenciesAsAP(self):
        return {
            Operations.NOT: 1 * self.AAPLatenciesAsAP()[Operations.AAP],
            Operations.SHIFT: 1 * self.AAPLatenciesAsAP()[Operations.AAP],
            Operations.AND: 4 * self.AAPLatenciesAsAP()[Operations.AAP],
            Operations.OR: 4 * self.AAPLatenciesAsAP()[Operations.AAP],
            Operations.XOR: 5 * self.AAPLatenciesAsAP()[Operations.AAP]
            + 2 * self.AAPLatenciesAsAP()[Operations.AP],
            Operations.XNOR: 6 * self.AAPLatenciesAsAP()[Operations.AAP]
            + 2 * self.AAPLatenciesAsAP()[Operations.AP],
        }

    def getAPqueue(self, inst, num_rows, parallelism):
        if inst.op == Operations.pLUTo:
            return self.AAPLatenciesAsAP()[Operations.AP] * int(
                inst.LUT.num_entries * num_rows / parallelism
            )
        elif inst.op in [
            Operations.ACT,
            Operations.READ,
            Operations.WRITE,
            Operations.PRE,
        ]:
            return self.FundamentalLatenciesAsAP()[inst.op] * int(
                num_rows / parallelism
            )
        elif inst.op in [Operations.AP, Operations.AAP]:
            return self.AAPLatenciesAsAP()[inst.op] * int(num_rows / parallelism)
        elif inst.op in [
            Operations.NOT,
            Operations.SHIFT,
            Operations.AND,
            Operations.OR,
            Operations.XOR,
            Operations.XNOR,
        ]:
            return self.DerivedLatenciesAsAP()[inst.op] * int(num_rows / parallelism)
        else:
            raise ValueError("Invalid op!")

    def getAPqueue_fast(self, pluto_config, inst, num_rows, parallelism):
        num_entries = 0
        ops_pluto = 0
        if inst.op == Operations.pLUTo:
            num_entries = inst.LUT.num_entries
            if pluto_config == pluto_configs[0]:
                ops_pluto = 2 * 2 * num_entries
            elif pluto_config == pluto_configs[1]:
                ops_pluto = 2 * num_entries
            elif pluto_config == pluto_configs[2]:
                ops_pluto = num_entries + 1
            else:
                raise ValueError("Invalid config!")

        num_AP = {
            Operations.pLUTo: ops_pluto,
            Operations.ACT: 1,
            Operations.READ: 1,
            Operations.WRITE: 1,
            Operations.PRE: 1,
            Operations.AP: 2,
            Operations.AAP: 3,
            Operations.NOT: 3,
            Operations.SHIFT: 3,
            Operations.AND: 12,
            Operations.OR: 12,
            Operations.XOR: 19,
            Operations.XNOR: 22,
        }

        return int(num_AP[inst.op] * num_rows / parallelism)


class DDR4(Memory):
    # Generic Parameters
    name = "DDR4"
    total_memory_bytes = (2**3) * (2**30)
    row_size_bytes = 8192
    rows_per_subarray = 512

    cpu_tdp = 105 / 12
    cpu_clock = 2.3e9

    Energy = {
        Operations.ACT: 2.07e-1,  # nJ
        Operations.READ: 7.26,  # nJ
        Operations.WRITE: 7.54,  # nJ
        Operations.PRE: 4.58e-1,  # nJ
        Operations.AP: 6.64e-1,  # nJ
        Operations.AAP: 8.71e-1,  # nJ
        Operations.NOT: 1.74,  # nJ
        Operations.SHIFT: 1.74,  # nJ
        Operations.AND: 3.48,  # nJ
        Operations.OR: 3.48,  # nJ
        Operations.XOR: 5.68,  # nJ
    }

    FundamentalLatencies = {
        Operations.ACT: 14.16,  # ns
        Operations.READ: 14.16,  # ns
        Operations.WRITE: 14.16,  # ns
        Operations.PRE: 14.16,  # ns
    }


class HMC(Memory):
    # HMC-specific
    n_vaults = 32
    clock_speed = 1.25e9

    # Generic Parameters
    name = "3DS"
    total_memory_bytes = (2**3) * (2**30)
    row_size_bytes = 8192 / n_vaults  # per vault
    rows_per_subarray = 512

    cpu_tdp = 10
    cpu_clock = 1.25e9

    Energy = {
        Operations.ACT: 2.07e-1,  # nJ
        Operations.READ: 7.26,  # nJ
        Operations.WRITE: 7.54,  # nJ
        Operations.PRE: 4.58e-1,  # nJ
        Operations.AP: 6.64e-1,  # nJ
        Operations.AAP: 8.71e-1,  # nJ
        Operations.NOT: 1.74,  # nJ
        Operations.SHIFT: 1.74,  # nJ
        Operations.AND: 3.48,  # nJ
        Operations.OR: 3.48,  # nJ
        Operations.XOR: 5.68,  # nJ
    }

    FundamentalLatencies = {
        Operations.ACT: 10.2,  # ns
        Operations.READ: 7.7,  # ns
        Operations.WRITE: 7.7,  # ns
        Operations.PRE: 9.9,  # ns
    }

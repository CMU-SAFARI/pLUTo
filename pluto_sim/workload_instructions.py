import math

from pluto_core import Instruction, Operations
from workload_data import WorkloadsData
from workload_luts import Workloads


def get_size_inputs(workload):
    data = WorkloadsData[workload]
    return max([d.size_bytes for d in data])


VecAdd4_KSA_InstQueue = [
    Instruction(Operations.XOR, get_size_inputs(Workloads.VecAdd8)),
    Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
]
VecAdd4_KSA_InstQueue.extend(
    [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
    ]
    * int(math.log2(4))
)
VecAdd4_KSA_InstQueue.extend(
    [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.XOR, get_size_inputs(Workloads.VecAdd8)),
    ]
)

VecAdd4_LUT_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecAdd8), LUT_ix=0)
]

VecAdd8_InstQueue = [
    Instruction(Operations.XOR, get_size_inputs(Workloads.VecAdd8)),
    Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
]
VecAdd8_InstQueue.extend(
    [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecAdd8)),
    ]
    * int(math.log2(8))
)
VecAdd8_InstQueue.extend(
    [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecAdd8)),
        Instruction(Operations.XOR, get_size_inputs(Workloads.VecAdd8)),
    ]
)

VecMulQ8_InstQueue = (
    [
        # Q1x7
        # Copy x4
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ8)),
        # And x4
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        # Or x2
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8)),
        # Shift x2
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ8)),
        # Or x2
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8)),
        # pLUTo 256 x4
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ8), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ8), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ8), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ8), LUT_ix=0),
        # Or
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8))
        # 16-bit Add x2
    ]
    + 2
    * (
        [
            Instruction(Operations.XOR, get_size_inputs(Workloads.VecMulQ8)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        ]
        + [
            Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ8)),
            Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ8)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
            Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ8)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ8)),
        ]
        * int(math.log2(16))
    )
    + [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ8)),
        Instruction(Operations.XOR, get_size_inputs(Workloads.VecMulQ8)),
    ]
)

VecMulQ16_InstQueue = (
    4
    * [
        # Q1x15
        # Copy x4
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AAP, get_size_inputs(Workloads.VecMulQ16)),
        # And x4
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        # Or x2
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16)),
        # Shift x2
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ16)),
        # Or x2
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16)),
        # pLUTo 256 x4
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ16), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ16), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ16), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VecMulQ16), LUT_ix=0),
        # Or
        Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16))
        # 32-bit Add x2
    ]
    + 2
    * (
        [
            Instruction(Operations.XOR, get_size_inputs(Workloads.VecMulQ16)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        ]
        + [
            Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ16)),
            Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ16)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
            Instruction(Operations.OR, get_size_inputs(Workloads.VecMulQ16)),
            Instruction(Operations.AND, get_size_inputs(Workloads.VecMulQ16)),
        ]
        * int(math.log2(32))
    )
    + [
        Instruction(Operations.SHIFT, get_size_inputs(Workloads.VecMulQ16)),
        Instruction(Operations.XOR, get_size_inputs(Workloads.VecMulQ16)),
    ]
)

CRC8_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.CRC8), LUT_ix=0),
    Instruction(Operations.Reduction, get_size_inputs(Workloads.CRC8)),
]

CRC16_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.CRC16), LUT_ix=0),
    Instruction(Operations.Reduction, get_size_inputs(Workloads.CRC16)),
]

CRC32_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.CRC32), LUT_ix=0),
    Instruction(Operations.Reduction, get_size_inputs(Workloads.CRC32)),
]

Salsa20_InstQueue = [
    Instruction(Operations.Reduction, get_size_inputs(Workloads.Salsa20)),
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.Salsa20), LUT_ix=0),
    Instruction(Operations.XOR, get_size_inputs(Workloads.Salsa20), LUT_ix=0),
]

VMPC_InstQueue = (
    [
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VMPC), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VMPC), LUT_ix=0),
        Instruction(Operations.pLUTo, get_size_inputs(Workloads.VMPC), LUT_ix=0),
    ]
    + VecAdd8_InstQueue
    + [Instruction(Operations.pLUTo, get_size_inputs(Workloads.VMPC), LUT_ix=0)]
)

BitWiseOps_InstQueue = [
    # Compute
    Instruction(Operations.OR, get_size_inputs(Workloads.BitWiseOps)),
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.BitWiseOps), LUT_ix=0),
]

BitCount_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.BitCount), LUT_ix=0)
]

BitCount_short_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.BitCount_short), LUT_ix=0)
]

ImgBin_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.BitWiseOps), LUT_ix=0)
]

ColorGrade_InstQueue = [
    Instruction(Operations.pLUTo, get_size_inputs(Workloads.BitWiseOps), LUT_ix=0)
]

LeNet4_InstQueue = [
    # Conv + Tanh
    # Feature Map * SizeX * SizeY * KernelX * KernelY / Stride / (8 / bitwidth)
    Instruction(Operations.pLUTo, 6 * 28 * 28 * 5 * 5 / 1 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 6 * 28 * 28 * 5 * 5 / 1 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 6 * 28 * 28 * 5 * 5 / 1 / 2),
    # AvgPool + Tanh
    Instruction(Operations.pLUTo, 6 * 14 * 14 * 2 * 2 / 2 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 6 * 14 * 14 * 2 * 2 / 2 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 6 * 14 * 14 * 2 * 2 / 2 / 2),
    # Conv + Tanh
    Instruction(Operations.pLUTo, 16 * 10 * 10 * 5 * 5 / 1 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 16 * 10 * 10 * 5 * 5 / 1 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 16 * 10 * 10 * 5 * 5 / 1 / 2),
    # AvgPool + Tanh
    Instruction(Operations.pLUTo, 16 * 5 * 5 * 2 * 2 / 2 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 16 * 5 * 5 * 2 * 2 / 2 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 16 * 5 * 5 * 2 * 2 / 2 / 2),
    # Conv + Tanh
    Instruction(Operations.pLUTo, 120 * 1 * 1 * 5 * 5 / 1 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 120 * 1 * 1 * 5 * 5 / 1 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 120 * 1 * 1 * 5 * 5 / 1 / 2),
    # FC + Tanh
    Instruction(Operations.pLUTo, 84 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 84 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 84 / 2),
    # FC + SoftMax
    Instruction(Operations.pLUTo, 10 / 2, LUT_ix=0),
    Instruction(Operations.pLUTo, 10 / 2, LUT_ix=1),
    Instruction(Operations.Reduction, 10 / 2),
]

LeNet1_InstQueue = [
    # Conv + Tanh
    # Feature Map * SizeX * SizeY * KernelX * KernelY / Stride / (8 / bitwidth)
    Instruction(Operations.pLUTo, 6 * 28 * 28 * 5 * 5 / 1 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 6 * 28 * 28 * 5 * 5 / 1 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 6 * 28 * 28 * 5 * 5 / 1 / 8),
    # AvgPool + Tanh
    Instruction(Operations.pLUTo, 6 * 14 * 14 * 2 * 2 / 2 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 6 * 14 * 14 * 2 * 2 / 2 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 6 * 14 * 14 * 2 * 2 / 2 / 8),
    # Conv + Tanh
    Instruction(Operations.pLUTo, 16 * 10 * 10 * 5 * 5 / 1 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 16 * 10 * 10 * 5 * 5 / 1 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 16 * 10 * 10 * 5 * 5 / 1 / 8),
    # AvgPool + Tanh
    Instruction(Operations.pLUTo, 16 * 5 * 5 * 2 * 2 / 2 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 16 * 5 * 5 * 2 * 2 / 2 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 16 * 5 * 5 * 2 * 2 / 2 / 8),
    # Conv + Tanh
    Instruction(Operations.pLUTo, 120 * 1 * 1 * 5 * 5 / 1 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 120 * 1 * 1 * 5 * 5 / 1 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 120 * 1 * 1 * 5 * 5 / 1 / 8),
    # FC + Tanh
    Instruction(Operations.pLUTo, 84 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 84 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 84 / 8),
    # FC + SoftMax
    Instruction(Operations.pLUTo, 10 / 8, LUT_ix=0),
    Instruction(Operations.pLUTo, 10 / 8, LUT_ix=1),
    Instruction(Operations.Reduction, 10 / 8),
]

InstructionQueues = {
    Workloads.VecAdd4_KSA: VecAdd4_KSA_InstQueue,
    Workloads.VecAdd8: VecAdd8_InstQueue,
    Workloads.VecMulQ8: VecMulQ8_InstQueue,
    Workloads.VecMulQ16: VecMulQ16_InstQueue,
    Workloads.CRC8: CRC8_InstQueue,
    Workloads.CRC16: CRC16_InstQueue,
    Workloads.CRC32: CRC32_InstQueue,
    Workloads.Salsa20: Salsa20_InstQueue,
    Workloads.VMPC: VMPC_InstQueue,
    Workloads.BitWiseOps: BitWiseOps_InstQueue,
    Workloads.BitCount: BitCount_InstQueue,
    Workloads.BitCount_short: BitCount_short_InstQueue,
    Workloads.ImgBin: ImgBin_InstQueue,
    Workloads.ColorGrade: ColorGrade_InstQueue,
    Workloads.LeNet4: LeNet4_InstQueue,
    Workloads.LeNet1: LeNet1_InstQueue,
}

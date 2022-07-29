from pluto_core import Data, Workloads

VecAdd4_KSA_Data = [
    # A + B = C
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

VecAdd4_LUT_Data = [
    # A + B = C
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

VecAdd8_Data = [
    # A + B = C
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

VecMul8_Data = [
    # 8-bit
    # A .* B = C
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

VecMul16_Data = [
    # 16-bit
    # A .* B = C
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

MatVecMul_Data = [
    # A * b = c
    Data("A", size_bytes=640 * 640, Input=True),
    Data("B", size_bytes=640 * 1, Input=True),
    Data("C", size_bytes=640 * 1, Output=True),
]

DotProd_Data = [
    # a .* b = c
    Data("A", size_bytes=20480, Input=True),
    Data("B", size_bytes=20480, Input=True),
    Data("C", size_bytes=20480, Output=True),
]

MatMul_Data = [
    # A * B = C
    Data("A", size_bytes=640 * 480, Input=True),
    Data("B", size_bytes=480 * 320, Input=True),
    Data("C", size_bytes=640 * 320, Output=True),
]

CRC8_Data = [
    # C = CRC8(A)
    Data("A", size_bytes=128 * 1048576, Input=True),
    Data("C", size_bytes=128 * 1048576, Output=True),
]

CRC16_Data = [
    # C = CRC16(A)
    Data("A", size_bytes=128 * 1048576, Input=True),
    Data("C", size_bytes=128 * 1048576, Output=True),
]

CRC32_Data = [
    # C = CRC32(A)
    Data("A", size_bytes=128 * 1048576, Input=True),
    Data("C", size_bytes=128 * 1048576, Output=True),
]

RC4_Data = [
    # C = RC4(A)
    Data("A", size_bytes=1024 * 1048576, Input=True),
    Data("C", size_bytes=1024 * 1048576, Output=True),
]

Salsa20_Data = [
    # C = Salsa20(A)
    Data("A", size_bytes=512 * 1048576, Input=True),
    Data("C", size_bytes=512 * 1048576, Output=True),
]

VMPC_Data = [
    # C = VMPC(A)
    Data("A", size_bytes=512 * 1048576, Input=True),
    Data("C", size_bytes=512 * 1048576, Output=True),
]

BitWiseOps_Data = [
    # C = A & B
    # Whenever different, also:
    # C = A & B
    # C = A | B
    # C = A ^ B
    # C = !B
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

BitCount_Data = [
    # C = BitCount8(A)
    Data("A", size_bytes=2**13 * 16, Input=True),
    Data("B", size_bytes=2**13 * 16, Input=True),
    Data("C", size_bytes=2**13 * 16, Output=True),
]

ImgBin_Data = [
    # C = BinImg(A)
    Data("A", size_bytes=2**13 * 115, Input=True),
    Data("C", size_bytes=2**13 * 115, Output=True),
]

ColorGrade_Data = [
    # C = ColorGrade(A)
    Data("A", size_bytes=2**13 * 115, Input=True),
    Data("C", size_bytes=2**13 * 115, Output=True),
]

LeNet_Data = [
    Data("A", size_bytes=2**13 * 115, Input=True),
    Data("C", size_bytes=2**13 * 115, Output=True),
]

WorkloadsData = {
    Workloads.VecAdd4_KSA: VecAdd4_KSA_Data,
    Workloads.VecAdd8: VecAdd8_Data,
    Workloads.VecMulQ8: VecMul8_Data,
    Workloads.VecMulQ16: VecMul16_Data,
    Workloads.CRC8: CRC8_Data,
    Workloads.CRC16: CRC16_Data,
    Workloads.CRC32: CRC32_Data,
    Workloads.Salsa20: Salsa20_Data,
    Workloads.VMPC: VMPC_Data,
    Workloads.BitWiseOps: BitWiseOps_Data,
    Workloads.BitCount: BitCount_Data,
    Workloads.BitCount_short: BitCount_Data,
    Workloads.ImgBin: ImgBin_Data,
    Workloads.ColorGrade: ColorGrade_Data,
    Workloads.LeNet1: LeNet_Data,
    Workloads.LeNet4: LeNet_Data,
}

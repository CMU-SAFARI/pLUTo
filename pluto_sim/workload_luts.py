from pluto_core import LUT, Workloads


# Add 4
def VecAdd4_KSA_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [] * p


def VecAdd8_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [] * p


def VecMul8_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def VecMul16_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def CRC8_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def CRC16_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def CRC32_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def Salsa20_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def VMPC_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def BitWiseOps_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def BitCount_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def BitCount_short_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(16)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def ImgBin_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def ColorGrade_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


def LeNet_LUTs(m, p):
    assert p <= m.num_subarrays()
    return [
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
        LUT(m, [range(256)], lambda x: ("%0.2X" % ((x // 16) + (x % 16)))[:2], 1),
    ] * p


WorkloadLUTs = {
    Workloads.VecAdd4_KSA: VecAdd4_KSA_LUTs,
    Workloads.VecAdd8: VecAdd8_LUTs,
    Workloads.VecMulQ8: VecMul8_LUTs,
    Workloads.VecMulQ16: VecMul16_LUTs,
    Workloads.CRC8: CRC8_LUTs,
    Workloads.CRC16: CRC16_LUTs,
    Workloads.CRC32: CRC32_LUTs,
    Workloads.Salsa20: Salsa20_LUTs,
    Workloads.VMPC: VMPC_LUTs,
    Workloads.BitWiseOps: BitWiseOps_LUTs,
    Workloads.BitCount_short: BitCount_short_LUTs,
    Workloads.BitCount: BitCount_LUTs,
    Workloads.ImgBin: ImgBin_LUTs,
    Workloads.ColorGrade: ColorGrade_LUTs,
    Workloads.LeNet1: LeNet_LUTs,
    Workloads.LeNet4: LeNet_LUTs,
}


def get_workload_luts(w, m, p):
    return WorkloadLUTs[w](m, p)

from enum import auto, Enum

import numpy as np

pluto_configs = ["GSA", "BSA", "GMC"]


class Workloads(Enum):
    VecAdd4_KSA = auto()
    VecAdd8 = auto()
    VecMulQ8 = auto()
    VecMulQ16 = auto()
    CRC8 = auto()
    CRC16 = auto()
    CRC32 = auto()
    Salsa20 = auto()
    VMPC = auto()
    BitWiseOps = auto()
    BitCount = auto()
    BitCount_short = auto()
    ImgBin = auto()
    ColorGrade = auto()
    LeNet4 = auto()
    LeNet1 = auto()


class Operations(Enum):
    ACT = auto()
    READ = auto()
    WRITE = auto()
    PRE = auto()
    AP = auto()
    AAP = auto()
    NOT = auto()
    SHIFT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    XNOR = auto()
    pLUTo = auto()
    Reduction = auto()


class Data:
    name = ""
    size_bytes = -1
    Input = False
    Output = False

    def __init__(self, name, size_bytes, Input=False, Output=False):
        self.name = name
        self.size_bytes = size_bytes
        self.Input = Input
        self.Output = Output


class Instruction:
    op = None
    input_size_bytes = -1
    rowA = None
    rowB = None
    rowC = None
    LUT = None
    LUT_ix = -1

    def __init__(self, op, size, rowA=None, rowB=None, rowC=None, LUT=None, LUT_ix=-1):
        if op == Operations.pLUTo:
            assert LUT != None or LUT_ix != -1

        self.op = op
        self.input_size_bytes = size
        self.rowA = rowA
        self.rowB = rowB
        self.rowC = rowC
        self.LUT = LUT
        self.LUT_ix = LUT_ix


def func():
    pass


class LUT:
    # Memory parameters
    memory = None

    # LUT metadata
    inputs = []
    num_entries = -1
    function = func
    data_width = -1
    repmat_factor = (1, 8192)
    data_hex = []

    def __init__(self, memory, inputs, function, data_width):
        self.memory = memory
        self.inputs = inputs
        self.function = function
        self.data_width = data_width

        self.repmat_factor = (
            int(self.memory.row_size_bytes / self.data_width / len(self.inputs)),
            1,
        )
        self.generate_data()

    def generate_data(self):
        self.data_hex = []
        for in_vec in self.inputs:
            if len(in_vec) > self.num_entries:
                self.num_entries = len(in_vec)

            self.data_hex.append([])
            for i in in_vec:
                self.data_hex[-1].append(self.function(i))

        self.data_hex = np.tile(self.data_hex, self.repmat_factor).T

        # print(self.data_hex)
        # print(self.data_hex.shape)

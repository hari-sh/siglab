import numpy as np
import modulate.modutil as modutil

M = 4
symdict = {
    (0, 0, 0, 0): -3 - 3j,
    (0, 0, 0, 1): -3 - 1j,
    (0, 0, 1, 0): -3 + 3j,
    (0, 0, 1, 1): -3 + 1j,
    (0, 1, 0, 0): -1 - 3j,
    (0, 1, 0, 1): -1 - 1j,
    (0, 1, 1, 0): -1 + 3j,
    (0, 1, 1, 1): -1 + 1j,
    (1, 0, 0, 0):  3 - 3j,
    (1, 0, 0, 1):  3 - 1j,
    (1, 0, 1, 0):  3 + 3j,
    (1, 0, 1, 1):  3 + 1j,
    (1, 1, 0, 0):  1 - 3j,
    (1, 1, 0, 1):  1 - 1j,
    (1, 1, 1, 0):  1 + 3j,
    (1, 1, 1, 1):  1 + 1j
}

def mod(bits):
    assert len(bits) % M == 0, "Bits length must be a multiple of 4 for 16-QAM"
    return modutil.mod(bits, symdict, M)

def demod(symbols):
    return modutil.demod(symbols, dict((v,k) for k,v in symdict.items()))

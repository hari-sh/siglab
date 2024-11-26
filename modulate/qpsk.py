import numpy as np
import modulate.modutil as modutil

M = 2
symdict = {
    (0, 0): -1 - 1j,
    (0, 1): -1 + 1j,
    (1, 0): 1 - 1j,
    (1, 1): 1 + 1j
}

def mod(bits):
    assert len(bits) % M == 0, "Bits length must be a multiple of M"
    return modutil.mod(bits, symdict, M)

def demod(symbols):
    return modutil.demod(symbols, dict((v,k) for k,v in symdict.items()))

# def mod(bits):
#     bit_pairs = bits.reshape(-1, 2)
#     symbols = 1 / np.sqrt(2) * ((2 * bit_pairs[:, 0] - 1) + 1j * (2 * bit_pairs[:, 1] - 1))
#     return symbols

# def demod(symbols):
#     bits = np.zeros((len(symbols), 2))
#     bits[:, 0] = np.real(symbols) > 0
#     bits[:, 1] = np.imag(symbols) > 0
#     return bits.flatten().astype(int)
import numpy as np

qam16_mod = {
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

def modulate(bits):
    assert len(bits) % 4 == 0, "Bits length must be a multiple of 4 for 16-QAM"
    symbols = []
    for i in range(0, len(bits), 4):
        symbol_bits = tuple(bits[i:i+4])
        symbols.append(qam16_mod[symbol_bits])
    return np.array(symbols)

def demodulate(symbols):
    qam16_demod = dict((v,k) for k,v in qam16_mod.items())
    keys = np.array(list(qam16_demod.keys()))
    bits = []
    for symbol in symbols:
        closest_constellation_point = min(keys, key=lambda x: np.abs(symbol - x))
        bits.extend(qam16_demod[closest_constellation_point])
    return np.array(bits)

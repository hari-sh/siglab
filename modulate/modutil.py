import numpy as np
def mod(bits, symdict, M):
    symbols = []
    for i in range(0, len(bits), M):
        symbol_bits = tuple(bits[i:i+M])
        symbols.append(symdict[symbol_bits])
    return np.array(symbols)

def demod(symbols, symdict):
    keys = np.array(list(symdict.keys()))
    bits = []
    for symbol in symbols:
        closest_constellation_point = min(keys, key=lambda x: np.abs(symbol - x))
        bits.extend(symdict[closest_constellation_point])
    return np.array(bits)
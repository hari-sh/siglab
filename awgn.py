import numpy as np
from numpy.random import randn

def add(signal, snr_db):
    snr_linear = 10**(snr_db / 10)
    signal_power = np.mean(np.abs(signal)**2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power / 2) * (randn(len(signal)) + 1j * randn(len(signal)))
    return signal + noise
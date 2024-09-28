import numpy as np
def add_awgn_noise(symbols, snr_dB):
    snr_linear = 10**(snr_dB / 10)
    signal_power = np.mean(np.abs(symbols)**2)
    noise_power = signal_power / snr_linear
    
    noise = np.sqrt(noise_power / 2) * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))
    
    noisy_symbols = symbols + noise
    return noisy_symbols
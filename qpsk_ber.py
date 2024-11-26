import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
import modulate.qpsk as passmod
# import modulate.qam16 as passmod
import awgn

def simulate_ber_qpsk(snr_db_range, num_bits):
    ber = []
    for snr_db in snr_db_range:
        # bits = np.random.randint(0, 2, num_bits)
        bits = np.random.binomial(n=1, p=0.5, size=num_bits)
        tx_symbols = passmod.mod(bits)
        rx_symbols = awgn.add(tx_symbols, snr_db)
        rx_bits = passmod.demod(rx_symbols)
        ber.append(np.sum(bits != rx_bits)/num_bits)
    return ber

def theoretical_ber_qpsk(snr_db_range):
    snr_linear = 10**(np.array(snr_db_range) / 10)
    return 0.5 * erfc(np.sqrt(snr_linear))

snr_db_range = np.arange(-2, 17, 0.5)

num_bits = 200000

simulated_ber = simulate_ber_qpsk(snr_db_range, num_bits)
theoretical_ber = theoretical_ber_qpsk(snr_db_range)

plt.figure(figsize=(10, 6))
plt.semilogy(snr_db_range, simulated_ber, 'o-', label="Simulated BER")
# plt.semilogy(snr_db_range, theoretical_ber, 's-', label="Theoretical BER", linestyle='dashed')
plt.title("BER vs. SNR")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid(True, which="both", linestyle='--', linewidth=0.7)
plt.legend()
plt.show()

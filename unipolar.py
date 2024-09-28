import numpy as np
import matplotlib.pyplot as plt

def plot_binary(bits1, bits2):
    bit_duration = 1

    time1 = np.arange(0, len(bits1) * bit_duration, 0.01)
    time2 = np.arange(0, len(bits2) * bit_duration, 0.01)

    signal1 = np.repeat(bits1, int(1/0.01))
    signal2 = np.repeat(bits2, int(1/0.01))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    ax1.step(time1, signal1, where='post', color='blue', linewidth=2)
    ax1.set_ylim(-0.5, 1.5)
    ax1.set_title('Transmitted Bits')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.set_xticks(np.arange(0, len(bits1)+1, step=1))
    ax1.set_yticks([0, 1], labels=['0', '1'])

    ax2.step(time2, signal2, where='post', color='green', linewidth=2)
    ax2.set_ylim(-0.5, 1.5)
    ax2.set_title('Received Bits')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Amplitude')
    ax2.set_xticks(np.arange(0, len(bits2)+1, step=1))
    ax2.set_yticks([0, 1], labels=['0', '1'])

    plt.tight_layout()
    plt.show()

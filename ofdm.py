import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft
import qam16 as qam
from unipolar import plot_binary
plt.rcParams['figure.figsize'] = [10, 5]


bits_per_symbol = 4

def add_cyclic_prefix(inp, l):
    return np.concatenate((inp[-l+1:], inp), axis=0)

def remove_cyclic_prefix(inp, l):
    return inp[l-1:]

bits =  np.random.binomial(n=1, p=0.5, size=16)
X = qam.modulate(bits)
h = np.random.rayleigh(size=int(len(bits)/bits_per_symbol))
plt.plot(h)
x = ifft(X)
xpad = add_cyclic_prefix(x, len(h))
r = np.convolve(xpad, h)[:-len(h)+1]
y = remove_cyclic_prefix(r, len(h))

Y = fft(y)
H = fft(h)

xhat = np.divide(Y, H)
rec_bits = qam.demodulate(xhat)
plot_binary(bits, rec_bits)
print(X)
print(xhat)



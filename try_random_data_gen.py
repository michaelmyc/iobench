import numpy as np

# (1024 - 132) / 8

# k * 8 + 128 bytes

x = np.random.bytes(1024 - 128)
np.save("test.npy", x)

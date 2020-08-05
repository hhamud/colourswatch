import numpy as np


numpy_array = np.zeros([6, 1, 3], dtype=np.uint8)
numpy_array[:,100:] = [255, 128, 0]
numpy_array[:, :100] = [0, 0, 255]
print(numpy_array)
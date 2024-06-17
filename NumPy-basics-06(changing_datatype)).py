import numpy as np

array2=np.arange(12,dtype=np.float64).reshape(3,4)

print(array2.dtype)

array2.dtype=np.int32

print(array2.dtype)
import numpy as np

array1=np.arange(10)
array2=np.arange(12,dtype=float).reshape(3,4)
array3=np.arange(8).reshape(2,2,2)

### ndim- number of dimensions

print(array1.ndim)
print(array2.ndim)
print(array3.ndim)

print(array1.shape)
print(array2.shape)
print(array3.shape)

### some other attributes are itemsize (memory occupied by each element in array), dtype(data type)
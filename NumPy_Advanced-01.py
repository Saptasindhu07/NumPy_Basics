import numpy as np

array1=np.random.randint(1,100,24).reshape(6,4)

print(array1)

### Sorting Ascending

print(np.sort(array1,axis=0)) ##col-wise sort

### Appending 

print(np.arange(4).reshape(1,4))
print(np.append(array1,np.arange(4).reshape(1,4),axis=0)) ### Appending a new row

### Taking out unique items
array2=np.array([1,1,1,1,1,1,12,2,2,2,2,2,2,23,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5,55,555,55,67,67,76,67])
print(np.unique(array2))

### Searrching for indices in an array where the given condition is satisfied 
### Syntax- np.where(condition, true_case_action, flase_case_action)

print(np.where(array2>3,0,array2)) ### replace by 0 is true else let it be

### np.argmax(), np.argmin() returns the max or min elements from the array or row/columnwise


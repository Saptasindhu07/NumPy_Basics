import numpy as np

array1=np.arange(10).reshape(1,10)
array2=np.arange(12,dtype=float).reshape(3,4)
array3=np.arange(8).reshape(2,2,2)
array4=array1.reshape(10,1)
##arithmetic operators

print(array1)
print(array1+2)

### relational operators 

print(array1)
print(array1>5)
print(array1==7)


###Vector operations(matrix operations)

print(array1+array1)

## other operations (max,min,sum)

print(array2)
print("KAKKKAKAKAA")
print(np.max(array2,axis=0))    ###if axis=0, column by column checked. else if axis=1,row by row checked and max/min
                                ###from each row or column returned as array
print(np.max(array2,axis=1))

###statistical operations (mean,median,mode,std dev etc.)

print(np.mean(array1))          ##Axis can be mentioned if row-wise or col-wise mean is needed

###dot product(matrix multiply)

print(np.dot(array1,array4))

###indexing and slicing (format array_name[row(?:?:?),col(?:?:?)])

print(array2[::2,::3])

###transpose, ravel(change any dimension array to 1-D array)

print(array2.T)
print(array2.ravel())

### hstack((array_1,array_2)), vstack((array_1,array_2)) for stacking horizontally and vertically 
### hsplit(array_name,how many parts to split in),vsplit(array_name,how many parts to split in)

### Advanced indexing 

print(array2)

print(array2[[1,2],1::2])

###Boolean Indexing (give a logic to select a number based on criteria from matrix)

array_bool=np.random.randint(1,100,24).reshape(6,4)

print(array_bool[array_bool>50])
print(array_bool[array_bool%2==0])

###Broadcasting (describes how NumPy treats arrays with different shapes during arithmetic operations)
### Broadcasting happens automatically NumPy for rules, check the copy notes

a=np.arange(12).reshape(4,3)
b=np.arange(3)
print(a+b)


###Sigmoid Function

def sigmoid(array):
    return 1/(1+np.exp(-(array)))

print(sigmoid(array1))
print(sigmoid(array4)) 
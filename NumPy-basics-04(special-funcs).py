import numpy as np

###Shape always in the form of rows,cols

print(np.ones((3,4),dtype=float))
print(np.zeros((10,20),dtype=complex))

###random initialises random integer between 0 and 1

print(500*np.random.random((5,5)))

### linspace takes a range of start and end and generates numbers linearly distributed

print(np.linspace(-10,10,15,dtype=float))

###Create an identity matrix

print(np.identity(4,dtype=int))
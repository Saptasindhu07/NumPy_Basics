import matplotlib.pyplot as plt
import numpy as np 


X=np.random.randint(0,100,50)
Y1=X

X2=np.arange(-50,50,0.001)
Y2=np.power(X2,2)
Y3=np.sin(X2)


plt.plot(X,Y1,c="green",label="Y=X")
plt.plot(X2,Y2,c="red",label="Y=X^2")
plt.plot(X2,Y3,c="blue",label="y=sinX")

plt.legend()
plt.show()
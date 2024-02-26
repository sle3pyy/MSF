import numpy as np  
import matplotlib.pyplot as plt

x=np.arange(200,1200,100)
y=np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])
logY=np.log(y)
logX=np.log(x)
#plt.plot(x,logY,color='r')
#plt.plot(logX,logY,color='r')
plt.semilogy(x,y)
plt.show()
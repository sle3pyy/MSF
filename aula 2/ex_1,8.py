import numpy as np
import matplotlib.pyplot as plt

L=np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])
x=np.arange(0,50,5)

Lsum = np.sum(np.log(L))
xsum = np.sum(x)
Lxsum = np.sum(np.log(L)*x)
L2sum = np.sum(np.log(L)**2)
x2sum = np.sum(x**2)

m=(len(L)*Lxsum-Lsum*xsum)/(len(L)*L2sum-Lsum**2)
b=(L2sum*xsum-Lsum*Lxsum)/(len(L)*L2sum-(Lsum**2))
r=(len(L)*Lxsum-Lsum*xsum)**2/((len(L)*L2sum-Lsum**2)*(len(L)*x2sum-xsum**2))
mErr=np.abs(m)*np.sqrt(((1/r)-1)/(len(L)-2))
bErr=mErr*(np.sqrt(L2sum/len(L)))

print("m = ",m,"+-",mErr)
print("b = ",b,"+-",bErr)
print("r = ",r)

#plt.plot(x,y)
plt.semilogy(x,L)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

L=np.array([222,207.5,194,171.5,153,133,113,92])
x=np.array([2.3,2.2,2,1.8,1.6,1.4,1.2,1])

Lsum = np.sum(L)
xsum = np.sum(x)
Lxsum = np.sum(L*x)
L2sum = np.sum(L**2)
x2sum = np.sum(x**2)

m=(len(L)*Lxsum-Lsum*xsum)/(len(L)*L2sum-Lsum**2)
b=(L2sum*xsum-Lsum*Lxsum)/(len(L)*L2sum-(Lsum**2))
r=(len(L)*Lxsum-Lsum*xsum)**2/((len(L)*L2sum-Lsum**2)*(len(L)*x2sum-xsum**2))
mErr=np.abs(m)*np.sqrt(((1/r)-1)/(len(L)-2))
bErr=mErr*(np.sqrt(L2sum/len(L)))

print("m = ",m,"+-",mErr)
print("b = ",b,"+-",bErr)
print("r = ",r)

plt.scatter(L,x,color='r')
plt.plot(L,m*L+b,'b-')
plt.show()
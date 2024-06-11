import numpy as np
import matplotlib.pyplot as plt

L=np.array([0.15,0.2,0.16,0.11,0.25,0.32,0.4,0.45,0.5,0.55])
x=np.array([1.21,1.4,1.26,1.05,1.6,1.78,2,2.11,2.22,2.33])

k=np.mean((4*np.pi**2*L)/x**2)
kErr=np.std((4*np.pi**2*L)/x**2)
print("k = ",k,"+-",kErr)

#plt.plot(x,L,'o')
logL = np.log(L)
logx = np.log(x)

logLsum = np.sum(logL)
logxsum = np.sum(logx)
logLxsum = np.sum(logL*logx)
logL2sum = np.sum(logL**2)
logx2sum = np.sum(logx**2)

m=(len(logL)*logLxsum-logLsum*logxsum)/(len(logL)*logL2sum-logLsum**2)
b=(logL2sum*logxsum-logLsum*logLxsum)/(len(logL)*logL2sum-(logLsum**2))
r=(len(logL)*logLxsum-logLsum*logxsum)**2/((len(logL)*logL2sum-logLsum**2)*(len(logL)*logx2sum-logxsum**2))
mErr=np.abs(m)*np.sqrt(((1/r)-1)/(len(logL)-2))
bErr=mErr*(np.sqrt(logL2sum/len(logL)))

print("m = ",m,"+-",mErr)
print("b = ",b,"+-",bErr)
print("r = ",r)

plt.plot(np.log(x),np.log(L),'o')
plt.show()
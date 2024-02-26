import numpy as np
import matplotlib.pyplot as plt

x=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
y=np.array(range(0,10))
m=(len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/(len(x)*np.sum(x**2)-np.sum(x)**2)
b=(np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/(len(x)*np.sum(x**2)-np.sum(x)**2)
r=(len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))**2/((len(x)*np.sum(x**2)-np.sum(x)**2)*(len(x)*np.sum(y**2)-np.sum(y)**2))
mErr=np.abs(m)*np.sqrt(((1/r)-1)/(len(x)-2))
bErr=mErr*(np.sqrt(np.sum(x**2)/len(x)))

a=np.polyfit(x,y,1)
print("Polyfit results:",a)

print("m = ",m,"+-",mErr)
print("b = ",b,"+-",bErr)
print("r = ",r)
print("Speed in km/h:",m*3.6,"+-",mErr*3.6)

plt.scatter(y,x,color='r')
plt.show()
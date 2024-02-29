import numpy as np 
import matplotlib.pyplot as plt
import sympy 
t, v, aB = sympy.symbols("t v aB")
t= np.linspace(0,0.01,100)

v=70

xA=v*t

aB=2*12500
xB=0.5*aB*(t**2)

#X=sympy.solve(xA = xB,t)
#print(X)

#plt.plot(t,xA,"r-")
#plt.plot(t,xB,"b")
plt.show()
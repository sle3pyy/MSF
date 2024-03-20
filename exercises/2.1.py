import numpy as np
import matplotlib.pyplot as plt
import sympy


x=np.linspace(0,30,5)
y1= (70/3.6)*x
y2= 0.5*2*x**2

plt.plot(x,y1,"r-")
plt.plot(x,y2,"b-")
plt.show()


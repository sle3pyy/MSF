import numpy as np
import matplotlib.pyplot as plt

a= np.array([2,3,-2])
b= np.array([-1.5,-1,2])

print("o produto vetorial de a e b é:", np.cross(a,b))

#cos(theta)= a.b/(|a||b|)

aNorm= np.linalg.norm(a)
bNorma= np.linalg.norm(b)
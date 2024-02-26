import numpy as np
import matplotlib.pyplot as plt

N=10
X = np.random.normal(4.5,0.5,size=N)
Xmedia = np.mean(X)
Xerro = np.std(X)/np.sqrt(N)

Y = np.random.normal(12.0,0.7,size=N)
Ymedia = np.mean(Y)
Yerro = np.std(Y)/np.sqrt(N)

Z=Y+X
Zmedia = np.mean(Z)
Zerro = np.std(Z)/np.sqrt(N)
Zerro1 = Xerro + Yerro
print(Zerro, Zerro1)

W= Y*X
Wmedia = np.mean(W)
Werro = np.std(W)/np.sqrt(N)
Werro1 = (np.abs(Xerro/Xmedia)+np.abs(Yerro/Ymedia)) * Wmedia
print(Werro,Werro1)
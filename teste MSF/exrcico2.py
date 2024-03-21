import numpy as np
import matplotlib.pyplot as plt

vi=50        #velocidade inicial
t0=0         #tempo inicial
tf=11       #tempo final
dt=0.01
vt=100       #velocidade terminal
g=-9.8       #aceleração gravitacional
D=(g/vt**2)  #constante de arrasto


t= np.arange(t0,tf,dt)   #dominio
v= np.empty(len(t))      #velocidade
y= np.empty(len(t))      #altura
a= np.empty(len(t))      #aceleração
v[0]=vi                  #velocidade incial

for i in range(np.size(t)-1):    #metodo de Euler movimento do fogo de aritificio
    a[i] = g - D*v[i]*np.abs(v[i])
    v[i+1]=v[i]+a[i]*dt  
    y[i+1]=y[i]+v[i]*dt  

#ALINEA A
index_t5 = np.argmin(np.abs(t - 5))   #indice do instante de tempo 5s
plt.plot(t,y,'r')


#ALINEA B 
Hmax = np.argmax(y)   #indice da altura maxima
print("A altura maxima é:",y[Hmax],"no instante de tempo:",t[Hmax])       


#ALINEA C   
#O fogo de arificio explode antes de chegar á altura máxima
Ht5 = y[index_t5]  #altura no instante de tempo 5s
print("O fogo de artificio explode no instante de tempo 5s, logo a diferença entre a altura maxima a altura em que explode é:",y[Hmax]-Ht5)


plt.show()        

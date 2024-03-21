import numpy as np
import matplotlib.pyplot as plt

#VER O FINAL DO CODIGO PARA CORRER ALINE A ALINEA (inicialmente só corre a alinea A)

t=np.array([0,1,2,3,4,5,6,7])
N=np.array([11,20,33,54,83,134,244,425])

def alineaA(t,N):
    Nsum = np.sum(N)
    tsum = np.sum(t)
    Ntsum = np.sum(N*t)
    t2sum = np.sum(t**2)
    N2sum = np.sum(N**2)

    m=(len(N)*Ntsum - tsum*Nsum) / (len(N)*t2sum - tsum**2) 
    b=(Nsum - m*tsum) / len(N)  # y-intercept
    r=(len(N)*Ntsum - Nsum*tsum)**2 / ((len(N)*t2sum - tsum**2)*(len(N)*N2sum - Nsum**2))
    print("The slope of the line is:",m)
    print("The y-intercept is:",b)
    print("The coefficient of determination r2 is:",r)

    plt.plot(t,N,'ro')
    plt.plot(t,m*t+b,'b')
    #pelo grafico e pelo valor de r2 podemos concluir que a relação entre t e N é uma função exponencial e não linear.

def alineaB(t,N):
    plt.semilogy(t,N,'r')
    
    logN= np.log(N)
    Nsum = np.sum(logN)
    tsum = np.sum(t)
    Ntsum = np.sum(logN*t)
    N2sum = np.sum(logN**2)
    t2sum = np.sum(t**2)

    m=(len(N)*Ntsum - tsum*Nsum) / (len(N)*t2sum - tsum**2) 
    b=(Nsum - m*tsum) / len(N)  # y-intercept
    r=(len(N)*Ntsum-Nsum*tsum)**2/((len(N)*N2sum-Nsum**2)*(len(N)*t2sum-tsum**2))  #coeficiente de determinação
    mErr=np.abs(m)*np.sqrt(((1/r)-1)/(len(N)-2))  #erro do declive
    bErr=mErr*(np.sqrt(N2sum/len(N)))   #erro do coeficiente linear

    print("a inclinação da reta é:",m,"+-",mErr)
    print("o coeficiente linear é:",b,"+-",bErr)
    print("o coeficiente de determinaçao r2 é:",r)
     
    plt.plot(t,m*t+b,'b')

def alineaC(t,N):
    #pelos resultados das alineas anteriores podemos concluir que a relação entre t e N é uma função exponencial, e a relação entre ln(N) e t é uma função linear.
    plt.plot(t,N,'ro')

#IMPORTANTE
#para correr uma alinea separadamente, basta comentar as outras duas
#alineaA(t,N)
alineaB(t,N)    
#alineaC(t,N)

plt.show()
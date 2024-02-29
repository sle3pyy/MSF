import numpy as np 
import matplotlib.pyplot as plt
import sympy 

def graphSpeed():
    t,v,g =sympy.symbols("t v g") 
    yA = sympy.lambdify(t, Y.subs({v:6.8, g:9.8}), "numpy")
    t = np.linspace(0,4,100)
    print("v(t)=",Y)
    plt.plot(t,yA(t),"r-")

def graphA():
    t,v,g =sympy.symbols("t v g")    
    aA= sympy.lambdify(t, A.subs({v:6.8, g:9.8}), "numpy") 
    t = np.linspace(0,4,100)
    print("a(t)=",A)
    plt.plot(t,aA(t),"b-")

def solverQueda(height):
    t,v,g =sympy.symbols("t v g") 
    sol=sympy.nsolve((height-y).subs({v:6.8,g:9.8}),t,0) 
    print(sol)

def solverA(height):    
    t,v,g =sympy.symbols("t v g") 
    y=0.5*g*t**2
    sol=sympy.nsolve((height-y).subs({v:6.8,g:9.8}),t,0)
    print(sol)

t,v,g =sympy.symbols("t v g")    
y = (v**2/g)*sympy.log(sympy.cosh(g*t/v))

Y=sympy.diff(y,t)
A=sympy.diff(Y,t)

solverQueda(20)
solverA(20)  
graphA()
graphSpeed()

plt.show()

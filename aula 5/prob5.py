import numpy as np
import matplotlib.pyplot as plt

x=0; y=0; theta=0
pos= np.array([[x,y,theta]]) #posição inicial

ang=45; dist=3
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

ang=90; dist=2
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

ang=45; dist=2
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

ang=45; dist=2
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

ang=90; dist=3
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

xf= x; yf= y; thetaf= theta

dist= np.sqrt(xf**2+yf**2); ang=np.remainder(np.arcsin(-yf/dist)-thetaf,360)
theta+=ang
x+=dist*np.cos(np.deg2rad(-theta))
y+=dist*np.sin(np.deg2rad(-theta))
pos= np.append(pos,[[x,y,theta]],0) #posição final

print(pos)
plt.plot(pos[:,0],pos[:,1])
plt.show()
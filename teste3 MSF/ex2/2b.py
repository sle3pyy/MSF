import numpy as np
import matplotlib.pyplot as plt

def maxminv(x0,x1,x2,y0,y1,y2):
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2)
    # Resultados (output): xm, ymax
    xab = x0 - x1
    xac = x0 - x2
    xbc = x1 - x2
    a = y0 / (xab * xac)
    b = -y1 / (xab * xbc)
    c = y2 / (xac * xbc)
    xmla = (b + c) * x0 + (a + c) * x1 + (a + b) * x2
    xm = 0.5 * xmla / (a + b + c)
    xta = xm - x0
    xtb = xm - x1
    xtc = xm - x2
    ymax = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xm, ymax

t0 = 0.0        # condição inicial, tempo [s]
tf = 200.0      # limite do domínio, tempo final [s]
dt = 0.001      # passo [s]
x0 = 0.2        # condição inicial, posição inicial [m]
v0 = 0.0        # condição inicial, velocidade inicial [m/s]
m = 2.0         # massa [kg]
k = 0.5         # constante da mola [N/m]
b = 0.2         # constante de amortecimento [kg/s]
F_0 = 5         # amplitude da força externa [N]
ω_f = 1         # frequência angular da força externa [rad/s]

# inicializar domínio temporal [s]
t = np.arange(t0, tf, dt)

# inicializar solução
a = np.zeros(np.size(t)) # aceleração [m/s2]
v = np.zeros(np.size(t)) # velocidade [m/s]
x = np.zeros(np.size(t)) # posição [m]
x[0] = x0
v[0] = v0

# método de Euler-Cromer
for i in range(np.size(t) - 1):
    a[i] = (-k * x[i] - b * v[i] + F_0 * np.cos(ω_f * t[i])) / m
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i+1] * dt
 

# arrays com valores máximos, respetivos instantes de tempo, e o período
t_max = np.array([])    # instante de tempo nos máximos
x_max = np.array([])    # máximos de amplitude
T = np.array([])        # período entre máximos 

for i in range(0, np.size(t) - 3, 2):
    # Percorrer domínio temporal em sequências de três:
    # x[i], x[i+1], x[i+2] e respetivos instantes de tempo para i = 0, ..., N-3
    tm, xm = maxminv(t[i], t[i+1], t[i+2], x[i], x[i+1], x[i+2])
    # verificar se extremo está dentro da "janela corrida" (t[i] <-> t[i+2])
    if t[i] < tm and tm < t[i+2]:
        # verificar se é máximo e adicionar a lista se esse for o caso
        if xm > np.maximum(x[i], x[i+2]):
            t_max = np.append(t_max, tm)
            x_max = np.append(x_max, xm)
            # calcular diferenca entre os dois ultimos instantes de tempo
            # e adicionar ao array dos periodos
            T = np.append(T, t_max[np.size(t_max) - 1] - t_max[np.size(t_max) - 2])

print("O período em regime estacionário é T = {0:.2f} s".format(T[-1]))
print("A amplitude em regime estacionário é x_max = {0:.2f} m".format(x_max[-1]))

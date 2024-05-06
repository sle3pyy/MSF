import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
t0 = 0.0  # initial time [s]
tf = 0.5  # final time [s]
dt = 0.001  # time step [s]
r0 = np.array([0.0, 2.0, 3.0])  # initial position [m]
v0 = np.array([160.0, 20.0, -20.0]) * 1000 / 3600  # initial velocity [m/s]
g = 9.8  # gravitational acceleration [m/s^2]

# Calculate terminal velocity and air resistance coefficient
v_T = np.linalg.norm(v0)  # terminal velocity [m/s]
D = g / v_T ** 2  # air resistance coefficient [m^-1]

# Initialize time domain
N = int((tf - t0) / dt + 1)
t = np.linspace(t0, tf, num=N)

# Initialize acceleration arrays
a = np.zeros([np.size(t), 3])  # resultant acceleration
a_res = np.zeros([np.size(t), 3])  # acceleration due to air resistance
a_grv = np.zeros([np.size(t), 3])  # acceleration due to gravity

# Initialize velocity and position arrays
v = np.zeros([np.size(t), 3])
v[0, :] = v0
r = np.zeros([np.size(t), 3])
r[0, :] = r0

# Calculate acceleration
for i in range(np.size(t) - 1):
    a_grv[i, :] = - g * np.array([0.0, 0.0, 1.0])
    a_res[i, :] = - D * np.linalg.norm(v[i, :]) * v[i, :]
    a[i, :] = a_grv[i, :] + a_res[i, :]
    v[i + 1, :] = v[i, :] + a[i, :] * dt
    r[i + 1, :] = r[i, :] + v[i, :] * dt


i_ts = np.size(r[r[:,2] > 0], 0) - 1
ts = t[i_ts]
rs = r[i_ts, :]
print("Tempo no impacto com o campo, t_s = {0:.2f} s".format(ts))
print("Coordenada de impacto no campo, r(t = {0:.2f} s) = ({1:.2f}, {2:.2f}, {3:.2f}")


# representação gráfica das energias
M = 0.057 # massa da bola, [kg]
v_norm = np.linalg.norm(v, axis=1) # norma da velocidade, |v(t)|
E_p = M * g * r[0:i_ts, 2] # energia potencial, [J]
E_c = 0.5 * M * v_norm[0:i_ts] ** 2 # energia cinética, [J]
E_m = E_p + E_c # energia mecânica, [J]


plt.plot(t[0:i_ts], E_p, 'r-', t[0:i_ts], E_c, 'g-', t[0:i_ts], E_m, 'b-')
plt.legend(['E_p', 'E_c', 'E_m'])
plt.xlabel("t [s]")
plt.ylabel("Energia [J]")
plt.title('Decomposição da energia da bola')
plt.show()
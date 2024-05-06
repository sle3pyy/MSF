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

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
# Coordenadas das linhas de campo e rede
x0 = 0
x1 = 18.3 - 11.9
x2 = 11.9
x3 = 18.3
x4 = 2 * 11.9
y0 = 0
y1 = 4.1
y2 = 8.2
z0 = 0.0
z1 = 1.0

ax.plot3D(np.array([x0, x4]), np.array([y0, y0]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x1, x3]), np.array([y1, y1]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x0, x4]), np.array([y2, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x0, x0]), np.array([y0, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x1, x1]), np.array([y0, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x2, x2]), np.array([y0, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x3, x3]), np.array([y0, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x4, x4]), np.array([y0, y2]), np.array([z0, z0]), 'r-')
ax.plot3D(np.array([x2, x2]), np.array([y0, y2]), np.array([z1, z1]), 'k-')
ax.plot3D(np.array([x2, x2]), np.array([y0, y0]), np.array([z0, z1]), 'k-')
ax.plot3D(np.array([x2, x2]), np.array([y2, y2]), np.array([z0, z1]), 'k-')

# Trajetória da bola
ax.plot3D(r[:, 0], r[:, 1], r[:, 2], 'b-')
ax.set_title('Trajetória da bola de ténis em 3D')
ax.set_box_aspect(aspect = (14, 8, 3))
plt.show()
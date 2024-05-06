import numpy as np

a = np.array([2.0, 3.0, -2.0])
b = np.array([-1.5, -1.0, 2.0])

print("O produto vetorial (a x b) é:")

print(np.cross(a,b))

# cos(θ) = a.b / (ab)
a_norm = np.linalg.norm(a)
b_norm = np.linalg.norm(b)
theta = np.arccos(np.inner(a,b) / (a_norm * b_norm))

print('O ângulo entre os vetores "a" e "b" é θ = {0:.2f}°'.format(theta * 180 / np.pi))

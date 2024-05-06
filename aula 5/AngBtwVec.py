import numpy as np
import matplotlib.pyplot as plt

a=np.array([3,4])       #vetor a
b=np.array([4,-3])      #vetor b

#plt.figure(figsize=5)
np.inner(a,b)           #produto interno



dot_product = np.dot(a, b)
# Calculate the magnitudes of a and b
magnitude_a = np.linalg.norm(a)
magnitude_b = np.linalg.norm(b)

# Calculate the angle in radians
angle_rad = np.arccos(dot_product / (magnitude_a * magnitude_b))

# Convert the angle to degrees
angle_deg = np.degrees(angle_rad)

print("The angle between the vectors is", angle_deg, "degrees")
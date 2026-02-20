# # Stream Line Plot

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos

# Create a 2D grid
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Flow parameters
U = 1        # Free stream velocity
R = 1.5      # Radius of the cylinder

# Convert to polar coordinates
r = np.sqrt(X**2 + Y**2)
theta = np.arctan(Y / X)

# Analytical velocity components in polar coordinates (potential flow)
Vr = U * (1 - (R**2 / r**2)) * cos(theta)      # Radial component
Vt = -U * (1 + (R**2 / r**2)) * sin(theta)     # Tangential component

# Transform polar velocities back to Cartesian coordinates
Vx = Vr * cos(theta) - Vt * sin(theta)
Vy = Vr * sin(theta) + Vt * cos(theta)

# Mask the velocity inside the cylinder (where r < R) to hide internal flow
Vx[r < R] = np.nan
Vy[r < R] = np.nan

# Plotting the streamlines
plt.figure(figsize=(5, 5), dpi=100)

# Add the cylinder as a grey circle
circle1 = plt.Circle((0, 0), R, color='grey')
plt.gca().add_patch(circle1)

# Generate streamlines, color them by velocity magnitude
strplot = plt.streamplot(X, Y, Vx, Vy,
                         color=np.sqrt(Vx**2 + Vy**2),
                         density=[1.5, 1.5],
                         cmap='jet')
plt.colorbar(label='Velocity Magnitude')
plt.title('Potential Flow Around a Cylinder')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
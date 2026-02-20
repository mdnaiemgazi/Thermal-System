# Pressure Distribution Around a Circular Cylinder in Potential Flow
# Calculates and visualizes pressure field using potential flow theory

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos

# Create 2D grid for flow domain
x = np.linspace(-5, 5, 500)      # X-coordinate range with higher resolution
y = np.linspace(-5, 5, 500)      # Y-coordinate range with higher resolution
X, Y = np.meshgrid(x, y)         # Generate mesh grid for calculations

# Flow parameters
U = 1                             # Free stream velocity (m/s)
R = 1.5                           # Radius of the cylinder (m)
rho = 1.2                         # Density of the fluid (kg/m³, approximate air density)

# Convert Cartesian coordinates to polar coordinates
r = np.sqrt(X**2 + Y**2)          # Radial distance from cylinder center
theta = np.arctan(Y / X)          # Angular coordinate (radians)

# Calculate pressure field using potential flow theory
# Pressure coefficient formula: Cp = 1 - 4sin²θ for cylinder surface
# Extended to full field: P = (0.5*ρ*U²) * (2*(R/r)²*(cos²θ - sin²θ) - (R/r)⁴)
P = (0.5 * rho * U**2) * ((2 * (R/r)**2 * (cos(theta)**2 - sin(theta)**2) - (R/r)**4))

# Mask the interior of the cylinder (r < R) to avoid unphysical values
P[r < R] = np.nan

# Create visualization
plt.figure(figsize=(5, 5), dpi=100)
circle1 = plt.Circle((0, 0), R, color='grey')   # Draw cylinder as grey circle
plt.gca().add_patch(circle1)

# Generate filled contour plot of pressure distribution
plt.contourf(X, Y, P, 150, cmap='jet')          # 150 contour levels for smooth gradient
plt.colorbar()                                   # Add colorbar for pressure scale
plt.show()
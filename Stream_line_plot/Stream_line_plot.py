# ============================================
# THERMAL SYSTEM STREAMLINE VISUALIZATION
# Author: Naiem Gazi
# Department: Mechanical Engineering, CUET
# ============================================

# Import necessary libraries
import numpy as np  # NumPy for numerical computations and array operations
import matplotlib.pyplot as plt  # Matplotlib for creating visualizations

# ============================================
# PROBLEM STATEMENT
# ============================================
"""
In thermal/fluid systems, understanding flow patterns is crucial.
This code visualizes streamlines for a 2D vector field defined by:
    U = X² + Y - 1
    V = X + Y² + 1
    
These equations represent a simplified flow field that could model
various thermal convection patterns or fluid circulation in a square cavity.
"""

# ============================================
# GRID GENERATION
# ============================================

# Define the domain boundaries
n = 5  # Domain extends from -5 to 5 in both X and Y directions

# Create 100 evenly spaced points in X and Y directions
# This creates a 100x100 grid for high-resolution visualization
x = np.linspace(-n, n, 100)  # 100 points from -5 to 5 in X-direction
y = np.linspace(-n, n, 100)  # 100 points from -5 to 5 in Y-direction

# Generate 2D meshgrid for vector field calculations
# X and Y become 100x100 matrices containing coordinates of every grid point
X, Y = np.meshgrid(x, y)

# ============================================
# VECTOR FIELD DEFINITION
# ============================================
# Define the vector field components
# U represents velocity/momentum in X-direction
# V represents velocity/momentum in Y-direction
U = X**2 + Y - 1  # X-component: quadratic in X, linear in Y
V = X + Y**2 + 1  # Y-component: linear in X, quadratic in Y

# ============================================
# VISUALIZATION SETUP
# ============================================
# Create a figure with specific size (10 inches wide, 5 inches tall)
# This size is optimized for side-by-side comparison
plt.figure(figsize=(10, 5))

# ============================================
# FIRST SUBPLOT: U-Component Streamlines
# ============================================
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot

# Create streamline plot colored by U-component values
# density=[1,1] controls streamline density (1 = moderate density)
# cmap="rainbow" uses rainbow color scheme to show magnitude
stream_U = plt.streamplot(X, Y, U, V, color=U, density=[1, 1], cmap="rainbow")

# Add colorbar to show magnitude scale for U-component
plt.colorbar(stream_U.lines)

# Add labels and title with increased font size for readability
plt.title("Stream Plot - U Component", fontsize=15)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)

# Adjust layout to prevent label overlapping
plt.tight_layout(pad=3)  # pad=3 adds padding between subplots

# ============================================
# SECOND SUBPLOT: V-Component Streamlines
# ============================================
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot

# Create streamline plot colored by V-component values
stream_V = plt.streamplot(X, Y, U, V, color=V, density=[1, 1], cmap="rainbow")

# Add colorbar for V-component
plt.colorbar(stream_V.lines)

# Add labels and title
plt.title("Stream Plot - V Component", fontsize=15)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)

# Set consistent axis limits for both plots
plt.xlim(-n, n)
plt.ylim(-n, n)

# ============================================
# DISPLAY THE PLOTS
# ============================================
plt.show()  # Display the figure window

# ============================================
# OUTPUT DESCRIPTION
# ============================================
"""
The output shows two streamline plots:

LEFT PLOT (U-Component):
- Streamlines colored by U-component magnitude
- U = X² + Y - 1
- Warm colors (red/orange) indicate high U values
- Cool colors (blue/purple) indicate low U values

RIGHT PLOT (V-Component):
- Streamlines colored by V-component magnitude
- V = X + Y² + 1
- Color intensity shows the strength of V-component
- Flow patterns show circulation and stagnation regions

PHYSICAL INTERPRETATION:
- Streamlines show the path a fluid particle would follow
- Color intensity indicates flow speed/magnitude
- Convergence/divergence of streamlines shows acceleration/deceleration
- This pattern could represent natural convection in a square cavity
"""
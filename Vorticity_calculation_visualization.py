"""
Thermal System Analysis Tool
Author: Naiem Gazi (Mechanical Engineering, CUET)
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_vorticity(U, V, dx, dy):
    """Calculate vorticity of the flow field"""
    dVdx = np.gradient(V, dx, axis=1)
    dUdy = np.gradient(U, dy, axis=0)
    return dVdx - dUdy

def plot_streamlines_with_analysis(n=5, points=100):
    """
    Main function to create streamline visualizations
    with engineering analysis
    """
    
    # Create grid
    x = np.linspace(-n, n, points)
    y = np.linspace(-n, n, points)
    X, Y = np.meshgrid(x, y)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    
    # Define velocity field
    U = X**2 + Y - 1
    V = X + Y**2 + 1
    
    # Calculate vorticity for engineering analysis
    vorticity = calculate_vorticity(U, V, dx, dy)
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Thermal System Flow Analysis\n MD Naiem Gazi (CUET)', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: U-component streamlines
    ax1 = axes[0, 0]
    stream1 = ax1.streamplot(X, Y, U, V, color=U, cmap='rainbow', density=1.5)
    plt.colorbar(stream1.lines, ax=ax1, label='U Magnitude')
    ax1.set_title('Flow Field - U Component')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: V-component streamlines
    ax2 = axes[0, 1]
    stream2 = ax2.streamplot(X, Y, U, V, color=V, cmap='rainbow', density=1.5)
    plt.colorbar(stream2.lines, ax=ax2, label='V Magnitude')
    ax2.set_title('Flow Field - V Component')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Velocity magnitude
    ax3 = axes[1, 0]
    magnitude = np.sqrt(U**2 + V**2)
    contour = ax3.contourf(X, Y, magnitude, levels=20, cmap='hot')
    plt.colorbar(contour, ax=ax3, label='Velocity Magnitude')
    ax3.streamplot(X, Y, U, V, color='white', density=1, linewidth=0.5)
    ax3.set_title('Velocity Magnitude Distribution')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    
    # Plot 4: Vorticity
    ax4 = axes[1, 1]
    vort_plot = ax4.contourf(X, Y, vorticity, levels=20, cmap='RdBu_r')
    plt.colorbar(vort_plot, ax=ax4, label='Vorticity')
    ax4.streamplot(X, Y, U, V, color='black', density=1, linewidth=0.5)
    ax4.set_title('Vorticity Field\n(Indicates Rotation)')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    
    plt.tight_layout()
    plt.show()
    
    # Print analysis summary
    print("="*50)
    print("THERMAL SYSTEM ANALYSIS SUMMARY")
    print("="*50)
    print(f"Domain: {2*n} x {2*n} units")
    print(f"Grid Resolution: {points}x{points}")
    print(f"Max Velocity: {np.max(magnitude):.3f}")
    print(f"Min Velocity: {np.min(magnitude):.3f}")
    print(f"Max Vorticity: {np.max(vorticity):.3f}")
    print(f"Min Vorticity: {np.min(vorticity):.3f}")
    print("="*50)
    
    return X, Y, U, V

# Run the analysis
if __name__ == "__main__":

    X, Y, U, V = plot_streamlines_with_analysis()

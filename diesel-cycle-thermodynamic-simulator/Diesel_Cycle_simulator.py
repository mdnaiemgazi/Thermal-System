# Diesel Cycle Simulator
# Basic implementation of diesel cycle thermodynamics and P-V diagram generation

from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import numpy as np  # Added missing import

def volume(d, s, l, r, theta):
    """
    Calculate instantaneous cylinder volume based on crank angle
    
    Parameters:
    d : float - cylinder bore diameter (m)
    s : float - piston stroke (m)
    l : float - connecting rod length (m)
    r : float - compression ratio
    theta : float or array - crank angle (radians)
    
    Returns:
    float or array - instantaneous cylinder volume (m³)
    """
    # Calculate swept volume (displacement volume)
    Vs = (pi/4) * d**2 * s
    
    # Calculate clearance volume from compression ratio
    # r = (Vs + Vc)/Vc, therefore Vc = Vs/(r-1)
    Vc = Vs/(r-1)
    
    # Piston position calculation using slider-crank mechanism
    term1 = 1/(r-1)  # Clearance volume term
    term2 = 1 + (2/s) - cos(theta)  # Piston motion term
    term3 = sqrt((2/s)**2 + (sin(theta))**2)  # Connecting rod correction
    
    # Total instantaneous volume
    V = Vs * (term1 + 0.5 * (term2 - term3))
    
    return V

# Engine geometric parameters
d = 0.1   # bore diameter (m) - 10 cm
s = 0.1   # stroke length (m) - 10 cm
l = 0.15  # connecting rod length (m) - 15 cm
r = 12    # compression ratio

# Thermodynamic initial conditions
p1 = 101.3    # initial pressure (kPa) - atmospheric pressure
t1 = 300      # initial temperature (K) - room temperature
gamma = 1.4   # specific heat ratio for air
t3 = 2500     # peak combustion temperature (K)

# Calculate volumes at key points
Vs = (np.pi/4) * d**2 * s  # swept volume (m³)
Vc = Vs/(r-1)               # clearance volume (m³)
v1 = Vs + Vc                # volume at BDC (state 1)
v2 = Vc                     # volume at TDC (state 2)
v4 = v1                     # volume at end of expansion (state 4)

# Calculate state points for ideal diesel cycle
# Process 1-2: Isentropic compression
p2 = p1 * (r)**gamma        # pressure at end of compression (kPa)
t2 = t1 * r**(gamma-1)      # temperature at end of compression (K)

# Process 2-3: Constant pressure heat addition
p3 = p2                     # constant pressure during combustion
v3 = v2 * t3/t2             # volume at end of heat addition (m³)

# Process 3-4: Isentropic expansion
p4 = p3 * (v3/v4)**gamma    # pressure at end of expansion (kPa)

# Find crank angle corresponding to end of heat addition (state 3)
theta = 0
while theta < np.pi:
    theta = theta + 0.001
    v_theta = volume(d, s, l, r, theta)
    # Find when volume matches v3 (within tolerance)
    if 0 < (v_theta - v3) < 0.001:
        break

print(f"Crank angle at end of combustion: {theta*180/pi:.1f} degrees")

# Generate P-V diagram data
# Compression stroke (0 to π radians)
V_comp = volume(d, s, l, r, np.linspace(0, pi, 180))
P_comp = (p1 * v1**gamma) / V_comp**gamma  # Isentropic relation

# Expansion stroke (π to theta radians)
V_exp = volume(d, s, l, r, np.linspace(pi, theta, 180))
P_exp = (p3 * v3**gamma) / V_exp**gamma    # Isentropic relation

# Plot P-V diagram
plt.figure(figsize=(10, 10))
plt.plot(V_comp, P_comp, 'b-', linewidth=2, label='Compression')
plt.plot([v2, v3], [p2, p3], 'r-', linewidth=2, label='Heat Addition')
plt.plot(V_exp, P_exp, 'g-', linewidth=2, label='Expansion')
plt.plot([v4, v1], [p4, p1], 'orange', linewidth=2, label='Heat Rejection')

# Mark state points
plt.plot(v1, p1, 'ko', markersize=8)
plt.plot(v2, p2, 'ko', markersize=8)
plt.plot(v3, p3, 'ko', markersize=8)
plt.plot(v4, p4, 'ko', markersize=8)
plt.annotate('1', (v1, p1), xytext=(5, 5), textcoords='offset points')
plt.annotate('2', (v2, p2), xytext=(5, 5), textcoords='offset points')
plt.annotate('3', (v3, p3), xytext=(5, 5), textcoords='offset points')
plt.annotate('4', (v4, p4), xytext=(5, 5), textcoords='offset points')

plt.title("PV Diagram Diesel Cycle", fontsize=15)
plt.xlabel("Volume (m³)", fontsize=15)
plt.ylabel("Pressure (kPa)", fontsize=15)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
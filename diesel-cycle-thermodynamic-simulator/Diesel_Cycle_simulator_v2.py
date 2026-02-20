"""
Diesel Cycle Thermodynamic Simulator
------------------------------------
A comprehensive simulator for analyzing ideal diesel cycles,
including P-V diagram generation and efficiency calculations.
"""

import numpy as np
import matplotlib.pyplot as plt


class DieselCycleSimulator:
    """
    A class to simulate and analyze ideal diesel engine cycles.
    
    This simulator calculates thermodynamic state points, generates
    P-V diagrams, and computes thermal efficiency for diesel cycles
    based on engine geometry and operating conditions.
    """
    
    def __init__(self, bore, stroke, connecting_rod_length, compression_ratio):
        """
        Initialize diesel engine parameters.
        
        Parameters:
        -----------
        bore : float
            Cylinder bore diameter (m)
        stroke : float
            Piston stroke length (m)
        connecting_rod_length : float
            Connecting rod length (m)
        compression_ratio : float
            Compression ratio (v1/v2)
        """
        self.bore = bore
        self.stroke = stroke
        self.connecting_rod_length = connecting_rod_length
        self.compression_ratio = compression_ratio
        
        # Calculate fundamental engine volumes
        # Swept volume: volume displaced by piston from TDC to BDC
        self.swept_volume = (np.pi/4) * bore**2 * stroke
        
        # Clearance volume: minimum volume at TDC
        # Derived from: compression_ratio = (swept_volume + clearance_volume)/clearance_volume
        self.clearance_volume = self.swept_volume / (compression_ratio - 1)
        
        # Total cylinder volume at BDC
        self.total_volume = self.swept_volume + self.clearance_volume
        
    def instantaneous_volume(self, crank_angle):
        """
        Calculate instantaneous cylinder volume based on crank angle.
        
        Uses slider-crank mechanism kinematics to determine piston position
        as a function of crank angle.
        
        Parameters:
        -----------
        crank_angle : float or array
            Crank angle in radians (0 = TDC, π = BDC)
            
        Returns:
        --------
        float or array
            Instantaneous cylinder volume (m³)
        """
        # Crank radius (half of stroke)
        R = self.stroke / 2
        
        # Distance from crank center to piston pin
        # Using law of cosines and Pythagorean theorem
        x = R * np.cos(crank_angle) + np.sqrt(
            self.connecting_rod_length**2 - (R * np.sin(crank_angle))**2
        )
        
        # Distance from TDC to current piston position
        h = self.connecting_rod_length + R - x
        
        # Calculate volume: clearance volume + displaced volume
        volume = self.clearance_volume + (np.pi/4) * self.bore**2 * h
        return volume
    
    def ideal_diesel_cycle(self, p1, T1, T3, gamma=1.4):
        """
        Calculate thermodynamic states for ideal diesel cycle.
        
        The ideal diesel cycle consists of:
        1→2: Isentropic compression
        2→3: Constant pressure heat addition (fuel injection/combustion)
        3→4: Isentropic expansion
        4→1: Constant volume heat rejection
        
        Parameters:
        -----------
        p1 : float
            Initial pressure at state 1 (kPa)
        T1 : float
            Initial temperature at state 1 (K)
        T3 : float
            Peak combustion temperature at state 3 (K)
        gamma : float
            Specific heat ratio (cp/cv), default 1.4 for air
            
        Returns:
        --------
        dict
            Dictionary containing state points and cycle properties
        """
        # State 1: Start of compression (Bottom Dead Center)
        v1 = self.total_volume
        
        # State 2: End of compression (Top Dead Center)
        v2 = self.clearance_volume
        # Isentropic relations: pv^γ = constant, Tv^(γ-1) = constant
        p2 = p1 * (self.compression_ratio)**gamma
        T2 = T1 * (self.compression_ratio)**(gamma-1)
        
        # State 3: End of heat addition (constant pressure combustion)
        p3 = p2  # Constant pressure process
        # From ideal gas law at constant pressure: v3/v2 = T3/T2
        v3 = v2 * T3 / T2
        
        # State 4: End of expansion (Bottom Dead Center)
        v4 = v1
        # Isentropic expansion from state 3 to 4
        p4 = p3 * (v3/v4)**gamma
        T4 = T3 * (v3/v4)**(gamma-1)
        
        return {
            'states': {
                1: {'p': p1, 'v': v1, 'T': T1},
                2: {'p': p2, 'v': v2, 'T': T2},
                3: {'p': p3, 'v': v3, 'T': T3},
                4: {'p': p4, 'v': v4, 'T': T4}
            },
            'gamma': gamma,
            'compression_ratio': self.compression_ratio
        }
    
    def generate_pv_diagram(self, cycle_data, n_points=100):
        """
        Generate P-V diagram data points for all four processes.
        
        Parameters:
        -----------
        cycle_data : dict
            Dictionary containing state points from ideal_diesel_cycle()
        n_points : int
            Number of points to generate for each process
            
        Returns:
        --------
        dict
            Dictionary containing (volume, pressure) tuples for each process
        """
        states = cycle_data['states']
        gamma = cycle_data['gamma']
        
        # Process 1-2: Isentropic compression
        # Volume decreases from v1 to v2
        v_12 = np.linspace(states[1]['v'], states[2]['v'], n_points)
        # Isentropic relation: p1*v1^γ = p*v^γ
        p_12 = states[1]['p'] * (states[1]['v'] / v_12)**gamma
        
        # Process 2-3: Constant pressure heat addition
        # Volume increases at constant pressure
        v_23 = np.linspace(states[2]['v'], states[3]['v'], n_points)
        p_23 = np.full_like(v_23, states[2]['p'])
        
        # Process 3-4: Isentropic expansion
        # Volume increases from v3 to v4
        v_34 = np.linspace(states[3]['v'], states[4]['v'], n_points)
        # Isentropic relation from state 3
        p_34 = states[3]['p'] * (states[3]['v'] / v_34)**gamma
        
        # Process 4-1: Constant volume heat rejection
        # Pressure decreases at constant volume
        v_41 = np.full(n_points, states[4]['v'])
        p_41 = np.linspace(states[4]['p'], states[1]['p'], n_points)
        
        return {
            'compression': (v_12, p_12),
            'heat_addition': (v_23, p_23),
            'expansion': (v_34, p_34),
            'heat_rejection': (v_41, p_41)
        }
    
    def calculate_efficiency(self, cycle_data):
        """
        Calculate thermal efficiency of the diesel cycle.
        
        For diesel cycle, efficiency depends on compression ratio and
        cut-off ratio (ρ = v3/v2).
        
        Formula: η = 1 - (1/r^(γ-1)) * (ρ^γ - 1)/(γ(ρ - 1))
        
        Parameters:
        -----------
        cycle_data : dict
            Dictionary containing state points
            
        Returns:
        --------
        float
            Thermal efficiency (0 to 1)
        """
        states = cycle_data['states']
        gamma = cycle_data['gamma']
        
        # Cut-off ratio: volume ratio during constant pressure heat addition
        rho = states[3]['v'] / states[2]['v']
        
        # Diesel cycle efficiency formula
        efficiency = 1 - (1 / self.compression_ratio**(gamma-1)) * \
                     (rho**gamma - 1) / (gamma * (rho - 1))
        
        return efficiency
    
    def plot_pv_diagram(self, cycle_data, title="Diesel Cycle P-V Diagram"):
        """
        Plot the complete P-V diagram with all processes and state points.
        
        Parameters:
        -----------
        cycle_data : dict
            Dictionary containing state points
        title : str
            Plot title
            
        Returns:
        --------
        float
            Thermal efficiency
        """
        pv_data = self.generate_pv_diagram(cycle_data)
        
        plt.figure(figsize=(10, 8))
        
        # Plot each process with distinct colors
        v_comp, p_comp = pv_data['compression']
        v_heat_add, p_heat_add = pv_data['heat_addition']
        v_exp, p_exp = pv_data['expansion']
        v_heat_rej, p_heat_rej = pv_data['heat_rejection']
        
        plt.plot(v_comp, p_comp, 'b-', linewidth=2, label='1→2 Compression (Isentropic)')
        plt.plot(v_heat_add, p_heat_add, 'r-', linewidth=2, label='2→3 Heat Addition (Constant P)')
        plt.plot(v_exp, p_exp, 'g-', linewidth=2, label='3→4 Expansion (Isentropic)')
        plt.plot(v_heat_rej, p_heat_rej, 'orange', linewidth=2, label='4→1 Heat Rejection (Constant V)')
        
        # Mark and label state points
        states = cycle_data['states']
        for i in [1, 2, 3, 4]:
            plt.plot(states[i]['v'], states[i]['p'], 'ko', markersize=8)
            plt.annotate(f'{i}', (states[i]['v'], states[i]['p']),
                        xytext=(5, 5), textcoords='offset points', fontsize=12,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7))
        
        plt.xlabel('Volume (m³)', fontsize=12)
        plt.ylabel('Pressure (kPa)', fontsize=12)
        plt.title(title, fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.legend(loc='best')
        plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
        
        # Calculate and display efficiency
        efficiency = self.calculate_efficiency(cycle_data)
        plt.text(0.05, 0.95, f'Thermal Efficiency: {efficiency:.1%}',
                transform=plt.gca().transAxes, fontsize=12,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8))
        
        # Add cut-off ratio information
        rho = states[3]['v'] / states[2]['v']
        plt.text(0.05, 0.87, f'Cut-off Ratio: {rho:.2f}',
                transform=plt.gca().transAxes, fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8))
        
        plt.tight_layout()
        plt.show()
        
        return efficiency


def main():
    """
    Main function to demonstrate diesel cycle simulation.
    """
    # Engine geometric parameters
    bore = 0.1          # Cylinder bore (10 cm)
    stroke = 0.1        # Piston stroke (10 cm)
    rod_length = 0.15   # Connecting rod length (15 cm)
    compression_ratio = 18  # Typical for diesel engines
    
    # Thermodynamic operating conditions
    p1 = 101.3          # Initial pressure (atmospheric, kPa)
    T1 = 300            # Initial temperature (room temperature, K)
    T3 = 2200           # Peak combustion temperature (K)
    
    # Create simulator instance
    simulator = DieselCycleSimulator(bore, stroke, rod_length, compression_ratio)
    
    # Calculate ideal diesel cycle
    print("Calculating ideal diesel cycle...")
    cycle = simulator.ideal_diesel_cycle(p1, T1, T3)
    
    # Plot P-V diagram and get efficiency
    efficiency = simulator.plot_pv_diagram(cycle)
    
    # Display detailed results
    print("\n" + "="*50)
    print("DIESEL CYCLE ANALYSIS RESULTS")
    print("="*50)
    print(f"Engine Geometry:")
    print(f"  Bore: {bore*1000:.1f} mm")
    print(f"  Stroke: {stroke*1000:.1f} mm")
    print(f"  Connecting Rod: {rod_length*1000:.1f} mm")
    print(f"  Compression Ratio: {compression_ratio}")
    print(f"\nCycle Performance:")
    print(f"  Thermal Efficiency: {efficiency:.1%}")
    print(f"\nState Point Details:")
    print("-"*50)
    print(f"{'State':<8} {'Pressure (kPa)':<16} {'Volume (cm³)':<16} {'Temperature (K)':<16}")
    print("-"*50)
    
    for state, data in cycle['states'].items():
        print(f"{state:<8} {data['p']:<16.1f} {data['v']*1e6:<16.2f} {data['T']:<16.1f}")
    
    print("="*50)


if __name__ == "__main__":
    main()
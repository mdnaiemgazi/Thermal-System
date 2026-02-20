# Diesel Cycle Thermodynamic Simulator

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-orange)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3%2B-green)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Thermodynamics](https://img.shields.io/badge/Thermodynamics-Diesel%20Cycle-red)](https://en.wikipedia.org/wiki/Diesel_cycle)

A comprehensive Python-based simulator for analyzing ideal diesel engine cycles. This tool calculates thermodynamic state points, generates publication-quality P-V diagrams, and computes thermal efficiency based on engine geometry and operating conditions. Perfect for mechanical engineering students, researchers, and automotive enthusiasts studying internal combustion engines.

## 🔍 Project Overview

The Diesel Cycle Thermodynamic Simulator is a computational tool designed to model and visualize the ideal diesel cycle—the thermodynamic cycle that powers diesel engines. By inputting basic engine geometry and operating parameters, the simulator calculates all thermodynamic state points, generates accurate P-V diagrams, and computes key performance metrics such as thermal efficiency and cut-off ratio.

The project includes two implementations:
- **Version 1 (Procedural)**: A straightforward script for beginners to understand the core concepts
- **Version 2 (Object-Oriented)**: A modular, extensible class-based implementation for advanced users and further development

## 🎯 Problem Statement

In mechanical engineering education and research, understanding the thermodynamic behavior of internal combustion engines is fundamental. However, manually calculating state points and visualizing the pressure-volume relationship for diesel cycles is time-consuming, abstract, and prone to errors. This simulator provides an automated, visual, and flexible solution for diesel cycle analysis.

## ✅ Objectives

- Model the four processes of the ideal diesel cycle (compression, heat addition, expansion, heat rejection)
- Calculate pressure, volume, and temperature at all four state points
- Generate accurate P-V diagrams with proper scaling and labeling
- Compute thermal efficiency using the diesel cycle formula
- Determine the cut-off ratio (ρ = v₃/v₂)
- Provide both beginner-friendly and extensible implementations

## ✨ Key Features

- **Thermodynamic State Calculation**: Computes pressure, volume, and temperature at all four critical points of the diesel cycle
- **P-V Diagram Generation**: Automatically generates pressure-volume diagrams with proper scaling and formatting
- **Efficiency Analysis**: Calculates thermal efficiency using the diesel cycle formula
- **Cut-off Ratio Calculation**: Determines the ratio of volumes during constant pressure heat addition
- **Geometric Flexibility**: Accommodates various engine geometries (bore, stroke, connecting rod length)
- **Dual Implementation**: Both procedural and object-oriented versions for learning flexibility

## 🔬 Methodology / Approach

### 1. **Engine Geometry Calculation**
   - Swept volume: V_s = (π/4) × bore² × stroke
   - Clearance volume: V_c = V_s / (r - 1) where r is compression ratio
   - Total volume: V_total = V_s + V_c

### 2. **Instantaneous Volume Function**
   - Uses slider-crank mechanism kinematics to determine piston position
   - Volume = V_c + (π/4) × bore² × piston displacement

### 3. **State Point Calculations**
   - **State 1 (BDC)**: Initial conditions (p₁, T₁, V₁ = V_total)
   - **State 2 (TDC)**: Isentropic compression: p₂ = p₁ × r^γ, T₂ = T₁ × r^(γ-1), V₂ = V_c
   - **State 3 (End of combustion)**: Constant pressure: p₃ = p₂, V₃ = V₂ × T₃/T₂
   - **State 4 (End of expansion)**: Isentropic expansion: p₄ = p₃ × (V₃/V₄)^γ, V₄ = V₁

### 4. **Performance Metrics**
   - Cut-off ratio: ρ = V₃/V₂
   - Thermal efficiency: η = 1 - (1/r^(γ-1)) × (ρ^γ - 1)/(γ(ρ - 1))

## 🛠️ Tools & Technologies

- **Programming Language**: Python 3.7+
- **Numerical Computing**: NumPy 1.20+ for array operations
- **Data Visualization**: Matplotlib 3.3+ for P-V diagram generation
- **Development Environment**: Compatible with any Python IDE (VSCode, PyCharm, Jupyter Notebook)

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/diesel-cycle-thermodynamic-simulator.git

# Navigate to project directory
cd diesel-cycle-thermodynamic-simulator

# Install required packages
pip install numpy matplotlib

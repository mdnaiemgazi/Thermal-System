# Thermal System Analysis - Mechanical Engineering Portfolio

A comprehensive collection of Python-based thermal and fluid dynamics simulation tools for mechanical engineering analysis and visualization.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21+-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-green.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Repository Overview

This repository contains a suite of Python-based simulation tools developed for thermal system analysis, fluid mechanics visualization, and thermodynamic process modeling. Each project demonstrates the application of computational methods to solve real-world mechanical engineering problems, making complex concepts accessible through interactive visualizations and numerical simulations.

The projects range from fundamental heat transfer simulations to advanced potential flow analysis, all designed with educational clarity and research-grade accuracy in mind.

---

## 🎯 Featured Projects

### 1. **Potential Flow Around a Cylinder**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/potential-flow-cylinder)

A computational fluid dynamics (CFD) visualization tool that simulates ideal potential flow past a circular cylinder. The project generates high-quality streamline plots colored by velocity magnitude, demonstrating key fluid mechanics concepts.

**Key Features:**
- Analytical solution of potential flow equations
- Velocity field calculation in polar coordinates
- Colored streamlines showing flow acceleration
- Masked cylinder body for clear visualization

**Sample Output:**

![Potential Flow Around Cylinder](https://github.com/mdnaiemgazi/Thermal-System/blob/main/potential-flow-cylinder/output.png?raw=true)

---

### 2. **Cylinder Pressure Distribution - Potential Flow**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/Cylinder-Pressure-Distribution-Potential-Flow)

Analyzes the pressure coefficient distribution around a circular cylinder in potential flow, comparing theoretical predictions with visualization of pressure variations.

**Key Features:**
- Pressure coefficient (Cp) calculation along cylinder surface
- Comparison of analytical and numerical results
- Symmetric pressure distribution visualization
- Stagnation point identification

---

### 3. **Stream Line Plot Generator**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/Stream_line_plot)

A dedicated tool for generating and customizing streamline plots for various flow configurations, providing flexibility in visualizing fluid motion.

**Key Features:**
- Customizable grid resolution and domain size
- Multiple flow configuration options
- High-resolution output for publications
- Interactive parameter adjustment

---

### 4. **Diesel Cycle Thermodynamic Simulator**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/diesel-cycle-thermodynamic-simulator)

A comprehensive simulation of the ideal Diesel cycle, calculating thermodynamic properties and efficiency at each state point.

**Key Features:**
- P-V and T-S diagram generation
- Thermal efficiency calculation
- Compression ratio analysis
- Heat addition and rejection visualization

---

### 5. **Engine Pin Shear Force Analysis**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/engine-pin-shear-force-analysis)

Structural analysis tool for calculating shear forces and stresses in engine piston pins under various loading conditions.

**Key Features:**
- Shear force distribution along pin length
- Stress concentration visualization
- Safety factor calculations
- Material property integration

---

### 6. **1D Heat Diffusion Simulator**
[![Link](https://img.shields.io/badge/View-Project-blue)](https://github.com/mdnaiemgazi/Thermal-System/tree/main/heat-diffusion-1d-simulator)

A numerical solver for the transient heat conduction equation in one dimension, demonstrating temperature evolution over time.

**Key Features:**
- Finite difference method implementation
- Multiple boundary condition options
- Temperature profile animation
- Thermal diffusivity sensitivity analysis

---

## 🛠️ Common Technologies

All projects in this repository utilize:

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **NumPy** | Numerical computations and array operations |
| **Matplotlib** | Data visualization and plotting |
| **SciPy** | Scientific computing (selected projects) |
| **Jupyter Notebooks** | Interactive development and documentation |

---

## 📊 Problem Statements & Objectives

### **Fluid Mechanics Domain**
- **Problem**: Visualizing complex flow patterns around bluff bodies is challenging without experimental setups.
- **Solution**: Computational fluid dynamics simulations using potential flow theory provide clear, accessible visualizations.
- **Objective**: Bridge the gap between theoretical fluid mechanics and practical visualization.

### **Thermodynamics Domain**
- **Problem**: Understanding thermodynamic cycles requires visualizing pressure-volume and temperature-entropy relationships.
- **Solution**: Interactive cycle simulators with real-time property calculations.
- **Objective**: Make thermodynamic principles tangible through computational modeling.

### **Heat Transfer Domain**
- **Problem**: Transient heat conduction analysis involves complex differential equations.
- **Solution**: Numerical methods with visual output show temperature evolution clearly.
- **Objective**: Demonstrate numerical heat transfer techniques with educational clarity.

---

## 📈 Expected Outcomes

Each project delivers:
- **Visual representations** of engineering phenomena
- **Numerical results** for validation and analysis
- **Educational insights** into underlying physical principles
- **Reproducible code** for further research and development

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy matplotlib scipy jupyter

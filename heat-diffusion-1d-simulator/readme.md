# 1D Transient Heat Diffusion Simulation in a Rod

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7%2B-green)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-red)](https://matplotlib.org/)

## Project Overview

A numerical simulation of transient heat conduction in a 1D rod with fixed-temperature boundary conditions. The model solves the heat equation using the finite difference method (FDM) and visualizes the temperature evolution over time. This project demonstrates fundamental concepts in computational fluid dynamics and heat transfer, making it suitable for academic presentations and portfolio demonstrations.

## Problem Statement

Consider a rod of length L = 5 m initially subjected to a sinusoidal temperature distribution with a maximum of 150°C at its center. Both ends of the rod are maintained at 0°C. The goal is to simulate how heat diffuses through the rod over time until it reaches a steady state, governed by the one-dimensional heat equation:

∂T/∂t = α ∂²T/∂x²

where α is the thermal diffusivity (0.2 m²/s), T is temperature, x is position, and t is time.

## Objectives

- Implement a numerical solver for the 1D transient heat equation using finite differences
- Visualize the temperature profile evolution in real-time
- Demonstrate the physical principle of heat diffusion from high to low temperature regions
- Provide an educational tool for understanding numerical methods in heat transfer

## Methodology / Approach

The simulation employs the **Method of Lines (MOL)** approach:

1. **Spatial Discretization**: The rod is divided into 150 equally spaced points. The second-order spatial derivative is approximated using the central finite difference scheme:

   ∂²T/∂x² ≈ (Tᵢ₊₁ - 2Tᵢ + Tᵢ₋₁) / Δx²

2. **Temporal Integration**: The resulting system of ordinary differential equations (ODEs) is solved using SciPy's `odeint` solver, which implements the LSODA algorithm (adaptive time-stepping).

3. **Boundary Conditions**: Dirichlet (fixed temperature) conditions are applied at both ends: T(0,t) = T(L,t) = 0°C.

4. **Initial Condition**: A half-sine wave profile: T(x,0) = 150 · sin(πx/L) °C.

5. **Visualization**: Real-time plotting shows the temperature profile evolution, with the initial profile as reference.

## Tools & Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3 | Primary programming language |
| NumPy | Array operations and numerical computations |
| SciPy (integrate.odeint) | ODE solver for time integration |
| Matplotlib | Real-time visualization and plotting |
| Finite Difference Method | Numerical discretization of PDE |

## Installation Instructions

1. **Clone or download** this repository to your local machine.

2. **Install Python 3.7+** if not already installed ([python.org](https://www.python.org/)).

3. **Install required libraries** using pip:

```bash
pip install numpy scipy matplotlib

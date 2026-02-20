# 🌊 Thermal System Streamline Visualization

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.5%2B-orange)
![NumPy](https://img.shields.io/badge/numpy-1.21%2B-green)

## 👨‍🔬 Author
**MD Naiem Gazi**  
*Mechanical Engineering, CUET (Chittagong University of Engineering & Technology)*

## 📋 Project Description
This project visualizes streamline patterns in thermal/fluid systems using Python. It demonstrates the application of numerical methods and visualization techniques in mechanical engineering problems.

## 🔧 Mathematical Model
The code visualizes streamlines for a 2D vector field defined by:
- **U(x,y) = x² + y - 1** (X-direction component)
- **V(x,y) = x + y² + 1** (Y-direction component)

These equations model simplified flow patterns that can represent:
- Natural convection currents
- Fluid circulation in cavities
- Thermal gradient-driven flows

## 📊 Output Visualization
!1(streamline_plot.png)
!2(Thermal_System_Flow_Analysis.png)

The visualization shows:
- **Left plot**: Streamlines colored by U-component magnitude
- **Right plot**: Streamlines colored by V-component magnitude
- Rainbow colormap indicates flow intensity

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy matplotlib

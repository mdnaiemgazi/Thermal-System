# engine_shear_force_analysis.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- 1. Load the engine data ---
# Use the FULL PATH to your CSV file
file_path = r"C:\Users\Asus\OneDrive\Desktop\Projects by ME\Python\reading the from file\engine_file.csv"
eng_data = pd.read_csv(file_path, nrows=722)

# Display the first few rows to verify data structure
print("Data loaded successfully!")
print(eng_data.head())
print(f"\nData shape: {eng_data.shape}")

# --- 2. Extract data for plotting ---
x1 = eng_data["Crank Angle (deg)"]
y1 = eng_data["Shear Force Pin_1"]
y2 = eng_data["Shear Force Pin_2"]

# --- 3. Generate the plot ---
plt.figure(figsize=(12, 6))

plt.plot(x1, y1, linewidth=2, label="Pin 1 Shear Force", color='blue')
plt.plot(x1, y2, linewidth=2, label="Pin 2 Shear Force", color='red')

plt.legend(fontsize=12)
plt.xlim(0, 720)
plt.xlabel("Crank Angle (degrees)", fontsize=12)
plt.ylabel("Shear Force (N)", fontsize=12)
plt.title("Shear Force on Pins vs. Crank Angle - Full Engine Cycle", fontsize=14)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Optional: Save the plot
# plt.savefig('shear_force_plot.png', dpi=300, bbox_inches='tight')
import matplotlib.pyplot as mp
import pandas as pd

# Data
height = [121.9, 124.5, 129.5, 134.6, 139.7, 147.3, 152.4, 157.5, 162.6]
weight = [19.7, 21.3, 23.5, 25.9, 28.5, 32.1, 35.7, 39.6, 43.2]

# Creating a DataFrame
df = pd.DataFrame({'height': height, 'weight': weight})

# Plot Configuration
mp.title("Average Weight with Respect to Average Height")
mp.xlabel("Weight in kg")
mp.ylabel("Height in cm")

# Plotting
mp.plot(df.height, df.weight, marker='o', markersize=10, color="green", linewidth=2, linestyle='dashdot')
mp.grid(True)
mp.show()

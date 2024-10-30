import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Base directory containing subdirectories of CSV files
base_dir = '/mnt/data/CSI-HAR-Dataset/CSI-HAR-Dataset/'

# Function to process each CSV file and plot the data
def process_and_plot_csv(file_path):
    # Read CSV into a NumPy array
    M = np.genfromtxt(file_path, delimiter=',')
    
    # Create pseudocolor plot
    plt.figure()
    plt.pcolor(M, cmap='viridis', shading='flat')  # 'flat' shading equivalent
    plt.axis('off')  # Turn off the axis
    plt.title(f'Plot for {os.path.basename(file_path)}')  # Optional: Add title to each plot
    plt.colorbar()  # Optional: add a colorbar for reference
    plt.show()

# Iterate through each subdirectory and CSV file
for subdir, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(subdir, file)
            process_and_plot_csv(file_path)  # Process each CSV file


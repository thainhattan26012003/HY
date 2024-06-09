import csv
import numpy as np
import pandas as pd

# Load data from CSV file
filename = "Trinh_ngu.csv"

# Initialize lists to store data
data = []

# Read data from CSV file
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

# Convert data to numpy array for calculations
data_array = np.array(data)

# Remove non-numeric columns
numeric_data = data_array[:, 1:7].astype(float)

# Calculate mean for each column
column_means = np.mean(numeric_data, axis=0)

# Print the mean for each column
print("Mean for each column:")
print(column_means)


df = pd.read_csv('Trinh_ngu.csv')
a = df.iloc[:, 1:2].values.tolist()
print(np.mean(a))
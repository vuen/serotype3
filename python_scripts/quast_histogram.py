#!/usr/bin/env python

#Date:    04.08.23
#Author:  Vuyelwa Nkomo
#version1


#Creating a histogram based on the N50 values and adding a cut off value


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/filtered_transposed_report2.csv')

# Extract values from the 'N50' column
n50_values = data['N50']

# Create a histogram
plt.hist(n50_values, bins=20, color='blue', alpha=0.7)

# Add a vertical line at the cutoff value of 5000
plt.axvline(x=5000, color='red', linestyle='dashed', linewidth=2, label='Cutoff at 5000')

# Add labels and title
plt.xlabel('N50 Contiguity')
plt.ylabel('Number of Isolate Sequences')
plt.title('Histogram of N50 Contiguity')

# Display the histogram
plt.show()


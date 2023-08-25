#!/usr/bin/env python

#03.08.23
#version1

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/metadata_lineage.csv')



# Specify the two columns to calculate the frequencies
column1 = 'GPSC'  # PopPUNK analysis GPSC
column2 = 'GPSC_gpsc'  # Assigned GPSC to Global Pneumoccocal Project

# Calculate the frequencies of unique GPS Cluster for both columns
value_counts1 = data[column1].value_counts()
value_counts2 = data[column2].value_counts()

# Create a list of all unique clusters from both columns
all_unique_values = list(set(value_counts1.index).union(value_counts2.index))

# Fill in missing values with zero frequencies
for value in all_unique_values:
    if value not in value_counts1.index:
        value_counts1[value] = 0
    if value not in value_counts2.index:
        value_counts2[value] = 0

# Sort the frequencies by index
value_counts1 = value_counts1.sort_index()
value_counts2 = value_counts2.sort_index()

# Set up the figure and axis
fig, ax = plt.subplots()

# Create bar charts for both GPSC columns
ax.bar(value_counts1.index, value_counts1.values, width=0.4, align='center', label=column1)
ax.bar(value_counts2.index, value_counts2.values, width=0.4, align='edge', label=column2)

# Add labels and title
ax.set_xlabel('GPS Clusters ')
ax.set_ylabel('Frequency of isolates belonging to each cluster')
ax.set_title(f'Comparison of Frequencies between PopPUNK analysis GPSC and Assigned GPSC to Global Pneumoccocal Project')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

ax.set_xlim(0, max(value_counts1.index.max(), value_counts2.index.max()))
ax.set_ylim(0, max(value_counts1.max(), value_counts2.max()))

# Add a legend
ax.legend()

# Display the bar chart
plt.show()



#!/usr/bin/env python

#03.08.23
#version1

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/metadata_lineage.csv')




# Calculate the count of each unique number in each column
unique_numbers1_counts = data['GPSC'].value_counts()
unique_numbers2_counts = data['GPSC_gpsc'].value_counts()

# Create DataFrames from the unique numbers and counts
df_unique_numbers1 = pd.DataFrame({'GPSC': unique_numbers1_counts.index, 'Frequency of clusters from PopPUNK GPSC analysis': unique_numbers1_counts.values})
df_unique_numbers2 = pd.DataFrame({'GPSC_gpsc': unique_numbers2_counts.index, 'Frequency of clusters from assigned GPSC': unique_numbers2_counts.values})

# Merge the two DataFrames using the 'GPSC' and 'GPSC_gpsc' columns as keys
merged_df = pd.merge(df_unique_numbers1, df_unique_numbers2, how='outer', left_on='GPSC', right_on='GPSC_gpsc')

# Drop the duplicate 'GPSC_gpsc' column
merged_df = merged_df.drop(columns=['GPSC_gpsc'])

# Export the merged DataFrame to a single CSV file
csv_file_merged = 'gpsc_comparison.csv'
merged_df.to_csv(csv_file_merged, index=False)

print(f"Unique numbers and counts from both columns exported to {csv_file_merged}")




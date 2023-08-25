#!/usr/bin/env python

## Date:   12.08.23
## Version 1
## Author: Vuyelwa Nkomo

import pandas as pd
import re


# Sample data
#data = ~/vuyelwa.nkomo/path_to_scripts/metadata_serotype3.csv



# Read data from CSV files into DataFrames
table1 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/metadata_refine2.csv')
table2 = pd.read_csv('~/vuyelwa.nkomo/project_results/gpsc_assignment/gpsc_assignment_external_clusters.csv')

# Create a new column 'GPSC_gpsc' in table1
table1['GPSC_gpsc'] = None

#lues
# Create a vector from table2 with columns 'sample' and 'GPSC', and rename 'GPSC' to 'GPSC_'
vector_table2 = table2[['sample', 'GPSC']].rename(columns={'GPSC': 'GPSC_'})

# Convert values in 'GPSC_' column to integers, handling non-finite values
vector_table2['GPSC_'] = pd.to_numeric(vector_table2['GPSC_'], errors='coerce').astype('Int64')

# Iterate through rows of table1 and concatenate matching rows from vector_table2
for index, row in table1.iterrows():
    matching_rows = vector_table2[vector_table2['sample'] == row['ngsid']]
    concatenated_values = ', '.join(map(str, matching_rows['GPSC_'].dropna()))  # Drop NaN values before converting
    table1.at[index, 'GPSC_gpsc'] = concatenated_values



#pdated table1 to a new CSV file
table1.to_csv('metadata_gpsc.csv', index=False)

print(table1)



#!/usr/bin/env python

## Date:   12.08.23
## Version 1
## Author: Vuyelwa Nkomo

import pandas as pd
import re


# Sample data
#data = ~/vuyelwa.nkomo/path_to_scripts/metadata_serotype3.csv



# Read data from CSV files into DataFrames
table1 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/metadata_gpsc.csv')
table2 = pd.read_csv('~/vuyelwa.nkomo/project_results/poppunk_results_gps_2/poppunk_results_gps_2_microreact_clusters.csv')

import pandas as pd


# Create a new column 'lineage_cluster' in table1
table1['lineage_cluster'] = None

# Create a vector from table2 with columns 'id' and 'Cluster_Cluster__autocolour'
vector_table2 = table2[['id', 'Cluster_Cluster__autocolour']]

# Convert values in 'Cluster_Cluster__autocolour' column to integers
vector_table2['Cluster_Cluster__autocolour'] = vector_table2['Cluster_Cluster__autocolour'].astype(int)

# Iterate through rows of table1 and concatenate matching rows from vector_table2
for index, row in table1.iterrows():
    matching_rows = vector_table2[vector_table2['id'] == row['ngsid']]
    concatenated_values = ', '.join(map(str, matching_rows['Cluster_Cluster__autocolour']))  # Convert integers to strings
    table1.at[index, 'lineage_cluster'] = concatenated_values

# Save the updated table1 to a new CSV file
table1.to_csv('metadata_lineage.csv', index=False)

print(table1)


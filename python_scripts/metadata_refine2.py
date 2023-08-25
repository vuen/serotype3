#!/usr/bin/env python

## Date: 12.08.23
## Author: Vuyelwa Nkomo
## Version 1


import pandas as pd
import re


# Sample data
#data = ~/vuyelwa.nkomo/path_to_scripts/metadata_serotype3.csv


import pandas as pd

# Load data from file
file1 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/metadata_serotype3.csv')

# Select the 'ngsid' column and rename it
new_column_name = 'old_ngsid'
file1[new_column_name] = file1.pop('ngsid')

# Create a new 'ngsid' column with the desired prefix
file1['ngsid'] = file1[new_column_name].astype(str) + '_contigs_fasta'


# Fill missing values in the 'date' column with an empty string
file1['date'].fillna('', inplace=True)

# Split the date column into day, month, and year
file1[['year', 'month', 'day']] = file1['date'].str.split('-', expand=True)

# Convert the new columns to integers
file1['day'] = file1['day'].astype(int)
file1['month'] = file1['month'].astype(int)
file1['year'] = file1['year'].astype(int)


# Export the modified DataFrame to a new CSV file
output_csv = 'metadata_refine2.csv'
file1.to_csv(output_csv, index=False)

print(f"Data exported to '{output_csv}'")




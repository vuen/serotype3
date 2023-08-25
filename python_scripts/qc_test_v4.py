#!/usr/bin/env python

#Date:   04.08.23
#Author: Vuyelwa Nkomo
#version 4
#getting rid of isolates that have more than one species and yield post trim <=70
#addind .sh to file name 

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
df = pd.read_csv('~/serotype3_sequences/serotype_3_clades/serotype3_metadata/serotype3_readqc_data_2396.csv')

# Removing rows where 'mixed_with' is not 'nothing'
df = df[df['mixed_with'] == 'nothing']

# Removing rows where 'yield_post_trim' is less than 70
df = df[df['yield_post_trim'] >= 70]

print(df)

# exporting the results into a csv file
df.to_csv('~/vuyelwa.nkomo/path_to_scripts/csv_and_text_files/filtered_qc_data.csv', index=False)


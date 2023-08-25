#!/usr/bin/env python

#03.08.23
#version1
# creating a new table with the  assemblies that are present in both n50 filtered data and qc filtered data

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
table1 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/filtered_qc_data.csv')
table2 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/filtered_N50_data.csv')


# 
similarities = table1['sampleid'].isin(table2['Assembly'])

similarities_df = table1[similarities]

print(similarities_df)

similarities_df.to_csv('similarities.csv', index=False)





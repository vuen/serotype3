#!/usr/bin/env python

#Date:   03.08.23
#Author: Vuyelwa Nkomo
#version1
 

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
df = pd.read_table('~/vuyelwa.nkomo/project_results/quast_results/transposed_report.tsv')

# mixed_with removes the isolates that have more than one species
# yield_post_trim should be >=70 to be inline with the pipeline metrics
#it doesn't like the yield post trim criteria
criteria = df['N50'] == '>=5000' 

# Extract rows selected criteria
filtered_N50_data = df.loc[criteria]

print(filtered_N50_data)

# Replace 'filtered_data.txt' with the desired name of your text file
filtered_N50_data.to_csv('filtered_N50_data.csv', index=False)


#!/usr/bin/env python

#Date:   01.08.23
#Author: Vuyelwa Nkomo
#Version 1

#getting rid of isolates that have more than one species and yield post trim <=70
#addind .sh to file name 

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
df = pd.read_csv('~/serotype3_sequences/serotype_3_clades/serotype3_metadata/serotype3_readqc_data_2396.csv')

# mixed_with removes the isolates that have more than one species
# yield_post_trim should be >=70 to be inline with the pipeline metrics
criteria = (df['mixed_with'] == 'nothing') & (df['yield_post_trim'] == '>=70')

# Extract rows selected criteria
filtered_qc_data = df.loc[criteria, :]

# naming text file
filtered_qc_data.to_csv('filtered_qc_data.txt', index=False, sep='\t')


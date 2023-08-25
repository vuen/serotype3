#!/usr/bin/env python

#Date:   03.08.23
#Author: Vuyelwa Nkomo
#version 3

#getting rid of isolates that have more than one species and yield post trim <=70
#addind .sh to file name 

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
df = pd.read_csv('~/serotype3_sequences/serotype_3_clades/serotype3_metadata/serotype3_readqc_data_2396.csv')

# Remove rows where 'yield_post_trim' is less than 70
#df = df[df['yield_post_trim'] < 70]

#print('less than 70 yield',df)
# mixed_with removes the isolates that have more than one species
df = df[df['mixed_with'] != 'nothing']

# Remove rows where 'yield_post_trim' is less than 70
#df = df[df['yield_post_trim'] < 70]

print(df)


# naming csv file
df.to_csv('~/vuyelwa.nkomo/path_to_scripts/csv_and_text_files/removed_qc_data2.csv', index=False)

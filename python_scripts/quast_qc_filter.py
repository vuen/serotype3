#!/usr/bin/env python

#Date:   10.08.23
#Author: Vuyelwa Nkomo
#version 1

#This will filter out the N50 <5000

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
df = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/filtered_transposed_report2.csv')

# Test for  rows where 'N50' <5000
df1 = df[df['N50'] < 5000]

print('The below samples have <5000 N50',df1)

#Removing the rows where 'N50' <5000
df = df[df['N50'] >= 5000]

print('The below samples have N50 => 5000',df)


# exporting the results into a csv file
df.to_csv('filtered_quast_qc_data.csv', index=False)

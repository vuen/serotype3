#!/usr/bin/env python

#04.08.23
#version1
#quast analysis results being filtered using  filtered_qc_data

#importing and  installing pandas
#pip install pandas
import pandas as pd

# Loading setotype3_readqc_data_2396.csv dataset into a DataFrame
table1 = pd.read_csv('~/vuyelwa.nkomo/path_to_scripts/filtered_qc_data.csv')
table2 = pd.read_csv('~/vuyelwa.nkomo/project_results/quast_results/transposed_report.tsv', sep='\t')

#for i in table1['sampleid']:
#	for name in table2['Assembly']:
#		

matching_sample_ids = []

# Iterate through each sample ID in table1
for sample_id in table1['sampleid']:
    # Check if the sample ID exists in table2's 'Assembly' column
    if sample_id in table2['Assembly']:
        # If the sample ID exists, add it to the list of matching sample IDs
        matching_sample_ids.append(sample_id)

# Print the matching sample IDs
print("Matching Sample IDs:")
print(matching_sample_ids)

# Filter and print the rows in table2 that have matching sample IDs
matching_rows_table2 = table2.loc[table2['Assembly'].isin(matching_sample_ids)]
print("\nRows in table2 with matching sample IDs:")
print(matching_rows_table2)

# 
#filtered_transposed_report = table1['sampleid'].isin(table2['Assembly'])

#filtered_transposed_report_df = table1[filtered_transposed_report]

#print(filtered_transposed_report_df)

#filtered_transposed_report_df.to_csv('filtered_transposed_report.csv', index=False)





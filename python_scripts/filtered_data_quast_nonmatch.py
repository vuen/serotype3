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

matching_ngs_ids = []

#f i in table
# Iterate through each NGS ID in table1
for ngs_id in table1['ngsid']:
    # Use regex pattern to match 'ngsid' with 'Assembly'
    regex_pattern = r'^{}(_\d+)?(_contigs)?$'.format(ngs_id)
    
    # Use str.match to check if any value in the 'Assembly' column matches the regex pattern
    if table2['Assembly'].astype(str).str.match(regex_pattern).any():
        # If the NGS ID exists, add it to the list of matching NGS IDs
        matching_ngs_ids.append(ngs_id)

# Print the matching NGS IDs
print("Matching NGS IDs:")
print(matching_ngs_ids)

# Filter and store the non-matching rows in table2
non_matching_table2 = table2[~table2['Assembly'].astype(str).str.match('|'.join(map(str, matching_ngs_ids)))]

# Export the non-matching data to a CSV file
non_matching_table2.to_csv('non_matching_qc_data_quast_analysis.csv', index=False)

print("\nRows in table2 with matching NGS IDs:")
print(non_matching_table2)

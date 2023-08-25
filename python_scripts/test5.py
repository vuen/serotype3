#!/usr/bin/env python

# 11.08.23
#version 1





#csv_file_path = "filtered_quast_qc_data.csv"
#search_directory = "/serotype3_sequences/serotype_3_clades/assemblies/"
#keyword_column = "Assemblies"  # Change this to the actual column name
#output_file_path = "new_reference_list.txt"  # Path to the output text file
#file_list = []

import pandas as pd

# Step 1: Modify CSV Column
csv_file_path = 'total_removed_qc.csv'
df = pd.read_csv(csv_file_path)
df['Modified_Assemblies'] = df['Assembly'] + '.fasta'

# Step 2: Create a Vector
assembly_vector = df['Modified_Assemblies'].tolist()

# Step 3: Remove Matches
text_file_path = 'reference_list.txt'
lines_to_keep = []

with open(text_file_path, 'r') as text_file:
    for line in text_file:
        line = line.strip()
        columns = line.split('\t')  # Assuming tab-separated columns
        if len(columns) >= 1 and columns[0] not in assembly_vector:
            lines_to_keep.append(line)

# Write back the filtered lines to the text file
filtered_text_file_path = 'new_reference_list.txt'
with open(filtered_text_file_path, 'w') as filtered_text_file:
    for line in lines_to_keep:
        filtered_text_file.write(line + '\n')

print("Process completed.")


#!/usr/bin/env python

# 11.08.23
#version 1





#csv_file_path = "filtered_quast_qc_data.csv"
#search_directory = "/serotype3_sequences/serotype_3_clades/assemblies/"
#keyword_column = "Assemblies"  
#output_file_path = "new_reference_list.txt"  # Path to the output text file
#file_list = []

import csv
import os

csv_file_path = "filtered_quast_qc_data.csv"
input_file_path = "reference_list.txt"  # Path to the input two-column list file
output_file_path = "new_reference_list.txt"  # Path to the filtered output text file
keyword_column = "Assemblies"  # column name in the CSV

# Load keywords from the CSV 'Assemblies' column
csv_keywords = set()
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if keyword_column in row:
            keyword = row[keyword_column]
            csv_keywords.add(keyword)

# Filter the input two-column list based on the keywords from the CSV
filtered_entries = []
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        file_name, _ = line.strip().split('\t')
        keyword = os.path.splitext(file_name)[0]  # Extract the filename without extension
        if keyword in csv_keywords:
            filtered_entries.append(line)

# Save the filtered list to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(filtered_entries)

print(f"Filtered list has been saved to {output_file_path}")


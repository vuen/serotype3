#!/usr/bin/env python

## 10.08.23
##v1
##Vuyelwa Nkomo


input_file_path = '~vuyelwa.nkomo/path_to_scripts/csv_and_text_files/new_reference_list.txt'
output_file_path = '~vuyelwa.nkomo/path_to_scripts/csv_and_text_files/refine_new_reference_list.txt'

# Read the content of the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Skip the first line (header)
header = lines[0]
lines = lines[1:]

# Process the lines
processed_lines = []
for line in lines:
    parts = line.strip().split(',')
    # Remove the third element (id)
    del parts[2]
    # Join the remaining elements with a tab separator
    processed_line = '\t'.join(parts)
    processed_lines.append(processed_line)

# Write the processed lines to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(processed_lines))

print("Processing complete.")


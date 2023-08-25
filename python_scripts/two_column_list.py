
#!/usr/bin/env python
#Date: 25.08.2023
#Version 1

#This code will generate a two column list of the names of files within the desired folder and their file path. This code was previously done on a seperate computer and had to be recreated. As a two column list was already generated, this output was not used in the project files.



#importing os
import os

#selecting the correct directory
directory_path = "~/serotype3_sequences/serotype_3_clades/assemblies"

with open("file_list.txt", "w") as file:
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            file.write(f"{filename}\t{file_path}\n")

print("File list created successfully.")

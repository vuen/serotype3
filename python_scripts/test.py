#!/usr/bin/env python

import pandas as pd
import re

## Load up the data 
table1 = pd.read_csv("removed_qc_data.csv")
table2 = pd.read_csv("non_matching_qc_data_quast_analysis.csv")

## Create ngsid column in QC data, this subs out the MOLIS and other strings in the
## assemby names to only get the integer ngsid column. 
##table2['ngsid'] = table2['Assembly'].str.replace(r'_H.*$','').str.replace(r'_c.*$','')
table2['ngsid'] = table2['Assembly'].str.replace('_H.*$','', regex=True).str.replace('_c.*$','', regex=True)
## Get the column to match integer type of table 1 
table2['ngsid'] = table2['ngsid'].astype(int)

## Loop through the table2 ngsids to check if they're in the initial QC removed
## Set up empty vectors to store matching and missing ngsids first and an 
## empty variable to store the missing rows of data 
matching_ngsid = []
missing_ngsid = []
missing_df = pd.DataFrame(columns=table2.columns)

for index, row in table2.iterrows():                                               ## This iterates through each row of the df, giving us the row as a series object 
    current_ngsid = row.loc['ngsid']                                               ## This subsets the ngsid value from the current row
    match_df = table1.loc[table1['ngsid'] == current_ngsid]                        ## This searches for a match to the ngsid in the table 1 results 
    if match_df.empty:                                                             ## This tests whether there was a match, if empty there is no match 
        missing_ngsid.append(current_ngsid)                                        ## Appending the current ngsid to the missing values vector
        missing_df = pd.concat([missing_df, row.to_frame().T], ignore_index=True)  ## Appending the current row to the missing df, using pandas concat
    else:
        matching_ngsid.append(current_ngsid)                                       

## Now we have a vector of missing and a vector of matching ngsids 
## as well as a dataframe of the missing values 

print("Matching NGS IDs:")
print(matching_ngsid)

## Check if the number of rows line up - should be len(table2.index) - len(matching_ngsid)
if (len(table2.index) - len(matching_ngsid)) == len(missing_df.index):
    print("Tables match up, no extra missing isolates")

missing_df.to_csv("alt_filt_data_quast.csv", index=False)

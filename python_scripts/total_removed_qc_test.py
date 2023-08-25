#!/usr/bin/env python
#Date: 03.08.2023
#Author: Vuyelwa Nkomo
#Version 1


#This code adds up the total amount of samples that have been removed by the QC process

import pandas as pd
import re

## Load up the data 
table1 = pd.read_csv("removed_qc_data.csv")
table2 = pd.read_csv("removed_qc_data2.csv")

total = pd.concat([table1,table2], ignore_index=True)

print(total)

total.to_csv("total_removed_qc.csv",index=False)

import os
import pandas as pd
import numpy as np

#=========================================================#
#=========== Step 1 Read file and load data ==============#
#=========================================================#
df = pd.read_csv("C:\Temp\", 
    na_values=['NA', '?'])

#np.random.seed(42) # Uncomment this line to get the same shuffle each time
df = df.reindex(np.random.permutation(df.index))
df.reset_index(inplace=True, drop=True)
print(df[0:])

#=========================================================#
#=========== Step 2 Read file and load data ==============#
#=========================================================#

df = pd.read_csv("C:\Temp\", 
    na_values=['NA', '?'])

#np.random.seed(42) # Uncomment this line to get the same shuffle each time
df = df.sort_values(by='EML_CATEGORY', ascending=True)
print(f"Sorted: {df['EML_CATEGORY'].iloc[0]}")
print(df[0:])



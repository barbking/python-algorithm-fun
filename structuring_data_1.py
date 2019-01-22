# Notes on matching data from various sources:
# - check data for data type issues, if all set contain required data (need to remediate data?)
# - ensure datasets place same meaning on data elements (eg date formats, 32-bit vs 16-bit integer)
# - verify data attributes
# - more time spent verifying compatibility of datae from each source, less likely to encounter problems working with data,
#   sometime results may look correct but provide misleading information

# Remediation - dealing with data duplication
import pandas as pd
df = pd.DataFrame({ 'A': [0,0,0,0,0,1,0],
                    'B': [0,2,3,5,0,2,0],
                    'C': [0,3,4,1,0,2,0]})
print(df, "\n")
df = df.drop_duplicates()
print(df)

# Remediation - dealing with missing values
import numpy as np
df = pd.DataFrame({ 'A': [0,0,1,None],
                    'B': [1,2,3,4],
                    'C': [np.NAN,3,4,1]},
                    dtype=int)
print(df, "\n")
values = pd.Series(df.mean(), dtype=int)
print(values, "\n")
# fillna gets rid of missing values such as None or NAN
df = df.fillna(values)
print(df)
import csv
import glob
import pandas as pd

sample_files = glob.glob('./input/1105_thck_nc/*.csv')
list = []
for file in sample_files:
    dff = pd.read_csv(file)
    list.append(dff['Messwert'])

df = pd.concat(list, axis=1)
df.to_csv('merge_result.csv',index=False)

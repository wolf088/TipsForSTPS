import csv
import glob
import pandas as pd

sample_files = glob.glob('./input/t0.6/*.csv')
list = []
for i in range(len(sample_files)):
    filename = 'C:/Users/yoshi/work/vscode/python/research/merge_files/input/t0.6/t0.6_line_'+str(i+1)+'.csv'
    dff = pd.read_csv(filename, names=['No.','pos','T',], skiprows=6)
    list.append(dff['T'])
'''list = []
for file in sample_files:
    dff = pd.read_csv(file, names=['No.','pos','T',], skiprows=6)
    list.append(dff['T'])'''

#print(list)
df = pd.concat(list, axis=1)
#print(df)
df.to_csv('t0.6_merge.csv',index=False)

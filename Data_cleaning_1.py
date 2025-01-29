import pandas as pd
PD=pd.read_csv('C:/Users/PMLS/OneDrive/Desktop/Data cleaning/archive.zip')
print('Raw data:')
print(PD.head(20))
print('refined data:')
PD['RunTime']=PD['RunTime'].ffill()
print(PD.head(20))
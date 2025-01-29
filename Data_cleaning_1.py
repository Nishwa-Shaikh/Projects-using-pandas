import pandas as pd
PD=pd.read_csv('C:/Users/PMLS/OneDrive/Desktop/Data cleaning/archive.zip')
print('Raw data:')
print(PD)
print('refined data:')
PD['RunTime']=PD['RunTime'].ffill()
PD.drop(PD.columns[-1], axis=1, inplace=True)
Votes_2021=PD[PD['YEAR']==('2021')]['VOTES']
Votes_2021=list(Votes_2021)
for i in Votes_2021:
    count=0
    sum=0
    if i!='NaN':
        sum+=i
        count+=1
    if i=='NaN':
        Votes_2021=Votes_2021.index('NaN')
        Votes_2021[Votes_2021]=sum/count
'''print(PD.head(40))'''
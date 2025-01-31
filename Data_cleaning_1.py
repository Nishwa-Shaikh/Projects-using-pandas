import pandas as pd
PD = pd.read_csv("C:/Users/PMLS/Downloads/archive (1).zip")
print('Raw data:')
print(PD.head(40))
PD['RunTime'] = PD['RunTime'].ffill()
PD.drop(PD.columns[-1], axis=1, inplace=True)
PD.columns = PD.columns.str.strip()
# Convert 'YEAR' to string and then extract numeric values
PD['YEAR'] = PD['YEAR'].astype(str).str.extract('(\d+)').astype(float)
# Convert 'VOTES' to numeric (coerce non-numeric values to NaN)
PD['VOTES'] = pd.to_numeric(PD['VOTES'], errors='coerce')
PD['VOTES'] = PD.groupby('YEAR')['VOTES'].transform(lambda x: x.fillna(x.mean()))
PD['VOTES'] = PD['VOTES'].fillna(PD['VOTES'].mean())
PD=PD.dropna(subset=['YEAR'])
PD['GENRE'] = PD['GENRE'].astype(str)
PD['RATING'] = pd.to_numeric(PD['RATING'], errors='coerce')
PD['RATING'] = PD.groupby('GENRE')['RATING'].transform(lambda x: x.fillna(x.mean()))
PD['MOVIES']=PD['MOVIES'].str.strip()
PD['GENRE']=PD['GENRE'].str.strip()
PD['ONE-LINE']=PD['ONE-LINE'].str.strip()
PD['STARS']=PD['STARS'].str.strip()
#For that group that is NaN
PD['RATING'] = PD['RATING'].fillna(PD['RATING'].mean())
save_file_path = "C:/Users/PMLS/Downloads/refined_movie_data_set.csv"
PD.to_csv(save_file_path, index=False, encoding='utf-8')
print(PD)
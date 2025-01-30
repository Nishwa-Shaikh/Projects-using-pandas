import pandas as pd
PD = pd.read_csv("C:/Users/PMLS/Downloads/archive (1).zip")
print('Raw data:')
print(PD.head(40))
PD['RunTime'] = PD['RunTime'].ffill()
PD.drop(PD.columns[-1], axis=1, inplace=True)
# Strip whitespace from column names
PD.columns = PD.columns.str.strip()
# Convert 'YEAR' to string and then extract numeric values
PD['YEAR'] = PD['YEAR'].astype(str).str.extract('(\d+)').astype(float)
# Convert 'VOTES' to numeric (coerce non-numeric values to NaN)
PD['VOTES'] = pd.to_numeric(PD['VOTES'], errors='coerce')
# Fill NaN values in 'VOTES' with the mean of their respective 'YEAR'
PD['VOTES'] = PD.groupby('YEAR')['VOTES'].transform(lambda x: x.fillna(x.mean()))
PD['VOTES'] = PD['VOTES'].fillna(PD['VOTES'].mean())
PD=PD.dropna(subset=['YEAR'])
PD['GENRE'] = PD['GENRE'].astype(str)
# Now, you can fill NaN values in VOTES with the mean of their respective YEAR
PD['RATING'] = pd.to_numeric(PD['RATING'], errors='coerce')
PD['RATING'] = PD.groupby('GENRE')['RATING'].transform(lambda x: x.fillna(x.mean()))
#For that group that is NaN
PD['RATING'] = PD['RATING'].fillna(PD['RATING'].mean())
# Save the refined data into a new CSV file
save_file_path = "C:/Users/PMLS/Downloads/refined_movie_data.csv"
PD.to_csv(save_file_path, index=False, encoding='utf-8')
# Print the confirmation and the refined data
print('Refined data saved to:', save_file_path)
print(PD)

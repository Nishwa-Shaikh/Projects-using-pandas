import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt

# URL of the website
url = "https://www.boxofficemojo.com/franchise/fr3276246789/?sort=openingWeekendGross&ref_=bo_fr__resort#table"

# Fetch the page content
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
response.raise_for_status()  # Ensures the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the table containing the data
table = soup.find('table')  # Adjust the selector based on the actual HTML structure

# Extract table headers
table_headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    row_data = [column.text.strip() for column in columns]
    rows.append(row_data)

# Create a DataFrame for the original data
data = pd.DataFrame(rows, columns=table_headers)

# Save the original data to a CSV file
original_csv_file = "box_office_original_data.csv"
data.to_csv(original_csv_file, index=False, encoding='utf-8')
print('Raw Data: ')
print()
print(data)

# Refine the data
data = data.drop(['Estimated'], axis=1)
data['Rank'] = pd.to_numeric(data['Rank'], errors='coerce')  # Convert 'Rank' to numeric
data = data[(data['Rank'] != 9) & (~data['Rank'].isna()) & (data['Rank']<9)]  # Filter rows
data = data.sort_values(by='Rank', ascending=True)  # Sort by 'Rank'

# Save the refined data to a separate CSV file
refined_csv_file = "box_office_refined_data.csv"
data.to_csv(refined_csv_file, index=False, encoding='utf-8')
data = data.reset_index(drop=True)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.width', 900)
pd.set_option('display.max_colwidth', None)
print()
print("Refined Data:")
print()
print(data)
print('[8 rows x 8 columns]')
print()

# Plot directly from DataFrame
x = data['Release'].iloc[::-1]
y = pd.to_numeric(data['Lifetime Gross'].iloc[::-1].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(int), errors='coerce')

colors=['#191970','green','#FFD700','#36454F','#A9D0F5','grey','#DC143C', '#BEBEBE']
plt.figure(figsize=(9, 6))
plt.bar(x, y, color=colors)
plt.xlabel('Movie')
plt.ylabel('Lifetime Gross ($)')
plt.title('Harry Potter Movies - Lifetime Gross Revenue')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, max(y) * 1.1)
plt.tight_layout()
plt.show()

import pandas as pd
DATA={
    "Age":[39, 50, 38, 53, 28],
    "workclass":['state-gov','self-emp-not-inc','private','private','private'],
    "fnlwgt":[77516, 83311, 215646, 234721, 338409],
    'education':['Bachelors','Bachelors','HS-grad','11th','Bachelors'],
    'education-num':[13,13,9,7,13],
    'martial-status':['Never-married',' Married-civ-spouse', 'Divorced',' Married-civ-spouse',' Married-civ-spouse'],
    "occupation":['Not-in-family','Husband','Not-in-family','Husband','Wife'],
    'race':['White','White','White','Black','Black'],
    'sex':['Male','Male','Male','Male','Female'],
    'capital-gain':[2174, 0, 0, 0, 0],
    'capital-loss':[0, 0, 0, 0, 0],
    'hours-per-week':[40, 13, 40, 40, 40],
    'naive-country':['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary':['<=50','<=50','<=50','<=50','<=50']
}
df=pd.DataFrame(DATA)
race_counts=df['race'].value_counts()
print(race_counts)
print()
men=df[df['sex']=='Male']
Average_men=men['Age'].mean()
print("Average age of men is:",Average_men)
print()
total_people = len(DATA['education'])
bachelors_count = DATA['education'].count('Bachelors')
percentage_bachelors = (bachelors_count / total_people) * 100

print(f"Percentage of people with a Bachelor's degree: {percentage_bachelors:.2f}%")
print()
Advanced_Education=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
advanced_edu_high_salary = Advanced_Education[Advanced_Education['salary'] == '>50K'].shape[0]
total_advanced_edu = Advanced_Education.shape[0]
if total_advanced_edu > 0:
    percentage = (advanced_edu_high_salary / total_advanced_edu) * 100
else:
    percentage=0
print(f"Percentage of people with advanced education earning >50K: {percentage:.2f}%")
print()
advanced_education = ['Bachelors', 'Masters', 'Doctorate']

# Filter people without advanced education
non_advanced_education = [
    (edu, sal) for edu, sal in zip(DATA['education'], DATA['salary'])
    if edu not in advanced_education
]

# Count people without advanced education earning >50K
non_adv_earning_above_50k = sum(1 for edu, sal in non_advanced_education if sal == '>50')

# Total number of people without advanced education
total_non_advanced = len(non_advanced_education)
percentage_non_adv_above_50k = (non_adv_earning_above_50k / total_non_advanced) * 100 if total_non_advanced > 0 else 0

print(f"Percentage of people without advanced education making more than 50K: {percentage_non_adv_above_50k:.2f}%")
print()
Minimun_hours_worked=min(DATA['hours-per-week'])
print(f'The minimum number of hours a person works per week is:',Minimun_hours_worked)
print()
min_hours_workers = []
for i in range(len(DATA['hours-per-week'])):
    if DATA['hours-per-week'][i] == Minimun_hours_worked:
        min_hours_workers.append({
            'salary': DATA['salary'][i]
        })
count_earning_above_50k = 0
for worker in min_hours_workers:
    if worker['salary'] == '>50':
        count_earning_above_50k += 1

# Step 4: Calculate the percentage
total_min_hours_workers = len(min_hours_workers)

if total_min_hours_workers > 0:
    percentage = (count_earning_above_50k / total_min_hours_workers) * 100
else:
    percentage = 0
print(f"Percentage of minimum hour workers earning more than 50K: {percentage:.2f}%")
print()
country_counts = {}
for i in range(len(DATA['naive-country'])):
    country = DATA['naive-country'][i]
    salary = DATA['salary'][i]
    if country not in country_counts:
        country_counts[country] = {'total': 0, '>50K': 0}
    country_counts[country]['total'] += 1
    if salary == '>50':
        country_counts[country]['>50K'] += 1

# Step 2: Calculate percentage and find the country with the highest percentage
highest_country = None
highest_percentage = 0
for country, counts in country_counts.items():
    percentage = (counts['>50K'] / counts['total']) * 100 if counts['total'] > 0 else 0
    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_country = country

print(f"Country with the highest percentage of >50K earners: {highest_country} ({highest_percentage:.2f}%)")
print()
india_high_earners = []
for i in range(len(DATA['naive-country'])):
    if DATA['naive-country'][i] == 'India' and DATA['salary'][i] == '>50':
        india_high_earners.append(DATA['occupation'][i])

# Step 2: Find the most common occupation manually
occupation_count = {}
for occupation in india_high_earners:
    if occupation in occupation_count:
        occupation_count[occupation] += 1
    else:
        occupation_count[occupation] = 1
most_common_occupation = None
most_common_count = 0
for occupation, count in occupation_count.items():
    if count > most_common_count:
        most_common_count = count
        most_common_occupation = occupation

# Display results
if most_common_occupation:
    print(f"Most popular occupation for >50K earners in India: {most_common_occupation}")
else:
    print("No >50K earners found in India.")
    
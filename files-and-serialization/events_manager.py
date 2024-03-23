import pandas as pd

df = pd.read_csv('event_attendees.csv')

first_name = df['first_Name']
zip_codes = df['Zipcode']

print(zip_codes.head())


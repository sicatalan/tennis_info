import requests
import pandas as pd
import json

risky_norris_url = 'https://fintual.cl/api/real_assets/186/days?from_date=2022-01-01'

response = requests.get(risky_norris_url)
#print(response.json())
df = pd.json_normalize(response.json()['data'])
df = df.rename(columns = {'attributes.date': 'date',
'attributes.price': 'price'})
df = df[['date', 'price']]
print(df)

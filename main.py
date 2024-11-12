import json
import requests
import pandas as pd

resp = requests.get('https://disease.sh/v3/covid-19/countries').json()

columns = ['country', 'cases', 'todayCases', 'deaths', 'recovered', 'active', 'population']
data = []

for row in resp:
    filtered_row = {key: row[key] for key in columns if key in row}
    data.append(filtered_row)

# store in file
with open('coviddata.json', 'w') as f:
    json.dump(data, f)

#read data
df = pd.read_json('coviddata.json')

top5 = df.nlargest(n=5, columns='active')[['country', 'cases', 'active', 'population']]
print("\n",top5.to_string(index=False))



# for d in data:
#     print(d)

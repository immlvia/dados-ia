import requests
import pandas as pd
import sqlite3

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response = requests.get(url)
response.raise_for_status()
dado = response.json()
df = pd.json_normalize(dado)

df = df.drop_duplicates() 
df = df.dropna() 

conn = sqlite3.connect('ibge.db')
df.to_sql('estados', conn, if_exists='replace', index=False) 
conn.close() 


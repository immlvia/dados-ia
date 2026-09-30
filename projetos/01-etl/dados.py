import pandas as pf
import sqlite3

df = pf.read_csv('dados_carros.csv')

df = df.drop_duplicates() # remove linhas duplicadas

df = df.dropna() #remove linhas com valores nulos

df.columns = df.columns.str.strip().str.lower() # deixa tudo minusculo e remove espaços em branco

conn = sqlite3.connect('carros.db')

df.to_sql('carros', conn, if_exists='replace', index=False) #cria a tabela carros no banco de dados carros.db

conn.close() # fecha a conexão com o banco de dados
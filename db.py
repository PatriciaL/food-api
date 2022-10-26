import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

#Damos las credenciales

user = "PatriciaLafuente"
passw = "Lapatri86!!"
host = "PatriciaLafuente.mysql.pythonanywhere-services.com"
database = "PatriciaLafuente$foodb"

#Crea una base de datos virtual
db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})

#Conectamos a la base de datos


conn = db.connect()

#url = 'https://drive.google.com/file/d/1aV2wVXbXRjUSWouCDIbzVyzyFbe4DreU/view?usp=sharing'
#path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
#food_df = pd.read_csv(path)

#cols = ["id", "name", "food_group", "food_subgroup"]
#print("FOOD DATAFRAME")
#print(food_df[cols].head())
#print("")

#pasamos el dataframe a la sql
#food_df.to_sql('food',db)

#tables = conn.execute(
    #"SHOW TABLES;"
#)

#Creamos una lista de una tablas

#for table in tables.fetchall():
    #print(table)

#Consultar a SQL id, name , name_scientific

#rows = conn.execute(
#"""
#SELECT

    #id,
    #name,
    #name_scientific

#FROM food LIMIT 10;

#""")

#for row in rows.fetchall():
    #print(row)

url = 'https://drive.google.com/file/d/1t0kpGGWj53DFAiojLTUQd0juiH7NetYW/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
enzyme_df = pd.read_csv(path)

#pasamos el dataframe a la sql
enzyme_df.to_sql('enzyme',db)

conn.close()


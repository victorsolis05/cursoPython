from os import read
from sqlalchemy import create_engine
import csv


#engine = create_engine("sqlite:///wwe.sqlite")
#engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/postgres?client_encoding=utf8")
query = '''
    DROP TABLE IF EXISTS luchadores
'''

engine.execute(query)


query = '''
    CREATE TABLE luchadores(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        wins INTEGER,
        losses INTEGER,
        draws INTEGER
    )
'''

engine.execute(query)

with open("./data/07WWE-Data-2016.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    values = []
    id_contador = 0
    for x in csvreader:
        id_contador +=1
        a,b,c,d = x
        values.append(f"""({id_contador}, '{a.replace("'", " ")}', {b}, {c}, {d})""") #postgresql
        #values.append(f"""({id_contador}, "{a.replace("'", " ")}", {b}, {c}, {d})""") #mysql
    values = ",".join(values)

query = f'''
    INSERT INTO luchadores(id,name, wins, losses, draws)
    VALUES
    {values}
'''
engine.execute(query)

[print(x) for x in engine.execute("select * from luchadores limit 5")]
engine.dispose()

#pd.read_csv("").to_sql("tabla", engine, pack = 500) pandas
#pyflask
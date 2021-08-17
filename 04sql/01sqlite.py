import sqlite3


con = sqlite3.connect("miPrimerBase.db")

cur = con.cursor()

cur.execute("DROP TABLE people")
#Raw SQL
cur.execute('''
    CREATE TABLE people(
        name VARCHAR(30) NOT NULL,
        has_pet BOOLEAN,
        pet_type VARCHAR(30),
        pet_name VARCHAR(30),
        pet_age INT
    )
''')

cur.execute('''
    INSERT INTO people(name, has_pet, pet_type, pet_name, pet_age)
    VALUES
    ("Jose Manuel", true, "perro", "Perejil", 2),
    ("Carlos", true, "perro", "Pelusa", 5),
    ("Roberto", true, "gato", "Cat", 2)
''')

con.commit()


cur.execute("SELECT * FROM people")

print(cur)

resultados = [x for x in cur]
con.close()
print(resultados)

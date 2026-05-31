import sqlite3

# Opprett forbindelse til database (fil blir laget automatisk)
conn = sqlite3.connect("data/stps.db")
cursor = conn.cursor()

# Kjør SQL-script for å lage tabeller
with open("database/schema.sql", "r") as f:
    sql_script = f.read()
    cursor.executescript(sql_script)

conn.commit()

print("Database opprettet!")
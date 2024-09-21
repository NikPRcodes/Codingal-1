import sqlite3
database='database.sqlite'
conn=sqlite3.connect(database)
import pandas as pd
conn.execute("""CREATE TABLE IF NOT EXISTS panda(
             name TEXT,
             age INT,
             rollcall TEXT);
             """)
conn.execute("INSERT INTO panda (name,age,rollcall) \
             VALUES ('Maanas',14,'7')"); 
conn.commit()
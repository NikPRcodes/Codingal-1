import pandas as pd
import sqlite3
database = 'basketball.sqlite'
conn=sqlite3.connect(database)
bla=pd.read_sql("""SELECT * FROM Team c
                LEFT JOIN Team_Attributes co
                ON c.id == co.ID
                WHERE c.state == 'New York' """, conn)
print(bla)
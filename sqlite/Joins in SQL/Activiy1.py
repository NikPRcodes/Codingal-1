import pandas as pd
import sqlite3
database = 'database.sqlite'
conn=sqlite3.connect(database)
bla=pd.read_sql("""SELECT c.Country_Id, c.Country_Name,co.City_Name 
                FROM Country c
                INNER JOIN City co
                ON c.Country_Id ==co.Country_Id """, conn)
print(bla)

outer=pd.read_sql("""SELECT *   
                FROM Player
                LEFT JOIN  Season
                ON Player_Id ==Man_of_the_Series """, conn)

print(outer)

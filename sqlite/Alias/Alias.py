import pandas as pd
import sqlite3 

database="database.sqlite"
conn=sqlite3.connect(database)
match_details=pd.read_sql("""Select Season_Id, Match_Id, v.Venue_Name, c.City_Name, t.Team_Name AS Winner
                          FROM Match
                          INNER JOIN Venue AS v
                          ON Match.Venue_Id == v.Venue_Id 
                          INNER JOIN City AS c
                          ON v.City_Id==c.City_Id
                          INNER JOIN Team as t
                          ON Match.Match_Winner==t.Team_Id""",conn)
print(match_details)
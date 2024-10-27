import matplotlib.pyplot as pt
import pandas as pd
import numpy as np
population=pd.read_csv('Countries Data.csv')

y1952=(population.loc[population['year']==1952])
y2007=(population.loc[population['year']==2007])
ymerge=(y1952.merge(y2007,left_on='country',right_on='country'))
ymerge.drop(['year_x','year_y'],axis=1)
print(y1952.head(12))
print(y2007.head(12))
ymerge['population_growth']=ymerge['population_y']-ymerge['population_x']

ymerge = ymerge.sort_values('population_growth',ascending=False)
ymerge = ymerge.reset_index()
print(ymerge.head(10))
countries=['China','India','United States','Indonesia','Brazil','Pakistan','Bangladesh','Nigeria','Mexico','Philippines']
ymerge = ymerge[ymerge['country'].isin(countries)]
pop_growth=(ymerge['population_growth']/10**6)

pt.figure(figsize=(16,9))
pt.bar(countries,pop_growth,width=0.6)
pt.xlabel('Countries')
pt.ylabel('Population Growth(Millions)')
pt.title('Population Growth per Country')
pt.xticks(rotation=45)
for x,y in zip(countries,pop_growth):
    label = "{:.2f}".format(y)
    pt.annotate(label,
                (x,y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')
pt.show()
import matplotlib.pyplot as pt
import seaborn as sb
import pandas as pd
import numpy as np

titanic=pd.read_csv('Titanic Dataset (1).csv ')
minimum=titanic['Age'].min()
maximum=titanic['Age'].max()
print(minimum)
print(maximum)

bins = [0,15,30,45,60,75]
age_l =['child','young adult','Middle age set1','Middle age set2','Senior']
titanic['binned_age']=pd.cut(titanic['Age'], bins)
titanic['binned_age1']=pd.cut(titanic['Age'], bins, labels=age_l)

print(titanic[['binned_age','Age']].head(1))
print(titanic[['binned_age1','Age']].head(10))

titanic['binned_age1'].value_counts().plot(kind = 'bar')
pt.xlabel('Ages')
pt.ylabel('Count')
pt.show()

titanic['binned_age1'].value_counts().plot(kind = 'bar')

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

titanic=pd.read_csv('Titanic Dataset.csv')
print(titanic.head())
print(titanic.isnull().sum())

q1 =np.quantile(titanic['Age'],0.25)
q2 =np.quantile(titanic['Age'],0.50)
q3 =np.quantile(titanic['Age'],0.75)

print('Age Quartiles:')
print('q1 is',q1)
print('q2 is',q2)
print('q3 is',q3)

iqr=q3-q1
print("iqr of age is",iqr)
pt.hist(titanic['Age'])
pt.xlabel('Age')
pt.ylabel('# of passengers')
pt.show()

q1f =np.quantile(titanic['Fare'],0.25)
q2f =np.quantile(titanic['Fare'],0.50)
q3f =np.quantile(titanic['Fare'],0.75)

print('Fare Quartiles:')
print('q1 is',q1f)
print('q2 is',q2f)
print('q3 is',q3f)

iqrf=q3f-q1f
print("the iqr of the fares is",iqr)
pt.hist(titanic['Fare'])
bins = np.arange(1,250,20)
pt.xlabel('Fare')
pt.ylabel('# of passengers')
pt.show()

pt.boxplot(titanic['Age'])
pt.title('Age distribution')
pt.show()
pt.boxplot(titanic['Pclass'])
pt.title('Passenger class dist')
pt.show()

import pandas as pd

titanic=pd.read_csv('Titanic Dataset.csv')
print(titanic.head())
print(titanic.dtypes)
print(titanic.isnull().sum())

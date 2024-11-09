import seaborn as sb
import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

hear=pd.read_csv('heart.csv')
print(hear.head())
print(hear.columns)
print(hear.shape)
print(hear.describe())
print(hear.isnull().sum())
print(hear.info())

hear.hist(figsize=(12,12), layout=(5,3))
pt.show()
hear.boxplot()
pt.show()
hear.plot(kind='box', subplots=True,layout=(5,3),figsize=(12,12) )
pt.show()
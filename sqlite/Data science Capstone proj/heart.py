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
sb.barplot(data=hear, x='sex', y='chol',hue='target', palette='spring')
pt.show()
print(hear['target'].value_counts())

sb.countplot(x='slope',data=hear,palette='husl',hue='target')
sb.countplot(x='target',data=hear,palette='BuGn',hue='target')
sb.countplot(x='ca',data=hear,hue='target')
pt.show()
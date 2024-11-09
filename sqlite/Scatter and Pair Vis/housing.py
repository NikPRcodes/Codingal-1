import matplotlib.pyplot as pt
import seaborn as sb
import pandas as pd
import numpy as np

housing=pd.read_csv('USA_Housing.csv')
print(housing.head())
print(housing.info())
print(housing.describe())
print(housing.columns)

x=housing['Avg. Area House Age']
y=housing['Price']

pt.scatter(x,y,edgecolor='red')
pt.show()

sb.pairplot(housing,hue='Price')
pt.show()
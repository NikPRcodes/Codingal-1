import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
housing=pd.read_csv('USA_Housing.csv')
print(housing.head(10))
print(housing.info())
print(housing.describe())
print(housing.columns)
sn.pairplot(housing)
plt.show()
#sn.heatmap(housing.corr(),annot=True)
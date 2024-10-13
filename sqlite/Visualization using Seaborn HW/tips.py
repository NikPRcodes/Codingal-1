import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

tips=pd.read_csv('Tips Dataset.csv')
print(tips.head(10))
print(tips.info())
print(tips.describe())
sn.pairplot(tips)
plt.show()
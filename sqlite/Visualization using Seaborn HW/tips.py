import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

tips=pd.read_csv('Tips Dataset.csv')
print(tips.head(10))
print(tips.info())
print(tips.describe())
#sn.pairplot(tips)

sn.displot(tips["size"])
sn.displot(tips["tip"])
sn.displot(tips["total_bill"])
sn.displot(tips["total_bill"], kde=False,)
sn.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")
sn.pairplot(tips, hue ='gender')
plt.show()

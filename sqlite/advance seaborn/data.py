import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Iris Dataset.csv")
print(data.head())
print(data.info())

sb.barplot(x="Species", y="PetalLengthCm" ,data = data)
plt.show()

sb.countplot(x="Species" ,data = data)
plt.show()

sb.boxplot(x="Species", y="PetalLengthCm" ,data = data)
plt.show()

sb.swarmplot(x="Species", y="PetalLengthCm" ,data = data)
plt.show()


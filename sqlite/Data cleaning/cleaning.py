import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
df=pd.read_csv("country_vaccinations.csv")
print(df.head(10))
print(df.isnull().sum())
print(df.isnull().any())
subset=df.iloc[:35,:]
plt.figure(figsize=(12,8))
sb.heatmap(subset.isnull(),cbar=False, 
           cmap="summer")
#plt.show()
#print(df.dropna())
#print(df.dropna(how='all'))
print(subset.dropna(how='all'))
print(subset.fillna(37))
print(subset.fillna(method="ffill"))
print(subset.interpolate())
print(subset.dropna())
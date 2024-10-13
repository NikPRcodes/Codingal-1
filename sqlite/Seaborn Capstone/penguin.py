import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

penguins=pd.read_csv("penguins_size.csv")
print(sb.get_dataset_names())

df=sb.load_dataset('penguins')
print(df.head())
print(df.tail())
print(df.shape)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
#print(df.corr())
#sb.heatmap(df.corr(),cmap='Wistia', annot=True)
df.hist(figsize=(12,8))
plt.show()
df.plot(kind='box',subplots=True, layout=(3,2),sharex=False,sharey=False, figsize=(8,12))
plt.show()
print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

sb.countplot(x='sex',data=df, palette='summer')
plt.show()

sb.countplot(x='island',data=df, palette='RdPu')
plt.show()

sb.countplot(x='species',data=df, palette='YlOrRd')
plt.show()

sb.countplot(x='sex',data=df, palette='rocket', hue='species')
plt.show()

sb.countplot(x='island',data=df, palette='husl', hue='species')
plt.show()

sb.countplot(x='island',data=df, palette='spring', hue= 'sex')
plt.show()

sb.pairplot(data=df, hue='species',palette='mako')
plt.show()
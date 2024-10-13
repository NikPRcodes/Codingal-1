import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

weather=pd.read_csv("Weather Data.csv")
print(weather.head())
print(weather.info())

sb.barplot(x="temperature", y="humidity" ,data = weather)
plt.show()

sb.displot(x='humidity',data = weather,)
plt.show()
sb.histplot(x='humidity',data = weather)
plt.show()

sb.jointplot(x="temperature", y="humidity" ,data = weather)
plt.show()
sb.jointplot(x="temperature", y="humidity" ,data = weather, kind="hex")
plt.show()
sb.jointplot(x="temperature", y="humidity" ,data = weather, kind="kde")
plt.show()

sb.stripplot(x="temperature", y="weather_type" ,data = weather)
plt.show()

sb.swarmplot(x="temperature", y="humidity" ,data = weather, )
plt.show()

sb.boxplot(x="temperature", y="humidity", hue='weather_type',data = weather)
plt.show()

sb.countplot(x="weather_type" ,data = weather)
plt.show()

sb.pointplot(x="humidity", y="temperature", hue='weather_type',data = weather)
plt.show()
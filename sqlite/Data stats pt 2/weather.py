import numpy as np
import seaborn as sb
import pandas as pd
import statistics as stat

weather=pd.read_csv('Weather Dataset.csv')
print(weather.head())
print(weather.info())
print(weather.isnull().sum())
mean_temp = np.mean(weather['Temperature (C)'])
var_temp = np.var(weather['Temperature (C)'])
std_temp = np.std(weather['Temperature (C)'])
print('std is', std_temp)
print('var is', var_temp)
print('mean is', mean_temp)
for i in range(1,13):
    month=weather.loc[weather['month']==i]['Temperature (C)']
    print("For month: ", i)
    print("Mean temperature:",np.mean(month))
    print("Standard Deviation temperature:",np.std(month),"\n\n")
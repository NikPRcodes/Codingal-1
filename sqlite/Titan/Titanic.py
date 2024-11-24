import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

titanic=pd.read_csv('Titanic Dataset (1).csv')

print(titanic.head())
categories=['Name','Ticket','Cabin']
ord_cat = ['Embarked','Gender']


print(titanic['Gender'].value_counts())
gender_cat=['Males','Females']
titanic['Gender']= pd.Categorical(titanic['Gender'],gender_cat,ordered=True)
median_index=np.median(titanic['Gender'].cat.codes)
median_gender = gender_cat[int(median_index)]
print('There are more',median_gender,'in the ship.')

print(titanic['Embarked'].value_counts())
ember_cat=['S','C','Q']
titanic['Embarked']= pd.Categorical(titanic['Embarked'],ember_cat,ordered=True)
median_index1=np.median(titanic['Embarked'].cat.codes)
median_embarked = ember_cat[int(median_index1)]
print('The median of the people is',median_embarked,'on the ship.')

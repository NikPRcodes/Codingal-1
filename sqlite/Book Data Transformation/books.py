import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

book=pd.read_csv('Bestsellers with categories.csv')
print(book.head())
print(book.isnull().sum())





print(book['Genre'].value_counts())
Genre_cat=['Fiction','Non-fiction']
book['Genre']= pd.Categorical(book['Genre'],Genre_cat,ordered=True)
median_index=np.median(book['Genre'].cat.codes)
median_genre = Genre_cat[int(median_index)]
print('There are more',median_genre,'books in the bestsellers area')

sb.countplot(x=book['Genre'], order=book['Genre'].value_counts().index, palette='husl')
plt.show()
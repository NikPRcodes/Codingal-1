import pandas as pd
import numpy as np
titanic=pd.read_csv('Titanic Dataset.csv')

pclass1=np.mean(titanic['Age'])
print(pclass1)
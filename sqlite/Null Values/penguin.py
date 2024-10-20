import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

penguin=pd.read_csv('Penguins Data.csv')
print(penguin.isnull().sum())
sb.stripplot(penguin.isnull() )
plt.show()
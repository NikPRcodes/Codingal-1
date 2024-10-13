import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sales=pd.read_csv("Company Sales Data.csv")
print(sales)
profit_list=sales['total_profit'].tolist()
month=sales['month_number'].tolist()
plt.plot(month,profit_list,label='profit data')
#criteria=['month number','facecream','facewash','toothpaste','bathingsoap','shampoo','moisterizer','total units','total_profit']
plt.title("Company Monthly Profit")
plt.ylabel("Profit")
plt.xlabel("Month Num")
plt.xticks(month)
plt.yticks([100000,200000,300000,400000,500000])
plt.show()
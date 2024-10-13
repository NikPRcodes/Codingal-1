import pandas as pd
import numpy as np

exam_data= {'name':['Maanas','Nikhil','Bob','John','Steve','Alex','Emily','Sophia','Micheal','Nero'],
            'score':[12.5,9,6.5,np.nan,9,20,14.5,np.nan,8,19]
            ,'attempts':[1,3,2,3,1,2,3,1,2,3]
            ,'qualify':['Yes','No','Yes','No','No','Yes','Yes','No','No','Yes',]}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data, index=labels)
print("Summary of basic information about this DATAFrame and its data: ")
print(df.info())
print(df)
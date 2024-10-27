import matplotlib.pyplot as pt

men=[81,90,130,85,150,149,88,93,115,135]
women=[119,67,98,75,89,120,133,69,72,112]

blood_sugar=[men,women]
label1 = ['Men','Women']

bin1=[80,100,125,150]
pt.xlabel('Blood Sugar Range')
pt.ylabel('Total Number of Patients')
pt.hist(blood_sugar,bins=bin1,rwidth=0.9,color=['w','r'], label=label1,orientation='horizontal')
pt.gca().set_facecolor('black')
pt.legend()
pt.show()
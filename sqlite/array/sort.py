import numpy as np

data_type=[('name','S15'),('class',int),('height',float)]
student_details=[('Maanas',9,180.34),('Nikhil',25,176),('Bob',11,100),('John',34,230)] 

students=np.array(student_details, dtype=data_type)
print('Original array')
print(students)
print('Sorted by height')
print(np.sort(students, order='height'))

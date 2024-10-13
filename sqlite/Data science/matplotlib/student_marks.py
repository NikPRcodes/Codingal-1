import matplotlib.pyplot as pt
import numpy as np
student_names=["Bob","John","Tom","Jerry","Steve","Maanas","Nikhil"]
grades=[3.5,4.0,2.5,4.0,3.5,4.0,4.0]
percentage=[]
for i in grades:
    per = (i/4.0)*100
    percentage.append(per)
print(percentage)

#line chart
pt.plot(student_names,grades)
pt.title("Student Grades Graph")
pt.xlabel("Students")
pt.ylabel("GPA")
pt.show()

#Bar graph
pt.bar(student_names,percentage)
pt.title("Student Grades Graph")
pt.xlabel("Students") 
pt.ylabel("Percentage")
pt.show()
import matplotlib.pyplot as pt
Day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
July=[37,15,21,13,30,26,28]
Aug=[2,25,38,23,17,6,12]
pt.figure(figsize=(6,6))
pt.bar(Day,July,width=0.6)
pt.title('Births in One Week of July')
pt.xlabel('Day')
pt.ylabel('Births')
pt.xticks(rotation=45)
for x,y in zip(Day,July):
    label = "{:.2f}".format(y)
    pt.annotate(label,
                (x,y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')
pt.show()
pt.bar(Day,Aug,width=0.6)
pt.title('Births in One Week of Aug')
pt.xlabel('Day')
pt.ylabel('Births')
for x,y in zip(Day,Aug):
    label = "{:.2f}".format(y)
    pt.annotate(label,
                (x,y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')
pt.show()
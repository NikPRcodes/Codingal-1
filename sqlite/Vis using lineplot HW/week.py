import matplotlib.pyplot as pt
Day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
July=[37,15,21,13,30,26,28]
Aug=[2,25,38,23,17,6,12]

pt.plot(Day,July,label='July plot')
pt.plot(Day,Aug,label='August plot')
pt.title('Velocity-Time Graph')
pt.xlabel('Day')
pt.ylabel('Births')
pt.ylim(0,40)
pt.legend()
pt.show()
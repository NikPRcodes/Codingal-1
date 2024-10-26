import matplotlib.pyplot as pt
Sec=[0,5,10,15,20,25,30]
v1=[10,15,20,15,30,5,25]
v2=[5,25,30,20,15,5,10]

pt.plot(Sec,v1, linestyle='dashed', marker='D',label='velocity1')
pt.plot(Sec,v2, linestyle='dashed', marker='D',label='velocity2')
pt.title('Velocity-Time Graph')
pt.xlabel('Time(s)')
pt.ylabel('Velocity(m/s)')
pt.ylim(5,30)
pt.xlim(1,25)
pt.legend()
pt.show()
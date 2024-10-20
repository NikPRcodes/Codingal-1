import matplotlib.pyplot as pt
import numpy as pd

x=pd.arange(1,11,1)
y1=(2*x)+1
y2=(2*x*x)+2
pt.plot(x,y1,'g',linewidth=3,label='y=2x+1')
pt.plot(x,y2,'r',linewidth=3,label='y=2x^2+2')
pt.legend()
pt.show()
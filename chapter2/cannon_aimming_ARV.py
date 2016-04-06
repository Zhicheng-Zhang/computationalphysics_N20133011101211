# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];v=[];v_proper=[]
dt=0.1;g=-10;theta=1;B=0.0004;y0=1.0*math.pow(10,4)



for v_init in range(425000,425400):
    v_init=0.001*v_init
    v.append(v_init)
    v_x.append(v_init*math.cos(theta));v_y.append(v_init*math.sin(theta))
    x.append(0.0);y.append(0.0)
    while x[-1]<=800:
        v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]-B*math.pow(math.e,-y[-1]/y0)*v[-1]*v_x[-1]*dt
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g-B*math.pow(math.e,-y[-1]/y0)*v[-1]*v_y[-1]*dt
        v_y.append(v_y_tmp)
        if math.sqrt((x[-1]-500)**2+(y[-1]-750)**2)<=0.1:
            print '合适的速度：',v_init
            v_proper.append(v_init)
            break
print 'theta=1时，在偏差不超过0.1m的精度下打击到(500m,750m)处的目标的最小速度为：',min(v_proper)
        




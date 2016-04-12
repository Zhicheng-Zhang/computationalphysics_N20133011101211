# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];v_proper=[]
dt=0.01;g=-10;theta=1



for v_init in range(70400,70600):
    v_x.append(0.001*v_init*math.cos(theta));v_y.append(0.001*v_init*math.sin(theta))
    x.append(0.0);y.append(0.0)
    while x[-1]<=600:
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g
        v_y.append(v_y_tmp)
        if math.sqrt((x[-1]-223.14)**2+(y[-1]-176.43)**2)<=0.15:
            print '合适的速度：',0.001*v_init
            v_proper.append(0.001*v_init)
            break
print 'theta=1时，在偏差不超过0.15m的精度下打击到(223.14m,176.43m)处的目标的最小速度为：',min(v_proper)

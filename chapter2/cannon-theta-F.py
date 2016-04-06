# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];t=[];i=[];theta_list=[];x_list=[]
dt=0.01;g=-10;v_init=70


for theta in range(1,int(50*math.pi)):
    i.append(0)
    v_x.append(v_init*math.cos(0.01*theta));v_y.append(v_init*math.sin(0.01*theta))
    x.append(0.0);y.append(0.0);t.append(0.0)
    while y[-1]>=0.0:
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])        
     
    theta_list.append(0.01*theta);x_list.append(x[-1])
    print theta,t[-1],x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'ro')
plt.show()

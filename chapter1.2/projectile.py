# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
y=np.linspace(0.0,9.0,91)
def f(y): return 50*y-5*y**2       #无空气阻力情况下解析解
x=[];v=[];t=[]
dt=0.01;g=-10;end_time=9;b=0.1
x.append(0.0);v.append(50);t.append(0.0)
for i in range(int(end_time/dt)):  
    if v[-1]>=0:                      
        x_tmp=x[-1]+dt*v[-1]     #由于空气阻力在上升与下降过程中方向反向，故而根据速度的正负情况选择阻力方向
        x.append(x_tmp)
        v_tmp=v[-1]+dt*g-b*dt*v[-1]  #该式体现了物体的速度受重力和阻力的双重影响
        v.append(v_tmp)
        t.append(dt*(i+1))
        print t[-1],v[-1],x[-1]
    else:
        x_tmp=x[-1]+dt*v[-1]
        x.append(x_tmp)
        v_tmp=v[-1]+dt*g+b*dt*v[-1]
        v.append(v_tmp)
        t.append(dt*(i+1))
        print t[-1],v[-1],x[-1]

line1,=plt.plot(t,x,color='blue',linewidth=2.5,linestyle='-')
line2,=plt.plot(y,f(y),color='green',linewidth=1.5,linestyle='--')
plt.xlabel("time/(s)");plt.ylabel('displacement/(m)')                  #给图确定图例　
plt.legend((line1,line2),('numerical,with friction',
'analytical,no friction'),loc='upper left')
plt.title('The Time-dependence of the Displacement of An Upward Projectlie')
plt.annotate('peak value 94.74',xy=(4.05,94.738),xytext=(4.4,100),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.annotate('peak value 125',xy=(5.0,125),xytext=(5.3,130),
arrowprops=dict(facecolor='blue',shrink=0.03))          #分别标出有阻力数值解和无阻力解析解的极大值
plt.show()

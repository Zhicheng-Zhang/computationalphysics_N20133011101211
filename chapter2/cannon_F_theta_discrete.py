# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];theta_list=[];x_list=[]
dt=0.01;g=-10;v_init=70

theta=17
v_x.append(v_init*math.cos(math.pi*theta/180));v_y.append(v_init*math.sin(math.pi*theta/180))
x.append(0.0);y.append(0.0)
while y[-1]>=0.0:
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g
    v_y.append(v_y_tmp)
line1,=plt.plot(x,y)
print theta,x[-1],v_x[-1],y[-1],v_y[-1]
plt.show()

theta=30
v_x.append(v_init*math.cos(math.pi*theta/180));v_y.append(v_init*math.sin(math.pi*theta/180))
x.append(0.0);y.append(0.0)
while y[-1]>=0.0:
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g
    v_y.append(v_y_tmp)
line2,=plt.plot(x,y)
print theta,x[-1],v_x[-1],y[-1],v_y[-1]
plt.show()

theta=45

v_x.append(v_init*math.cos(math.pi*theta/180));v_y.append(v_init*math.sin(math.pi*theta/180))
x.append(0.0);y.append(0.0)
while y[-1]>=0.0:
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g
    v_y.append(v_y_tmp)
line3,=plt.plot(x,y)
print theta,x[-1],v_x[-1],y[-1],v_y[-1]
plt.show()

theta=72
v_x.append(v_init*math.cos(math.pi*theta/180));v_y.append(v_init*math.sin(math.pi*theta/180))
x.append(0.0);y.append(0.0)
while y[-1]>=0.0:
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g
    v_y.append(v_y_tmp)
line4,=plt.plot(x,y,color='g',linewidth=1.5,linestyle='-')
print theta,x[-1],v_x[-1],y[-1],v_y[-1]
plt.xlabel("x/(m)");plt.ylabel('y/(m)')
plt.title('The trajectory of a cannon shell without air resistance')
plt.annotate('theta 17degrees',xy=(100,19.3),xytext=(120,12),
arrowprops=dict(arrowstyle="->"))
plt.annotate('theta 30degrees',xy=(100,43.4),xytext=(120,30),
arrowprops=dict(arrowstyle="->"))
plt.annotate('theta 45degrees',xy=(189,116),xytext=(200,100),
arrowprops=dict(arrowstyle="->"))
plt.annotate('theta 72degrees',xy=(188,201),xytext=(208,190),
arrowprops=dict(arrowstyle="->"))
plt.show()

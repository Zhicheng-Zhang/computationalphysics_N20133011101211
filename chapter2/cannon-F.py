import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[]
dt=0.01;g=-10;v_init=71;theta=1
x.append(0.0);y.append(0.0);v_x.append(v_init*math.cos(theta))
v_y.append(v_init*math.sin(theta));
while y[-1]>=0.0:
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g
    v_y.append(v_y_tmp)
    
a=-y[-1]/y[-2]
x.append((x[-1]+a*x[-2])/(1+a))
y.append(0)
print x[-1],v_x[-1],y[-1],v_y[-1]

plt.plot(x,y,color='green',linewidth=1.5,linestyle='-')

plt.show()


import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];t=[];i=[];v=[]
dt=0.1;g=-10;v_init=500;theta=1;B=0.0004;y0=1.0*math.pow(10,4)
x.append(0.0);y.append(0.0);v_x.append(v_init*math.cos(theta));v.append(v_init)
v_y.append(v_init*math.sin(theta));t.append(0.0);i.append(0)
while y[-1]>=0.0:
    v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
    x_tmp=x[-1]+dt*v_x[-1]
    x.append(x_tmp)
    v_x_tmp=v_x[-1]-B*math.pow(math.e,-y[-1]/y0)*v[-1]*v_x[-1]*dt
    v_x.append(v_x_tmp)
    y_tmp=y[-1]+dt*v_y[-1]
    y.append(y_tmp)
    v_y_tmp=v_y[-1]+dt*g-B*math.pow(math.e,-y[-1]/y0)*v[-1]*v_y[-1]*dt
    v_y.append(v_y_tmp)
    i_tmp=i[-1]+1
    i.append(i_tmp)
    t.append(dt*i[-1])
    
a=-y[-1]/y[-2]
x.append((x[-1]+a*x[-2])/(1+a))
y.append(0)
print t[-1],x[-1],v_x[-1],y[-1],v_y[-1]

plt.plot(x,y,color='b',linewidth=1.5,linestyle='-')
plt.xlabel("x/(m)");plt.ylabel('y/(m)')
plt.title('The trajectory of a cannon shell with varying air resistance')
plt.plot([2253,2253],[0,2408],color ='blue', linewidth=2.5, linestyle="--")
plt.plot([0,4000],[0,0],color ='g', linewidth=2.5, linestyle="--")
plt.annotate('2408m',xy=(2253,2408),xytext=(2353,2308),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.annotate('2253m',xy=(2253,0),xytext=(2453,100),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.show()

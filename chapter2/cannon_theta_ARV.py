import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];t=[];i=[];theta_list=[];x_list=[];v=[]
dt=0.01;g=-10;v_init=70;B=0.004;y0=1.0*math.pow(10,1.5)


for theta in range(1,int(50*math.pi)):
    i.append(0);v.append(v_init)
    v_x.append(v_init*math.cos(0.01*theta));v_y.append(v_init*math.sin(0.01*theta))
    x.append(0.0);y.append(0.0);t.append(0.0)
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
        
     
    theta_list.append(0.01*theta);x_list.append(x[-1])
    print theta,t[-1],x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'g-')
plt.xlabel("theta/(rad)");plt.ylabel('shoot range/(m)')
plt.title('shoot range - theta relation of a cannon shell with varying air resistance')
plt.plot([0.85,0.85],[0,357],color ='blue', linewidth=2.5, linestyle="--")
plt.annotate('largest range 357m',xy=(0.85,357),xytext=(1.0,380),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.annotate(' 0.85rad(49degrees)',xy=(0.85,0),xytext=(1.0,20),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.show()


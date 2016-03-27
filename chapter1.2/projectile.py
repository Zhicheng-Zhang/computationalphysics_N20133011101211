import matplotlib.pyplot as plt
import numpy as np
y=np.linspace(0.0,9.0,91)
def f(y): return 50*y-5*y**2
x=[];v=[];t=[]
dt=0.1;g=-10;end_time=9;b=0.01
x.append(0.0);v.append(50);t.append(0.0)
for i in range(int(end_time/dt)):
    if v[-1]>=0:
        x_tmp=x[-1]+dt*v[-1]
        x.append(x_tmp)
        v_tmp=v[-1]+dt*g-b*v[-1]
        v.append(v_tmp)
        t.append(dt*(i+1))
        print t[-1],v[-1],x[-1]
    else:
        x_tmp=x[-1]+dt*v[-1]
        x.append(x_tmp)
        v_tmp=v[-1]+dt*g+b*v[-1]
        v.append(v_tmp)
        t.append(dt*(i+1))
        print t[-1],v[-1],x[-1]

line1,=plt.plot(t,x,color='blue',linewidth=2.5,linestyle='-')
line2,=plt.plot(y,f(y),color='green',linewidth=1.5,linestyle='--')
plt.xlabel("time/(s)");plt.ylabel('displacement/(m)')
plt.legend((line1,line2),('numerical,with friction','analysis,no friction'),loc='upper left')
plt.title('The Time-dependence of the Displacement of An Upward Projectlie')
plt.annotate('peak value 96.58',xy=(4.1,96.58),xytext=(4.4,100),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.annotate('peak value 125',xy=(5.0,125),xytext=(5.3,130),
arrowprops=dict(facecolor='blue',shrink=0.03))
plt.show()

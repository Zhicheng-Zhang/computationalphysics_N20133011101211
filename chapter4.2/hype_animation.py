from math import*
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

T=[];Theta=[]
class planet():
    '''erratic behavior of Saturn's moon:Hyperion'''
def __init__(self):
    self.x=[]
    self.y=[]
    self.vx=[]
    self.vy=[]
    self.theta=[]
    self.t=[]

def running(self,run_t,mvy,theta0):
    GM=4*pi**2;dt=0.0001;l1=0.1;l2=0.2
    omega=[];omega.append(0)
    self.t.append(0)
    m=planet()
    __init__(m)
    self.theta.append(theta0)
    m2=planet()
    __init__(m2)
    m.x.append(1);m.y.append(0);m.vx.append(0);m.vy.append(mvy)
    m1x0=m.x[-1]+l1*cos(self.theta[-1]);m1y0=m.y[-1]+l1*sin(self.theta[-1])
    self.x.append(m1x0);self.y.append(m1y0)
    m2x0=m.x[-1]-l2*cos(self.theta[-1]);m2y0=m.y[-1]-l2*sin(self.theta[-1])
    m2.x.append(m2x0);m2.y.append(m2y0)
    for i in range(int(run_t/dt)):
        l=sqrt(m.x[-1]**2+m.y[-1]**2)
        mvx_med=m.vx[-1]-dt*GM*m.x[-1]/(l**3)
        m.vx.append(mvx_med)
        mvy_med=m.vy[-1]-dt*GM*m.y[-1]/(l**3)
        m.vy.append(mvy_med)
        mx_med=m.x[-1]+m.vx[-1]*dt
        m.x.append(mx_med)
        my_med=m.y[-1]+m.vy[-1]*dt
        m.y.append(my_med)
        omega_med=omega[-1]+-dt*3*GM*(m.x[-1]*sin(self.theta[-1])-m.y[-1]*cos(self.theta[-1]))*(m.x[-1]*cos(self.theta[-1])+m.y[-1]*sin(self.theta[-1]))/(l**5)
        omega.append(omega_med)
        theta_med=self.theta[-1]+omega[-1]*dt
        self.theta.append(theta_med)
        if self.theta[-1]>=pi:
            self.theta[-1]-=2*pi
        m1x0=m.x[-1]+l1*cos(self.theta[-1]);m1y0=m.y[-1]+l1*sin(self.theta[-1])
        self.x.append(m1x0);self.y.append(m1y0)
        m2x0=m.x[-1]-l2*cos(self.theta[-1]);m2y0=m.y[-1]-l2*sin(self.theta[-1])
        m2.x.append(m2x0);m2.y.append(m2y0)
        self.t.append(dt*(i+1))
    return (self.t,self.theta)

def plot_theta(self):
    T.append(self.t)
    Theta.append(self.theta)
    
s=np.arange(3.83,7.83,0.05)
for i in s:
    mvy=i
    m1=planet()
    __init__(m1)
    running(m1,10,mvy,0)
    plot_theta(m1)

    

fig=plt.figure()
ax=plt.axes(xlim=[0,10],ylim=(-4,4))
line,=ax.plot([],[],color='r')
ax.set_xlabel('time/(yr)')
ax.set_ylabel(r'$\theta\quad (radians)$')
ax.set_title('Hyperion     'r'$\theta\quad v.s.\quad time$''')
ecc_text=ax.text(6,3.5,'')

def init():
    line.set_data([],[])
    ecc_text.set_text('')
    return line,ecc_text

def animate(i):
    if i<=len(s)-1:
        line.set_data(T[i],Theta[i])
    ecc_text.set_text(r'$initial\quad velocity=%.2f  HU/yr$' % (0.05*i+3.83))
    return line,ecc_text
anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(s),interval=100,blit=True)
plt.show(fig)




















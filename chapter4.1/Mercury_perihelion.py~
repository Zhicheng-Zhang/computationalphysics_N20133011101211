from math import*
from visual import*
from matplotlib.pyplot import*
import numpy as np
class planet():
    '''It describes the precession of Mercury's perihelion'''
def __init__(self,GMs,step,alpha):
    self.GMs=GMs
    self.dt=step
    self.x=[0.47034]
    self.y=[0]
    self.z=[0]
    self.vx=[0]
    self.vy=[2.59857*pi]
    self.vz=[0]
    self.alpha=alpha

def running(self,time):
    for i in range(int(time/self.dt)):
        r=sqrt(self.x[-1]**2+self.y[-1]**2+self.z[-1]**2)
        vx_med=self.vx[-1]-self.GMs*(1+self.alpha/(r**2))*self.dt*self.x[-1]/(r**3)
        self.vx.append(vx_med)
        vy_med=self.vy[-1]-self.GMs*(1+self.alpha/(r**2))*self.dt*self.y[-1]/(r**3 )
        self.vy.append(vy_med)
        self.vz.append(0)
        x_med=self.x[-1]+self.vx[-1]*self.dt
        self.x.append(x_med)
        y_med=self.y[-1]+self.vy[-1]*self.dt
        self.y.append(y_med)
        self.z.append(0)
    return (self.x,self.y)

def visual_mercury(self):
    sun=sphere(pos=(0,0,0),radius=0.05,color=color.red)
    mercu=sphere(pos=(0,1,0),radius=0.025,color=color.blue)
    mercu.velocity=vector(self.vx[0],self.vy[0],self.vz[0])
    mercu.trail=curve(color=color.yellow)
    for i in range(len(self.x)):
        rate(2000)
        mercu.pos.x=self.x[i]
        mercu.pos.y=self.y[i]
        mercu.pos.z=self.z[i]
        mercu.velocity.x=self.vx[i]
        mercu.velocity.y=self.vy[i]
        mercu.velocity.z=self.vz[i]
        mercu.trail.append(pos=mercu.pos)
    peri_x=[];peri_y=[]
    for j in range(2,len(self.x)):
        if j<=(len(self.x)-2):
            r_jm=sqrt(self.x[j-1]**2+self.y[j-1]**2+self.z[j-1]**2)
            r_j=sqrt(self.x[j]**2+self.y[j]**2+self.z[j]**2)
            r_jp=sqrt(self.x[j+1]**2+self.y[j+1]**2+self.z[j+1]**2)
            if r_j-r_jm>0 and r_jp-r_j<0:
                peri_x.append(self.x[j]),peri_y.append(self.y[j])
    return (peri_x,peri_y)

    
def plot_mercury():
    mercury=planet()
    x=[];y=[]
    xp=[];yp=[]
    __init__(mercury,4*pi**2,0.0001,0.01)
    lis=running(mercury,0.243555*1)
    lisp=visual_mercury(mercury)
    x.extend(lis[0]);y.extend(lis[1])
    xp.extend(lisp[0]);yp.extend(lisp[1])
    plot(x,y,'k-')
    for i in range(len(xp)):
        plot([0,xp[i]],[0,yp[i]],color='blue')   
    ylim(-0.4,0.5)
    scatter(0,0)
    show()
    
def plot_peri(times):
    mercury=planet()
    x=[];y=[]
    __init__(mercury,4*pi**2,0.0001,0.0008)
    running(mercury,0.243555*times)
    lis=visual_mercury(mercury)
    x.extend(lis[0]);y.extend(lis[1])
    t=[];theta=[]
    for i in range(len(x)):
        t.append(0.243555*(i+1))
    for j in range(len(x)):
        theta.append(180/pi*atan(y[j]/x[j]))
    xa=0;x2a=0;ya=0;xya=0
    for k in range(len(x)):
        xa+=t[k]
        ya+=theta[k]
        x2a+=t[k]**2
        xya+=t[k]*theta[k]
    n=len(x)
    xaf=xa/n;yaf=ya/n;x2af=x2a/n;xyaf=xya/n
    slope=(xyaf-xaf*yaf)/(x2af-xaf**2)
    print slope
    time=np.linspace(0,2.5,25,endpoint=True)
    def S(time): return slope*time
    scatter(t,theta,color='red')
    plot(time,S(time),label=r'$\theta=8.634t \qquad (\alpha=0.0008)$',color='black')
    xlabel('time (year)');ylabel(r'$\theta$(degrees)')
    title('Orbit orientation versus time')
    xlim(0,2.5);ylim(0,25)
    legend(loc='upper left')
    show()
def plot_ecc():
    e=[0,0.0111,0.0781,0.1428,0.206,0.2651,0.3227,0.3780]
    p=[4.2467,4.3072,5.3490,6.8066,8.6338,10.7768,13.7120,17.2392]
    plot(e,p,'k-',label=r'$\alpha=0.0008$')
    scatter(e,p,color='red')
    xlabel('eccentricity');ylabel('precession rate')
    title('precession rate versus eccentricity')
    legend(loc='upper left')
    show()
plot_mercury()


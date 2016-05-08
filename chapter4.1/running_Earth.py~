from math import*
from visual import*
class Earth():
    '''spherical celestial body governed by gravity'''
def __init__(self,GMs,step):
    self.GMs=GMs
    self.dt=step
    self.x=[1]
    self.y=[0]
    self.z=[0]
    self.vx=[0]
    self.vy=[2.3*pi]
    self.vz=[0]
    
def running(self,time):
    for i in range(int(time/self.dt)):
        r=sqrt(self.x[-1]**2+self.y[-1]**2+self.z[-1]**2)
        vx_med=self.vx[-1]-self.GMs*self.dt*self.x[-1]/(r**3)
        self.vx.append(vx_med)
        vy_med=self.vy[-1]-self.GMs*self.dt*self.y[-1]/(r**3)
        self.vy.append(vy_med)
        self.vz.append(0)
        x_med=self.x[-1]+self.vx[-1]*self.dt
        self.x.append(x_med)
        y_med=self.y[-1]+self.vy[-1]*self.dt
        self.y.append(y_med)
        self.z.append(0)
        if i<=(1,len(self.x)-2):
            if self.vx[i]*self.vx[i-1]<0:
                print self.x[-1],self.y[-1],self.z[-1]

def visual_earth(self):
    sun=sphere(pos=(0,0,0),radius=0.15,color=color.red)
    earthb=sphere(pos=(0,1,0),radius=0.075,color=color.blue)
    earthb.velocity=vector(self.vx[0],self.vy[0],self.vz[0])
    earthb.trail=curve(color=color.yellow)
    edge1=curve(pos=[(0,0,0),(1,0,0)],color=color.green)
    edge2=curve(pos=[(0,0,0),(1,0,0)],color=color.green)
    v=sqrt(earthb.velocity.x**2+earthb.velocity.y**2+earthb.velocity.z**2)
    r=sqrt(earthb.pos.x**2+earthb.pos.y**2+earthb.pos.z**2)
    print 'Ei=:',0.5*(v**2)-self.GMs/r
    S=0;lab=label(pos=(1.0,1.9),text='Area velocity: %f' % S)
    for i in range(len(self.x)):
        lab.text='Area velocity: %f' % S
        rate(500)
        earthb.pos.x=self.x[i]
        earthb.pos.y=self.y[i]
        earthb.pos.z=self.z[i]
        earthb.velocity.x=self.vx[i]
        earthb.velocity.y=self.vy[i]
        earthb.velocity.z=self.vz[i]
        earthb.trail.append(pos=earthb.pos)
        if i<=(len(self.x)-6):
            edge1.pos=[(0,0,0),(self.x[i+5],self.y[i+5],self.z[i+5])]
        if i>=5:
            edge2.pos=[(0,0,0),(self.x[i-5],self.y[i-5],self.z[i-5])]
        if i<=(len(self.x)-6) and i>=5:
            theta=acos((self.x[i]*self.vx[i]+self.y[i]*self.vy[i]+self.z[i]*self.vz[i])/(sqrt(self.x[i]**2+self.y[i]**2+self.z[i]**2)*sqrt(self.vx[i]**2+self.vy[i]**2+self.vz[i]**2)))
            S=sqrt(self.x[i]**2+self.y[i]**2+self.z[i]**2)*sqrt(self.vx[i]**2+self.vy[i]**2+self.vz[i]**2)*fabs(sin(theta))
    for i in range(len(self.x)):
        if i<=(len(self.x)-2):
            if self.vx[i]*self.vx[i+1]<0 and self.vx[i]>0:
                print i*self.dt

        
    v=sqrt(earthb.velocity.x**2+earthb.velocity.y**2+earthb.velocity.z**2)
    r=sqrt(earthb.pos.x**2+earthb.pos.y**2+earthb.pos.z**2)
    print 'Ef=:',0.5*(v**2)-self.GMs/r
    
    
earth=Earth()
__init__(earth,4*pi**2,0.002)
running(earth,1.79324*5)
visual_earth(earth)

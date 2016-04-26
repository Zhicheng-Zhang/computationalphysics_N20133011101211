from math import*
from matplotlib.pyplot import*
from visual import*

g=9.8;l=9.8;q=0.5

class Pendulum_chaos():
    '''Represents pendulum chaos and presents its various properties '''
    
def __init__(self,FD,OmegaD=2./3,theta0=0.2,omega0=0,run_time=800,step=300*pi):
    self.FD=FD
    self.OmegaD=2./3
    self.theta0=theta0
    self.omega0=omega0
    self.Theta=[theta0]
    self.Omega=[omega0]
    self.period=2*pi/OmegaD
    self.dt=self.period/step
    self.step=step
    self.run_time=run_time
    self.T=[0.0]

def oscillation(self):
    while self.T[-1]<=self.run_time:
        Omega_med=self.Omega[-1]+(-g/l*sin(self.Theta[-1])-q*self.Omega[-1]+self.FD*sin(self.OmegaD*self.T[-1]))*self.dt
        self.Omega.append(Omega_med)
        Theta_med=self.Theta[-1]+self.Omega[-1]*self.dt
        self.Theta.append(Theta_med)
        T_med=self.T[-1]+self.dt
        self.T.append(T_med)
        if self.Theta[-1]>=pi:
            self.Theta[-1]-=2*pi
        elif self.Theta[-1]<=-pi:
            self.Theta[-1]+=2*pi
    return 0

def plot_Theta(self):
    title('Theta versus time')
    xlabel('t/(s)');ylabel('Theta/(radiands)')
    plot(self.T,self.Theta,'k-',label='FD=1.485 step=0.01s')
    legend(loc='upper right',fontsize=9.0)
    show()
def plot_theta_vary(FD):
    pend=Pendulum_chaos()
    __init__(pend,FD)
    oscillation(pend)
    plot_Theta(pend)

def plot_Omega(self):
    title('Omega versus Theta')
    xlabel('Theta/(radians)');ylabel('Theta/(radiands)')
    scatter(self.Theta,self.Omega,color='k',s=1,label='FD=1.2')
    legend(loc='upper right',fontsize=9.0)
    show()
def plot_omega_vary(FD):
    pend=Pendulum_chaos()
    __init__(pend,FD)
    oscillation(pend)
    plot_Omega(pend)
    
def pendulum_3D(self):
    plane=box(pos=(0,0,0),length=3,width=1,height=0.2,material=materials.earth)
    ball=sphere(pos=(6*sin(self.theta0),0,-6*cos(self.theta0)),color=color.red,radius=0.5)
    bar=curve(pos=[plane.pos,ball.pos])
    i=0
    while i<=20000:
        rate(300)
        ball.pos.x=6*sin(self.Theta[i])
        ball.pos.z=-6*cos(self.Theta[i])
        bar.pos=[plane.pos,ball.pos]
        i+=1
def diaplay_pendulum_3D(FD):
    pend=Pendulum_chaos()
    __init__(pend,FD)
    oscillation(pend)
    pendulum_3D(pend)
    
def attractor(self):
    omeg=[];thet=[]
    for j in range (4000):
        omeg.append(self.Omega[int(75*pi*j)])
        thet.append(self.Theta[int(75*pi*j)])
    title('Omega versus theta')
    xlabel('Theta/(radians)');ylabel('Theta/(radiands)')
    scatter(thet,omeg,color='k',s=1,label='FD=1.26')
    legend(loc='upper right',fontsize=9.0)
    show()
def plot_attractor(FD):
    pend=Pendulum_chaos()
    __init__(pend,FD)
    oscillation(pend)
    attractor(pend)

def fractal(F_D,Omega_D=2./3,theta_0=0.2,omega_0=0.0,Run_time=8000,Step=300*pi):
    P=Pendulum_chaos()
    __init__(P,FD=F_D,OmegaD=Omega_D,theta0=theta_0,omega0=omega_0,run_time=Run_time,step=Step)
    oscillation(P)
    Fd=[];the=[]
    for n in range(800,830):
        Fd.append(F_D)
        the.append(P.Theta[int(300*pi*n)])
    return(Fd,the)

def plot_fractal(rang):
    fd=[];th=[]
    FD=1.35
    for w in range(rang):
        FD=1.35+0.001*w
        lis=fractal(F_D=FD)
        fd.extend(lis[0])
        th.extend(lis[1])
    title('Theta versus FD')
    xlabel('FD/(s**(-2))');ylabel('Theta/(radiands)')
    scatter(fd,th,color='k',s=1,label='bifurcation diagram')
    show()        






















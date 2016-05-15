from math import*
from matplotlib.pyplot import*
from visual import*
class planet():
    '''erratic behavior of Saturn's moon:Hyperion'''
def __init__(self):
    self.x=[]
    self.y=[]
    self.vx=[]
    self.vy=[]

def running(run_t,mvy,theta0):
    Sat=sphere(pos=(0,0,0),radius=0.2,color=color.red)
    M1=sphere(pos=(1.1,0,0),radius=0.05,color=color.blue)
    M2=sphere(pos=(0.8,0,0),radius=0.05,color=color.blue)
    rod=curve(pos=[(0.8,0,0),(1.1,0,0)],color=color.green)
    GM=4*pi**2;dt=0.0001;l1=0.1;l2=0.2
    theta=[];theta.append(theta0)
    omega=[];omega.append(0)
    t=[];t.append(0)
    m=planet()
    __init__(m)
    m1=planet()
    __init__(m1)
    m2=planet()
    __init__(m2)
    m.x.append(1);m.y.append(0);m.vx.append(0);m.vy.append(mvy)
    m1x0=m.x[-1]+l1*cos(theta[-1]);m1y0=m.y[-1]+l1*sin(theta[-1])
    m1.x.append(m1x0);m1.y.append(m1y0)
    m2x0=m.x[-1]-l2*cos(theta[-1]);m2y0=m.y[-1]-l2*sin(theta[-1])
    m2.x.append(m2x0);m2.y.append(m2y0)
    for i in range(int(run_t/dt)):
        rate(2000)
        l=sqrt(m.x[-1]**2+m.y[-1]**2)
        mvx_med=m.vx[-1]-dt*GM*m.x[-1]/(l**3)
        m.vx.append(mvx_med)
        mvy_med=m.vy[-1]-dt*GM*m.y[-1]/(l**3)
        m.vy.append(mvy_med)
        mx_med=m.x[-1]+m.vx[-1]*dt
        m.x.append(mx_med)
        my_med=m.y[-1]+m.vy[-1]*dt
        m.y.append(my_med)
        omega_med=omega[-1]+-dt*3*GM*(m.x[-1]*sin(theta[-1])-m.y[-1]*cos(theta[-1]))*(m.x[-1]*cos(theta[-1])+m.y[-1]*sin(theta[-1]))/(l**5)
        omega.append(omega_med)
        theta_med=theta[-1]+omega[-1]*dt
        theta.append(theta_med)
        m1x0=m.x[-1]+l1*cos(theta[-1]);m1y0=m.y[-1]+l1*sin(theta[-1])
        m1.x.append(m1x0);m1.y.append(m1y0)
        m2x0=m.x[-1]-l2*cos(theta[-1]);m2y0=m.y[-1]-l2*sin(theta[-1])
        m2.x.append(m2x0);m2.y.append(m2y0)
        M1.pos.x=m1.x[-1];M1.pos.y=m1.y[-1]
        M2.pos.x=m2.x[-1];M2.pos.y=m2.y[-1]
        rod.pos=[(m2.x[-1],m2.y[-1],0),(m1.x[-1],m1.y[-1],0)]
        t.append(dt*(i+1))
        
    return (theta,omega,t)

def subplot_thw():
    theta=[];omega=[];t=[]
    lis=running(10,5,0)
    theta.extend(lis[0])
    omega.extend(lis[1])
    t.extend(lis[2])
    p1=subplot(211)
    p1.plot(t,theta,'k-',label='Elliptical orbit')
    p1.set_title('Hyperion     'r'$\theta\quad v.s.\quad time$''')
    p1.set_ylabel(r'$\theta\quad (radians)$')
    p1.legend(fontsize=7)
    p2=subplot(212)
    p2.plot(t,omega,'k-',label='Elliptical orbit')
    p2.set_title('Hyperion    'r'$\omega \quad v.s. \quad time$''')
    p2.set_xlabel('time(yr)');p2.set_ylabel(r'$\omega\quad (radians/yr)$')
    p2.legend(fontsize=7)
    show()
    

    
def plot_dis(mvy):
    delta=[]
    t=[]
    theta_0=[]
    theta_1=[]
    lis=running(10,mvy,0)
    liss=running(10,mvy,0.01)
    theta_0.extend(lis[0])
    theta_1.extend(liss[0])
    for i in range(len(theta_1)):
        delta.append(fabs(theta_0[i]-theta_1[i]))
        if delta[i]>6.2:
            if theta_0[i]>theta_1[i]:
                delta[i]=fabs(theta_1[i]+2*pi-theta_0[i])
            else:
                delta[i]=fabs(theta_0[i]+2*pi-theta_1[i])   
        t.append(0.0001*i)
    return (t,delta)
    
def subplot_dis():
    t=[];deltac=[];deltae=[]
    lis=plot_dis(2*pi)
    t.extend(lis[0])
    deltac.extend(lis[1])
    liss=plot_dis(5)
    deltae.extend(liss[1])
    p1=subplot(211)
    p1.plot(t,deltac,'k-',label='circular orbit')
    p1.set_title('Hyperion     'r'$\Delta\theta\quad v.s.\quad time$''')
    p1.set_ylabel(r'$\Delta\theta(radians)$')
    p1.legend(fontsize=9)
    p2=subplot(212)
    p2.semilogy(t,deltae,'k-',label='elliptical orbit')
    p2.set_title('Hyperion     'r'$\Delta\theta\quad v.s.\quad time$''')
    p2.set_ylabel(r'$\Delta\theta(radians)$')
    p2.set_xlabel('time(yr)')
    p2.legend(loc='lower right')
    show()

def noregu_dis():
    t=[];delta=[]
    lis=plot_dis(5)
    t.extend(lis[0])
    delta.extend(lis[1])
    semilogy(t,delta,'k-',label='initial velocity: 5 HU/yr')
    title('Hyperion     'r'$\Delta\theta\quad v.s.\quad time$''')
    xlabel('time(yr)')
    ylabel(r'$\Delta\theta(radians)$')
    legend(loc='lower right')
    text(1,4,'no restriction of 'r'$\theta$''',fontsize=20)
    show()

running(10,2*pi,0)












    



    














    
        

















        
        
        
    










































































    

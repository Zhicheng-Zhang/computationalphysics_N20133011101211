from math import*
from visual import*
class planet():
    '''describing the behavior of a planet spring'''
def __init__(self,step,GM,x0,y0,z0,vx0,vy0,vz0):
    self.GM=GM
    self.dt=step
    self.x=[x0]
    self.y=[y0]
    self.z=[z0]
    self.vx=[vx0]
    self.vy=[vy0]
    self.vz=[vz0]

def spring(run_t):
    S1=sphere(pos=(10,0,0),radius=2,color=color.red)
    S2=sphere(pos=(-10,0,0),radius=2,color=color.red)
    M=sphere(pos=(0,0,20),radius=1,color=color.green)
    star1=planet()
    __init__(star1,0.001,1000,10,0,0,0,5,0)
    star2=planet()
    __init__(star2,0.001,1000,-10,0,0,0,-5,0)
    moon=planet()
    __init__(moon,0.001,1000,0,0,10,0,0,0)
    for i in range(int(run_t/star1.dt)):
        rate(2000)
        l=sqrt((star2.x[-1]-star1.x[-1])**2+(star2.y[-1]-star1.y[-1])**2+(star2.z[-1]-star1.z[-1])**2)
        star1.vx_med=star1.vx[-1]+star1.dt*star1.GM*(star2.x[-1]-star1.x[-1])/(l**3)
        star1.vx.append(star1.vx_med)
        star1.vy_med=star1.vy[-1]+star1.dt*star1.GM*(star2.y[-1]-star1.y[-1])/(l**3)
        star1.vy.append(star1.vy_med)
        star1.vz_med=star1.vz[-1]+star1.dt*star1.GM*(star2.z[-1]-star1.z[-1])/(l**3)
        star1.vz.append(star1.vz_med)
        star2.vx_med=star2.vx[-1]+star2.dt*star2.GM*(star1.x[-1]-star2.x[-1])/(l**3)
        star2.vx.append(star2.vx_med)
        star2.vy_med=star2.vy[-1]+star2.dt*star2.GM*(star1.y[-1]-star2.y[-1])/(l**3)
        star2.vy.append(star2.vy_med)
        star2.vz_med=star2.vz[-1]+star2.dt*star2.GM*(star1.z[-1]-star2.z[-1])/(l**3)
        star2.vz.append(star2.vz_med)
        star1.x_med=star1.x[-1]+star1.dt*star1.vx[-1]
        star1.x.append(star1.x_med)
        star1.y_med=star1.y[-1]+star1.dt*star1.vy[-1]
        star1.y.append(star1.y_med)
        star1.z_med=star1.z[-1]+star1.dt*star1.vz[-1]
        star1.z.append(star1.z_med)
        star2.x_med=star2.x[-1]+star2.dt*star2.vx[-1]
        star2.x.append(star2.x_med)
        star2.y_med=star2.y[-1]+star2.dt*star2.vy[-1]
        star2.y.append(star2.y_med)
        star2.z_med=star2.z[-1]+star2.dt*star2.vz[-1]
        star2.z.append(star2.z_med)
        l1=sqrt((star1.x[-1]-moon.x[-1])**2+(star1.y[-1]-moon.y[-1])**2+(star1.z[-1]-moon.z[-1])**2)
        l2=sqrt((star2.x[-1]-moon.x[-1])**2+(star2.y[-1]-moon.y[-1])**2+(star2.z[-1]-moon.z[-1])**2)
        moon.vx_med=moon.vx[-1]+moon.dt*moon.GM*(star1.x[-1]-moon.x[-1])/(l1**3)+moon.dt*moon.GM*(star2.x[-1]-moon.x[-1])/(l2**3)
        moon.vx.append(moon.vx_med)
        moon.vy_med=moon.vy[-1]+moon.dt*moon.GM*(star1.y[-1]-moon.y[-1])/(l1**3)+moon.dt*moon.GM*(star2.y[-1]-moon.y[-1])/(l2**3)
        moon.vy.append(moon.vy_med)
        moon.vz_med=moon.vz[-1]+moon.dt*moon.GM*(star1.z[-1]-moon.z[-1])/(l1**3)+moon.dt*moon.GM*(star2.z[-1]-moon.z[-1])/(l2**3)
        moon.vz.append(moon.vz_med)
        moon.x_med=moon.x[-1]+moon.vx[-1]*moon.dt
        moon.x.append(moon.x_med)
        moon.y_med=moon.y[-1]+moon.vy[-1]*moon.dt
        moon.y.append(moon.y_med)
        moon.z_med=moon.z[-1]+moon.vz[-1]*moon.dt
        moon.z.append(moon.z_med)
        S1.pos=(star1.x[-1],star1.y[-1],star1.z[-1])
        S2.pos=(star2.x[-1],star2.y[-1],star2.z[-1])
        M.pos=(moon.x[-1],moon.y[-1],moon.z[-1])

spring(200)       
    
    
    

    



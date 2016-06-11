from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.
time=[]
for j in range(8000):
    time.append(j)
def calcu(T):
    Magnet=[]
    spins=[[1.0 for x in range(10)] for y in range(10)]
    for j in range(8000):
        E1=0.;M=0.0

        for i in range(9):
            for j in range(9):
                E1=E1+J*(-spins[i][j]*spins[i+1][j]-spins[i][j]*spins[i-1][j]-spins[i][j]*spins[i][j+1]-spins[i][j]*spins[i][j-1])
        for i in range(1,9):
            E1=E1+J*(-spins[i][0]*spins[i][1]-spins[i][0]*spins[i][9]-spins[i][0]*spins[i-1][0]-spins[i][0]*spins[i+1][0])
        for i in range(1,9):
            E1=E1+J*(-spins[0][i]*spins[1][i]-spins[0][i]*spins[9][i]-spins[0][i]*spins[0][i-1]-spins[0][i]*spins[0][i+1])
        E1=E1+J*(-spins[0][0]*spins[1][0]-spins[0][0]*spins[9][0]-spins[0][0]*spins[0][9]-spins[0][0]*spins[0][1])
        E1=E1+J*(-spins[9][0]*spins[9][1]-spins[9][0]*spins[9][9]-spins[9][0]*spins[8][0]-spins[9][0]*spins[1][0])
        E1=E1+J*(-spins[0][9]*spins[0][8]-spins[0][9]*spins[0][1]-spins[0][9]*spins[1][9]-spins[0][9]*spins[9][9])
        E1=E1+J*(-spins[9][9]*spins[9][8]-spins[9][9]*spins[9][1]-spins[9][9]*spins[8][9]-spins[9][9]*spins[1][9])
        E1=E1/2
        numb1=random.randint(0,9)
        numb2=random.randint(0,9)
        spins[numb1][numb2]=-spins[numb1][numb2]
        E2=0.
        for i in range(9):
            for j in range(9):
                E2=E2+J*(-spins[i][j]*spins[i+1][j]-spins[i][j]*spins[i-1][j]-spins[i][j]*spins[i][j+1]-spins[i][j]*spins[i][j-1])
        for i in range(1,9):
            E2=E2+J*(-spins[i][0]*spins[i][1]-spins[i][0]*spins[i][9]-spins[i][0]*spins[i-1][0]-spins[i][0]*spins[i+1][0])
        for i in range(1,9):
            E2=E2+J*(-spins[0][i]*spins[1][i]-spins[0][i]*spins[9][i]-spins[0][i]*spins[0][i-1]-spins[0][i]*spins[0][i+1])
        E2=E2+J*(-spins[0][0]*spins[1][0]-spins[0][0]*spins[9][0]-spins[0][0]*spins[0][9]-spins[0][0]*spins[0][1])
        E2=E2+J*(-spins[9][0]*spins[9][1]-spins[9][0]*spins[9][9]-spins[9][0]*spins[8][0]-spins[9][0]*spins[1][0])
        E2=E2+J*(-spins[0][9]*spins[0][8]-spins[0][9]*spins[0][1]-spins[0][9]*spins[1][9]-spins[0][9]*spins[9][9])
        E2=E2+J*(-spins[9][9]*spins[9][8]-spins[9][9]*spins[9][1]-spins[9][9]*spins[8][9]-spins[9][9]*spins[1][9])
        E2=E2/2
        delE=E2-E1
        if delE>0:
            p=exp(-delE/(k*T))
            numb3=random.uniform(0,1)
            if numb3>p:
                spins[numb1][numb2]=-spins[numb1][numb2]
        for i in range(10):
            for j in range(10):
                M+=spins[i][j]
        M=M/100       
        Magnet.append(M)
    return Magnet
        
M1=[];M2=[];M3=[];M4=[]
M1=calcu(1.0)
M2=calcu(2.0)
M3=calcu(3.0)
M4=calcu(4.0)
p1=subplot(211)
p1.plot(time,M1,'b',label='T=1.0')
p1.plot(time,M2,'r',label='T=2.0')
ylim(0,1.0)
ylabel('Magnetization')
title('Ising model  Magnetizaion vs. time')
legend(loc='lower right')
p2=subplot(212)
p2.plot(time,M3,'b',label='T=3.0')
p2.plot(time,M4,'r',label='T=4.0')
xlabel('time')
ylabel('Magnetization')
legend(loc='upper right')
ylim(-0.5,1.0)
x=np.linspace(0,8000)
y=x-x
plot(x,y,'k--')

show()



























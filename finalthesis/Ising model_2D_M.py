from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.

def calcu(T):
    spins=[[1 for x in range(10)] for y in range(10)]
        
    for j in range(2000):
        E1=0.
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
                E=E1
            else:
                E=E2
        else:
            E=E2
    M=0
    for i in range(10):
        for j in range(10):
            M+=spins[i][j]
    M=M
    return M
            
Tem=[];Magnet=[]

for j in range(1,20):
    T=0.25*j
    c=0.
    for i in range(100):
        c+=calcu(T)
    Mag_tmp=c/10000
    Magnet.append(Mag_tmp)
    Tem.append(T)
    print Tem[j-1],Magnet[j-1]


scatter(Tem,Magnet,color='k',label='10x10 lattice')
xlabel('T/(J/k)')
ylabel('Magnetization')
title('Ising model  Magnetizaion vs. Temperature')
legend(loc='upper right')
ylim(-0.2,1.0)
xlim(0,5)
x=np.linspace(0,5)
y=x-x
plot(x,y,'r--')
show()

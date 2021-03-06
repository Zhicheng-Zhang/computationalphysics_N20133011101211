from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.;energy=[];time=[]

def calcu(T):
    spins=[[1 for x in range(10)] for y in range(10)]
    E=0.;Es=0.  
    for j in range(4000):
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
                Etem=E1
            else:
                Etem=E2
        else:
            Etem=E2
            

    for j in range(4000,104000):
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
                Etem=E1
            else:
                Etem=E2
        else:
            Etem=E2
        E=E+Etem
        Es=Es+Etem**2
    dele=0.00001*Es-(0.00001*E)**2
    return dele

C=[];Tem=[]
for i in range(1,50):
    T=i
    ct=calcu(0.1*T)
    ctm=ct/((0.1*T)**2)
    ctmp=ctm/100
    C.append(ctmp)
    Tem.append(0.1*T)
    print Tem[i-1],C[i-1]


scatter(Tem,C,color='k',label='Fluctuation-dissipation method')
title('Ising model 2D ')
xlabel('T/(J/k)')
ylabel('Specific heat per spin')
ylim(0,1.5)
text(4,1.3,r'$Specific\quad heat$',color='b',fontsize=15)
text(3.6,1.2,r'$versus \quad Temperature$',color='b',fontsize=15)
legend()


show()












    

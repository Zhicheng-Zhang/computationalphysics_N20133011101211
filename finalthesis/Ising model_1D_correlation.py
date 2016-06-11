from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.;g=0
spins=[];R=[1,2,3,4,5,6,7,8,9];
def calcu(T):
    G=[]
    for i in range(100):
        spins.append(1.)
    for i in range(1,100,2):
        spins[i]=-spins[i]
        
    for j in range(4000):
        E1=0.
        for i in range(99):
            E1=E1+J*(-spins[i]*spins[i+1])
        E1=E1+J*(-spins[99]*spins[0])
        numb=random.randint(0,99)
        spins[numb]=-spins[numb]
        E2=0.
        for i in range(99):
            E2=E2+J*(-spins[i]*spins[i+1])
        E2=E2+J*(-spins[99]*spins[0])
        delE=E2-E1
        if delE>0:
            p=exp(-delE/(k*T))
            numb2=random.uniform(0,1)
            if numb2>p:
                spins[numb]=-spins[numb]
                
    
    for r in range(1,10):
        pro=0
        for i in range(100):
            if i+r>=100:
                pro+=spins[i]*spins[i+r-100]
                if i-r<0:
                    pro+=spins[i]*spins[i-r+100]
                else:
                    pro+=spins[i]*spins[i-r]
            else:
                pro+=spins[i]*spins[i+r]
                if i-r<0:
                    pro+=spins[i]*spins[i-r+100]
                else:
                    pro+=spins[i]*spins[i-r]
        pro=pro/200
        G.append(pro)
    return G

Gr=[];c=[];Grr=[];Grrr=[]
c=calcu(0.5)
for i in range(9):
    Gr.append(c[i])
c=calcu(1.)
for i in range(9):
    Grr.append(c[i])
c=calcu(1.5)
for i in range(9):
    Grrr.append(c[i])
for j in range(9):
    c=calcu(0.5)
    for i in range(9):
        Gr[i]=Gr[i]+c[i]
for j in range(9):
    c=calcu(1.)
    for i in range(9):
        Grr[i]=Grr[i]+c[i]
for j in range(9):
    c=calcu(1.5)
    for i in range(9):
        Grrr[i]=Grrr[i]+c[i]
for i in range(9):
    Gr[i]=Gr[i]/10
for i in range(9):
    Grr[i]=Grr[i]/10
for i in range(9):
    Grrr[i]=Grrr[i]/10

scatter(R,Gr,color='k')
plot(R,Gr,'r',label='T=0.5')
scatter(R,Grr,color='k')
plot(R,Grr,'b',label='T=1.0')
scatter(R,Grrr,color='k')
plot(R,Grrr,'g',label='T=1.5')
title('Ising model correlations')
xlabel('r')
ylabel('correlation function G(r)')
legend()
show()
    

            









            

    




















from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.
spins=[]
def calcu(T):
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
    E=0.
    for i in range(99):
        E=E+J*(-spins[i]*spins[i+1])
    E=E+J*(-spins[99]*spins[0])
    E=E/100
    return E

Tem=[];Energy=[]

for j in range(1,10):
    T=j
    c=0.
    for i in range(100):
        c+=calcu(T)
    E_tmp=c/100
    Energy.append(E_tmp)
    Tem.append(T)
    print Tem[j-1],Energy[j-1]

x=np.linspace(1,10,90)
y=-np.tanh(1/x)
plot(x,y,'r',label='analytical result')
scatter(Tem,Energy,color='k',label='numerical result')
title('Ising model 1D Energy-Temperature Relation')
xlabel('T/(J/k)')
ylabel('Energy per spin')
legend(loc='lower right')
show()























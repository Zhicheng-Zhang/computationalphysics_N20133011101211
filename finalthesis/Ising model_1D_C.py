from math import*
import random
import numpy as np
from matplotlib.pyplot import*

J=1.;k=1.
spins=[];Tem=[];C=[]
def calcu(T):
    for i in range(200):
        spins.append(1.)
        
    Es=0;E=0;Etem=0.
    for j in range(4000):
        E1=0.
        
        for i in range(199):
            E1=E1+J*(-spins[i]*spins[i+1])
        E1=E1+J*(-spins[199]*spins[0])
        
        numb=random.randint(0,199)
        spins[numb]=-spins[numb]
        E2=0.
        for i in range(199):
            E2=E2+J*(-spins[i]*spins[i+1])
        E2=E2+J*(-spins[199]*spins[0])
        delE=E2-E1
        if delE>0:
            p=exp(-delE/(k*T))
            numb2=random.uniform(0,1)
            if numb2>p:
                spins[numb]=-spins[numb]
                Etem=E1
            else:
                Etem=E2
        else:
            Etem=E2

    for j in range(2000,202000):
        E1=0.
        
        for i in range(199):
            E1=E1+J*(-spins[i]*spins[i+1])
        E1=E1+J*(-spins[199]*spins[0])
        
        numb=random.randint(0,199)
        spins[numb]=-spins[numb]
        E2=0.
        for i in range(199):
            E2=E2+J*(-spins[i]*spins[i+1])
        E2=E2+J*(-spins[199]*spins[0])
        delE=E2-E1
        if delE>0:
            p=exp(-delE/(k*T))
            numb2=random.uniform(0,1)
            if numb2>p:
                spins[numb]=-spins[numb]
                Etem=E1
            else:
                Etem=E2
        else:
            Etem=E2
        E+=Etem
        Es+=Etem**2
    delE=0.000005*Es-(0.000005*E)**2
    return delE

def getE():
    for j in range(1,41):
        T=0.1*j
        c=0.
        c=calcu(T)
        c=c/(T**2)
        c=0.005*c
        C.append(c)
        Tem.append(T)
        print Tem[j-1],C[j-1]
        

getE()
x=np.linspace(0.01,4,100)
y=1*(1/x)**2*(2/(np.exp(1/x)+np.exp(-1/x)))**2
plot(x,y,'r',label='analytical result')
scatter(Tem,C,color='k',label='numerical result')
title('Ising model 1D Specific Heat - Temperature Relation')
xlabel('T/(J/k)')
ylabel('Specific Heat per spin')
legend(loc='upper right')
show()




























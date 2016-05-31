from math import*
from matplotlib.pyplot import*


y1=[]
for i in range(1000):
    y1.append(0.1*exp(-(0.03*i-5)**2)) #this represents a Gaussian wave packet;you can change the form of initial wave packet as you like


y2=[]
for i in range(1000):
    y2.append(0.1*exp(-(0.03*i-5)**2))
    
y3=[]
for i in range(1000):
    y3.append(0.1*exp(-(0.03*i-5)**2))
    
x=[]
for i in range(1000):
    x.append(i)
X=[];Y=[]

def calcu(t):
    for i in range(t):
        for j in range(1,999):
            y3[j]=-y1[j]+y2[j+1]+y2[j-1]
        for k in range(1000):
            y1[k]=y2[k]
            y2[k]=y3[k]
    X.append(x);Y.append(y3)

calcu(260)
p1=subplot(511)
p1.plot(X[0],Y[0],'k')
p1.set_title('waves on a string (square wave)')
p1.set_ylabel('Amplitude')

calcu(265)
p2=subplot(512)
p2.plot(X[1],Y[1],'k')
p2.set_ylabel('Amplitude')

calcu(270)
p3=subplot(513)
p3.plot(X[2],Y[2],'k')
p3.set_ylabel('Amplitude')

calcu(275)
p4=subplot(514)
p4.plot(X[3],Y[3],'k')
p4.set_ylabel('Amplitude')

calcu(5)
p5=subplot(515)
p5.plot(X[4],Y[4],'k')
p5.set_xlabel('x')
p5.set_ylabel('Amplitude')
show()


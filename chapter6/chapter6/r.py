from math import*
from matplotlib.pyplot import*

r=1.2
y1=[]
for i in range(500):
    y1.append(0.01*i)
for i in range(500,1000):
    y1.append(10-0.01*i)

    


y2=[]
for i in range(500):
    y2.append(0.01*i)
for i in range(500,1000):
    y2.append(10-0.01*i)
    
y3=[]
for i in range(500):
    y3.append(0.01*i)
for i in range(500,1000):
    y3.append(10-0.01*i)
    
x=[]
for i in range(1000):
    x.append(i)
X=[];Y=[]

def calcu(t):
    for i in range(t):
        for j in range(1,999):
            y3[j]=2*(1-r**2)*y2[j]-y1[j]+(y2[j+1]+y2[j-1])*r**2
        for k in range(1000):
            y1[k]=y2[k]
            y2[k]=y3[k]
    X.append(x);Y.append(y3)

calcu(0)
p1=subplot(511)
p1.plot(X[0],Y[0],'k')
p1.set_title('waves on a string (triangular wavepacket r=0.8)')
p1.set_ylabel('Amplitude')

calcu(40)
p2=subplot(512)
p2.plot(X[1],Y[1],'k')
p2.set_ylabel('Amplitude')

calcu(100)
p3=subplot(513)
p3.plot(X[2],Y[2],'k')
p3.set_ylabel('Amplitude')

calcu(200)
p4=subplot(514)
p4.plot(X[3],Y[3],'k')
p4.set_ylabel('Amplitude')

calcu(300)
p5=subplot(515)
p5.plot(X[4],Y[4],'k')
p5.set_xlabel('x')
p5.set_ylabel('Amplitude')
show()

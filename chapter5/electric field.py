from numpy import*
from matplotlib import*
from pylab import*

store=zeros((7,7))
store[:7,:1]-=1
store[:7,6:7]+=1
store[0,1]=-0.67;store[0,2]=-0.33;store[0,4]=0.33;store[0,5]=0.67
store[6,1]=-0.67;store[6,2]=-0.33;store[6,4]=0.33;store[6,5]=0.67
med=zeros((7,7))
med[:7,:1]-=1
med[:7,6:7]+=1
med[0,1]=-0.67;med[0,2]=-0.33;med[0,4]=0.33;med[0,5]=0.67
med[6,1]=-0.67;med[6,2]=-0.33;med[6,4]=0.33;med[6,5]=0.67

def calcu():
    for i in range(1,6):
        for j in range(1,6):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(6):
        for j in range(6):
            store[i,j]=med[i,j]
    return store

def call(times):
    for i in range(times):
        calcu()

def getdata_x(n):
    call(n)
    efieldx=zeros((5,5))
    for i in range(1,6):
        for j in range(1,6):
            efieldx[i-1,j-1]=-(med[i,j+1]-med[i,j-1])/2
    return efieldx

def getdata_y(n):
    call(n)
    efieldy=zeros((5,5))
    for i in range(1,6):
        for j in range(1,6):
            efieldy[i-1,j-1]=-(med[i+1,j]-med[i-1,j])/2
    return efieldy

fig0,(ax1,ax2)=subplots(ncols=2)
efieldx=zeros((5,5));efieldy=zeros((5,5))

efieldx=getdata_x(2);efieldy=getdata_y(2)
def  f(x,y): return efieldx[x,y]
def  g(x,y): return efieldy[x,y]
x=arange(5);y=arange(5)
X,Y=meshgrid(x,y)
U=f(X,Y);V=g(X,Y)
one=ax1.streamplot(X-2,Y-2,U,V,color=U,cmap=cm.autumn)
ax1.set_title('Electrical Field  (after 2 calls)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

efieldx=getdata_x(20);efieldy=getdata_y(20)
def  h(x,y): return efieldx[x,y]
def  k(x,y): return efieldy[x,y]
x=arange(5);y=arange(5)
X,Y=meshgrid(x,y)
U=h(X,Y);V=k(X,Y)
two=ax2.streamplot(X-2,Y-2,U,V,color=U,cmap=cm.autumn)
fig0.colorbar(two.lines)
ax2.set_title('Electrical Field  (after 20 calls)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

show()









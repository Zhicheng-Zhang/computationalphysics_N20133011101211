from numpy import*
from matplotlib import*
from pylab import*

store=zeros((8,8))
store[3,4]=1;store[3,3]=1;store[4,3]=1;store[4,4]=1
med=zeros((8,8))
med[3,4]=1;med[4,3]=1;med[4,4]=1;med[3,3]=1


def calcu():
    for i in range(1,3):
        for j in range(1,7):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(3,7):
        for j in range(1,3):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(5,7):
        for j in range(3,7):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(3,5):
        for j in range(5,7):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(7):
        for j in range(7):
            store[i,j]=med[i,j]
    return store

def call(times):
    for i in range(times):
        calcu()
        
def plot_contour():
    def f(x,y): return med[y,x]
    x=arange(8)
    y=arange(8)
    X,Y=meshgrid(x,y)
    c=contourf(X-4,Y-4,f(X,Y))
    cbar=colorbar()
    show()

def getdata_x(n):
    call(n)
    efieldx=zeros((6,6))
    for i in range(1,3):
        for j in range(1,7):
            efieldx[i-1,j-1]=-(med[i,j+1]-med[i,j-1])/2
    for i in range(3,7):
        for j in range(1,3):
            efieldx[i-1,j-1]=-(med[i,j+1]-med[i,j-1])/2
    for i in range(5,7):
        for j in range(3,7):
            efieldx[i-1,j-1]=-(med[i,j+1]-med[i,j-1])/2
    for i in range(3,5):
        for j in range(5,7):
            efieldx[i-1,j-1]=-(med[i,j+1]-med[i,j-1])/2
    return efieldx

def getdata_y(n):
    call(n)
    efieldy=zeros((6,6))
    for i in range(1,3):
        for j in range(1,7):
            efieldy[i-1,j-1]=-(med[i+1,j]-med[i-1,j])/2
    for i in range(3,7):
        for j in range(1,3):
            efieldy[i-1,j-1]=-(med[i+1,j]-med[i-1,j])/2
    for i in range(5,7):
        for j in range(3,7):
            efieldy[i-1,j-1]=-(med[i+1,j]-med[i-1,j])/2
    for i in range(3,5):
        for j in range(5,7):
            efieldy[i-1,j-1]=-(med[i+1,j]-med[i-1,j])/2
    return efieldy

efieldx=zeros((6,6));efieldy=zeros((6,6))
efieldx=getdata_x(20);efieldy=getdata_y(20)
def  f(x,y): return efieldx[y,x]
def  g(x,y): return efieldy[y,x]
x=arange(6);y=arange(6)
X,Y=meshgrid(x,y)
U=f(X,Y);V=g(X,Y)


quiver(X-2.5,Y-2.5,U,V)

title('Electric field')
xlabel('x');ylabel('y')


show() 








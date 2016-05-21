from numpy import*
from matplotlib import*
from pylab import*
from mpl_toolkits.mplot3d import Axes3D
store=zeros((10,10))
store[3,4]=1;store[3,3]=1;store[4,3]=1;store[4,4]=1
med=zeros((10,10))
med[4,5]=1;med[4,4]=1;med[5,4]=1;med[5,5]=1


def calcu():
    for i in range(1,4):
        for j in range(1,9):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(4,9):
        for j in range(1,4):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(6,9):
        for j in range(4,9):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(4,6):
        for j in range(6,9):
            med[i,j]=(1.0/4)*(store[i-1,j]+store[i+1,j]+store[i,j+1]+store[i,j-1])
    for i in range(9):
        for j in range(9):
            store[i,j]=med[i,j]
    return store

def call(times):
    for i in range(times):
        calcu()

call(20)        

def f(x,y): return med[y,x]
fig=figure()
ax=Axes3D(fig)
x=arange(10)
y=arange(10)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='jet')
ax.set_title('3D Perspective Plot of Potential')
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('Potential(V)')
show()




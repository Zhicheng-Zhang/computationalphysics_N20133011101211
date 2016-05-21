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
    xlabel('x');ylabel('y')
    title('Equipotential Lines (after 20 calls)')
    cbar=colorbar()
    show()

call(20)
plot_contour()









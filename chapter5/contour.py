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
def plot_contour():
    def f(x,y): return med[y,x]
    x=arange(7)
    y=arange(7)
    X,Y=meshgrid(x,y)
    xlabel('x');ylabel('y')
    title('the Equipotential Lines (after 20 calls to update)')
    c=contourf(X-3,Y-3,f(X,Y))
    cbar=colorbar()
    
    show()

call(20)
print med
plot_contour()

import numpy 
from matplotlib import pyplot 
from matplotlib import animation


c1, c2 = 300, 150
det_x = 0.003
det_t= det_x / 300
x0, x1 = 0.3, 0.7
k = 1000
X = numpy.arange(0, 1, det_x)
Y1 = [numpy.exp(-k*(x-x0)**2) for x in X]

Y1[0], Y1[-1] = 0., 0.

pre_Y1, next_Y1 = [y for y in Y1], [y for y in Y1]

r1= c1 * det_t / det_x

fig = pyplot.figure(figsize=(9,6))
xmin, xmax =  0., 1.
ymin, ymax = -1., 1.
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
ax = pyplot.axes(xlim=(xmin-dx, xmax+dx), ylim=(ymin-dy, ymax+dy))
line, = ax.plot([], [],color='r',label='evolution of Gaussian packet')
pyplot.legend()

# legend
pyplot.xlabel(r'$x$', fontsize=16)
pyplot.ylabel(r'$y$', fontsize=16)
ax.set_title('the linear superposition of two wave packets')

# draw animation
def initAnimation():   
    line.set_data([], [])
    return line,

def animate(i):
    global X, Y1, pre_Y1, next_Y1
    for j in xrange(1, len(X)-1):
        next_Y1[j] = 2*(1-r1**2)*Y1[j] - pre_Y1[j] + r1**2*(Y1[j+1]+Y1[j-1])
    
    pre_Y1 = [y for y in Y1]
    Y1 = [y for y in next_Y1]
    tmp = [Y1[k] for k in xrange(len(X))]
    line.set_data(X, tmp)   
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=initAnimation, interval=20, blit=True)
pyplot.show()

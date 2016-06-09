#Upward Projectile with Air Resistance
##摘要
    本文求解了一个二阶常微分方程，得到了一个竖直上抛的小球在考虑空气阻力的情况下位移与时间的关系，
    并与无空气阻力情况下的位移与时间的关系做了对比。
##问题分析
###变量设置
　设置了变量x（位移，列表）、v（速度，列表）、t(时间，列表)、end_time（运动时间）、b（空气阻力系数）
　和dt（步长）、g（重力加速度）
###初值设置
　　x=0.0m,v=50m/s（大于零代表向上，小于零代表向下），end_time=9s,b=0.1/s,dt=0.01s,g=-10m/s^2
###算法
>- 本题利用如下算法描述二阶常微分方程：
　　　x_tmp=x[-1]+dt*v[-1]　　　　　v_tmp=v[-1]+dt*g-b*dt*v[-1]
>- 选择结构
　 因为空气阻力总是与速度反向，所以在小球从上升变为下落的时候，阻力也反向，程序中用选择结构实现：
　if v[-1]>=0:           v_tmp=v[-1]+dt*g-b*dt*v[-1]
　　else:　　　　　　　　v_tmp=v[-1]+dt*g+b*dt*v[-1]

##绘图
   用matplotlib绘图，并给出图例、坐标单位、注解等，并标出了有阻力情形下小球数值解达到的最大高度和
   无阻力情形下解析解达到的最大高度。
##程序源码
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1.2/projectile.py)

##程序运行结果
>- 图１.　无阻力情形下x-t曲线，数值解与解析解对比
![x-t曲线](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1.2/freeprojectile.png)
>- 图２.  有阻力情形下x-t曲线，与无阻力情形对比
![x-t曲线](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1.2/frictionalprojectile.png)

##结果分析
>- 不考虑空气阻力的情形下，从图１中可以看出数值解与解析解均呈现抛物线形状，这符合我们对二阶常微分方程的解的预想。在dt较大时有一定差距，且数值解略大于解析解。
>- 考虑空气阻力的情形下，从图２中可以看出x-t曲线已经偏离抛物线形状，而且到达的最大高度明显地比无阻力情形低，也符合预期。












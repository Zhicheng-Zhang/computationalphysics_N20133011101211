#Various Parameters of A Cannon Shell's Trajectory
### 张志城 2013301110121
##摘要
本文从简单到复杂，分别研究了无空气阻力、有不随海拔变化空气阻力和随海拔变化空气阻力情况下的使射程最远的出射角和出射角一定时打击定点目标所需的最小发射速度。
##问题分析
###思路
采取由简单到复杂逐步深入的策略。
先用Euler法利用循环结构实现画出无空气阻力情况下炮弹轨迹，再加入空气阻力，最后使空气阻力随海拔增加而逐渐减小，分别画出炮弹轨迹。
在此基础之上，利用双重循环，扫描0-90度范围内的发射角，可获得给定发射速度下使射程最大的发射角。
为了实现在一定精度范围内打击给定目标，先固定发射角，然后扫描合适的速度范围，找到满足精度要求的最小发射速度。
###具体问题及解决方案
####为了使炮弹最终落点纵坐标为0，亦即落到地面上，而不是根据循环条件使得最终落点稍小于0，进行如下处理
a=-y[-1]/y[-2]
x.append((x[-1]+a*x[-2])/(1+a))
y.append(0)
####用未作处理前最后两点连成的直线与x轴相交，求得交点，作为最后落点。

####为了找出使射程最大的出射角，利用嵌套循环，将每个出射角与射程分别放到两个列表中，再利用matplotlib绘出射程-出射角关系曲线，可以很直观地看出最大射程对应的出射角。
##程序源码
###无阻力情形下射程-出射角关系
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon-theta-F.py)

###渐变阻力下射程-出射角关系
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_theta_ARV.py)

###无阻力情形下定点打击最小速度
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_aiming_F.py)

###渐变阻力下定点打击最小速度
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_aimming_ARV.py)
##运行结果
###无阻力情形下不同发射角对应轨迹
![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_theta_F_discrete.png)
###无阻力情形下射程-出射角关系曲线
![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_theta_F.png)
###渐变阻力下射程-出射角关系曲线
![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/figure_theta_ARV.png)
###无阻力下定点打击最小速度
![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon_aiming_F.png)
###渐变阻力下定点打击最小速度
![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2/cannon-aiming-ARV.png)

##结果分析
> 根据程序运行得到的出射角-射程关系曲线可知，无阻力情形下最佳发射角为45°，而在接近真实环境的渐变阻力下最佳发射角大于45°。
> 文中的程序实现了在固定发射角的条件下寻找打击定点的最小速度，精度分别达到0.15米和0.10米，精准度较好。但由于没有让发射角也变化发射速度并非最小，存在一定缺陷。

##致谢
> 感谢蔡浩老师课上的讲解和与曹一、李浩波等同学的交流讨论，这些帮助我完成了本文。


本次作业我选了第３题,另外又写了一下第５题的程序

#第３题　Falling with Friction#
##摘要##
  本文利用题中所给的微分方程编程描述了考虑空气阻力情况下一个小球从高处落下，其速度随时间变化的关系。并分析了步长对解析解与数值解之间差距的影响。
##问题分析##
###参数设置###
>- 变量设置:　设置了t（运动时间）、v（运动速度），以数组形式呈现。若只是设置为单纯的变量则在'print'的时候只能得到一个点，而不是一条曲线。
>- 常量设置:　设置了a=10（重力加速度）、b=1（摩擦力系数）、dt(步长，可以调整，以观察它对数值解近似程度的影响)、end_time(运行时间）。

###算法
>- tmp=v[-1]+dt*(a-b*v[-1])　　　　v.append(tmp)　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
>- 利用初值可算得dt之后的ｖ值v（dt），再利用v（dt）可算得2dt之后的v值，如此迭代下去，可算得end_time之后的v值。而且可以预计，随着dt的减小，数值解会越来越接近解析解。


###绘图
>- 本作业用matplotlib绘制数值解的v-t关系，设置了图像的标题，给曲线命名，设置坐标轴的名称和单位。
>- def f(x): return (1-np.exp(-x))*10                                                                                         
算出了题给问题的解析解，并定义函数，画出解析解的图像与数值解对比。

##程序代码
![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1/frictionalfall.py)
##程序运行结果
>- ![dt=0.5得到的v-t曲线](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1/figure_1.png)
>- ![dt=0.1得到的v-t曲线](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1/figure_1.1.png)

##结果分析
>- 可以看到曲线显示，随着时间增大，物体的速度逐渐增大，但增加得越来越慢，最后趋于一定值。
>- dt=0.1和dt=0.5得到的曲线之间的差异则表明，步长选取越小，数值解越接近解析解。

##致谢
>- 感谢蔡浩老师上课时讲的解微分方程的代码，感谢刘文焘同学的报告版式，为我提供了很好的参考。

第５题　　Radioactive Nucleus
=================================
>- ![代码链接](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1/ABdecay.py)
>- 运行结果　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
![运行结果](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter1/figure_1.2.png)







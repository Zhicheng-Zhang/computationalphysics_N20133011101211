#  Trajectory of A Baseball with Backspin & 3-D Display
###张志城 2013301110121
##  Abstracts
>- Making use of Euler method this passage researches the shoot range of a baseball at different angular velocities and then display the trajectory of the baseball in Vpython environment.

##  Principles
>- Considering gravity,air resistance and the effect of backspin(Magnus force),we have following formulas:
       <br />    ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3Dv_%7Bx%7D)
       <br />    ![] (http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7Bx%7D%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7D)
       <br />    ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%7By%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7By%7D)
       <br />    ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7By%7D%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3D-g)
       <br />    ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%7Bz%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7Bz%7D)
       <br />    ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7Bz%7D%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3D-%5Cfrac%7BS_%7B0%7D%7D%7Bm%7D%5Comega%20v_%7Bx%7D)
    
  >- I use Euler method to describe formulas above iterating the process again and again,and initialize x,y,z,v_x,v_y,v_z as lists so that I can draw the y-x curve with matplotlib.
  >- As for its 3-D display,I draw a baseball,two vertical walls and a playground with Vpython.Besides,I add materials to walls and the playground,and draw the trail of the baseball.

##Source Codes
###   ![The Effect of Backspin on the Trajectory of A Baseball] (https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_Magnus.py)
###   ![The 3-D Display of A Spining Baseball]  (https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_Magnus_AR.py)
  
  
##Results
###The Comparison of the Trajectory of A Baseball with Different Angular Velocity
>- y-x Relation with No Spin
   ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_backspin_0.png)
>- y-x Relation with 1000 rmp Spin
   ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_backspin_1000.png)
>- y-x Relation with 2000 rmp Spin
   ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_backspin_2000.png)
###Screenshots of the 3-D Display of A Spining Baseball
>- Front View
  ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_Magnus_frontview.png)
>- Top View
  ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter2.2/baseball_Magnus_topview.png)
  
## Analysis
>- We can find that with the increase of angular speed the shoot range increases correspondingly.This is because the backspin provides the baseball with upward force,so the baseball can travel for a longer period.
>- If the angular speed is upward,things are different.As is shown in the screenshots of the display,the baseball move both in y and z directions,which are seperately because of the Magnus force and gravity.

## Acknowledgement
>- Thanks for Mr. Cai's direction for using Vpython.
  

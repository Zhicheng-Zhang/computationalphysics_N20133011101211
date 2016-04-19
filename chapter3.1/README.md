# Problem 3.4  The Dependence of Period of Oscillation on Amplitudes
### 张志城 2013301110121
## Abstracts
>-  This passage researches the effect of power index in this second-order differential equation </br> 　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%5E%7B2%7D%7D%3D-kx%5E%7B%5Calpha%20%7D) </br> on the relatin between amplitudes and periods of oscillations.Basically,when the power index is great than 1, the periods of an oscillation will decrease with the increase of amplitudes,which is different from the situation when the power index is 1 in which the period is independent of amplitudes.

##Backgroud
>- It is known to us all that the equation of a harmonic oscillation is</br> 　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7Dx%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E%7B2%7D%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dx)</br>And the solution of the equation is</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?x%3Dx_%7B0%7Dsin%28%5COmega%20t&plus;%5Cvarphi%20%29)</br>
In which the frequency is</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7B%5Cfrac%7Bg%7D%7Bl%7D%7D)</br>Correspondingly,the period is</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?T%3D2%5Cpi%5Csqrt%7B%5Cfrac%7Bl%7D%7Bg%7D%7D)</br>which is independent of the amplitude,say,![](http://latex.codecogs.com/gif.latex?x_%7B0%7D).</br>
>- However,for following equation</br> 　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%5E%7B2%7D%7D%3D-kx%5E%7B%5Calpha%20%7D)  　　![](http://latex.codecogs.com/gif.latex?%5Calpha%3E1) </br>
things are different.The periods of the oscillation are dependent of amplitudes.And I'm trying to research this dependency.

## Three Algorithms to Solving the Equation
>- The basic idea of Euler method is </br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28%5Cfrac%7Bg%7D%7Bl%7D%29%5Ctheta_%7Bi%7D%5CDelta%20t)</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)</br>
 >- The Main Idea of Euler-Cromer Method is </br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28%5Cfrac%7Bg%7D%7Bl%7D%29%5Ctheta_%7Bi%7D%5CDelta%20t)</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega_%7Bi%7D%5CDelta%20t)</br>
 >- The Main Idea of Runge-Kutta Method is </br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Ctheta%5E%7B%27%7D%3D%5Ctheta_%7Bi%7D&plus;%5Cfrac%201%202%20%5Comega_%7Bi%7D%5CDelta%20t)</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Comega%5E%7B%27%7D%3D%5Comega_%7Bi%7D-%5Cfrac%201%202%20%5Cfrac%20g%20l%20%5Ctheta_%7Bi%7D%5CDelta%20t)</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega%7B%7D%5E%7B%27%7D%5CDelta%20t)</br>
　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%5Cfrac%20g%20l%20%5Ctheta%5E%7B%27%7D%5CDelta%20t)</br>

##Results
### The Comparison of Three Algorithms Solving Harmonic Oscillation</br>
　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/Algorithms.png)</br>
 >- We can find form the figure that Euler method can't solve the problem well,the amplitude gets larger and larger with time increasing.However,Euler-Cromer method and Runge-Kutta method describe the harmonic well:</br>
       The angle varies periodically with time;and the amplitude,so does energy,remains unchanged as time increases.

### The Behavior of Anharmonic Oscillations
　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/Period-Amplitude.png)
>- In this figure the anharmonic oscillation presents an obvious characteristic:
       As the amplitude increases,the period of the oscillation decreases accordingly.
>- Refering Yangyao Chen(陈洋遥)'s homework,we can get the analytical formula of period-amplitude relation of this anharmonic oscillation is:</br>
　　　![](http://latex.codecogs.com/gif.latex?%5Ctau%3DK%28%5Calpha%29%5Csqrt%20%5Cfrac%20%7B2%28%5Calpha&plus;1%29%7D%20k%20%5Ctheta_%7B0%7D%5E%7B%5Cfrac%20%7B1-%5Calpha%7D%202%20%7D)</br>
So when the power index![](http://latex.codecogs.com/gif.latex?%5Calpha)>1,the period decreases as amplitude increases.


## The Celestial Body's Motion & Chaotic
### Two-body Motion
>- The motion of two planet whose mass are the same with different initial velocity is presented in the following figure:</br>
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/two-body_def.png)</br>
Using 2nd-order Runge-Kutta method to solve the Newtonian equations:</br>
              ![](http://latex.codecogs.com/gif.latex?F%3D%5Cfrac%20%7BGM_%7B1%7DM_%7B2%7D%7D%7Br%5E%7B2%7D%7D)</br>
We can find that they move in this way:</br>
              ![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/two-body.gif)</br>
>- The motion of Sun and Earth can be expressed equivalently in the following figure:</br>
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/Sun-Earth.png)</br>
We can simulate their motion in Vpython:
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/Sun-Earth.gif)</br>

### Three-body Motion
>- The motion of three stars and a planet at the center of the stars can be presented in the following figure:</br>
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/three-body_constant.png)</br>The regular running of these bodies can be simulated well in Vpython:</br>
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/three-body_constant.gif)
　　　　　　　![](https://github.com/Zhicheng-Zhang/computationalphysics_N20133011101211/blob/master/chapter3.1/three-body_disorder.gif)

  

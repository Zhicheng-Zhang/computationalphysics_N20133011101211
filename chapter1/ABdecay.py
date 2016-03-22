import matplotlib.pyplot as plt

N_A=[];N_B=[];t=[]
N_A.append(100.0);N_B.append(0.0);t.append(0.0)
tau=1;dt=0.01;end_time=5.0
for i in range(int(end_time/dt)):
    Med1=N_A[-1]+(N_B[-1]-N_A[-1])/tau*dt
    Med2=N_B[-1]+(N_A[-1]-N_B[-1])/tau*dt
    N_A.append(Med1);N_B.append(Med2)
    t.append(dt*(i+1))
    print ('t=%s,N_A=%s,N_B=%s'%(t[-1],N_A[-1],N_B[-1]))


line1,=plt.plot(t,N_A,'r--')
line2,=plt.plot(t,N_B,'b--')
plt.xlabel('Time/(s)')
plt.ylabel('Number of Nuclei')
plt.legend((line1,line2),('Number of Nuclei A','Number of Nuclei B'))
plt.title('The Time-dependence of Numbers of Two Related Radioactive Nuclei')
plt.show()





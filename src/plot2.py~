# Plot n VS error y plot n VS tiempo
from math import *
import matplotlib.pyplot as plt

if __name__=='__main__':
  num=[]
  err=[]
  tiempo=[]

  fichero=open('resultado2.txt','r')
  
  for i in range(800):
    num.append(fichero.readline().strip('\n'))
    err.append(fichero.readline().strip('\n'))
    tiempo.append(fichero.readline().strip('\n'))
    
  num=[float(i) for i in n]
  tiempo=[float(i) for i in time]
  
  print num
  print tiempo
  
  diagrama3=plt.figure(3)
    
  plt.plot(num,tiempo)
    
  plt.title('Numero de subintervalos Vs tiempo')
  plt.xlabel('Numero de subintervalos')
  plt.ylabel('tiempo (s)')
  
  plt.xlim(0.0, 500.0)
    
  plt.savefig("Plot_nVStime.eps")
  
  fichero.close()

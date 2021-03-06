# Plot n VS error y plot n VS tiempo
from math import *
import matplotlib.pyplot as plt

def cotaError(n):
  return (pi**2)/(12*(n**2))
  
if __name__=='__main__':
  n=[]
  error=[]
  time=[]
  cota=[]
  
  num=[]
  err=[]
  tiempo=[]
    
  fichero=open('resultado.txt', 'r')
  for i in range(9):
    n.append(fichero.readline().strip('\n'))
    error.append(fichero.readline().strip('\n'))
    time.append(fichero.readline().strip('\n'))
  
  n=[float(i) for i in n]
  error=[float(i) for i in error]
  time=[float(i) for i in time]
  
  for i in n:
    cota.append(cotaError(i))
    
  diagrama1=plt.figure(1)
    
  plot1,=plt.plot(n,error,'r')
  plot2,=plt.plot(n,cota, 'b')
    
  plt.title('Numero de subintervalos Vs error')
  plt.xlabel('Numero de subintervalos')
  plt.ylabel('Error')
  
  #plt.legend()
  plt.legend([plot1,plot2],['Error absoluto','Cota del error']) # cota calculada analiticamente

  plt.xlim(0.0, 100)
  plt.ylim(-0.01, 0.7)
    
  plt.savefig("Plot_nVSerrorAndcota.eps")
  
  diagrama2=plt.figure(2)

  plt.plot(n,error, 'r')

  plt.title('Numero de subintervalos Vs error')
  plt.xlabel('Numero de subintervalos')
  plt.ylabel('Error')

  plt.xlim(0.0, 100)
  plt.ylim(-0.01, 0.7)
  
  plt.savefig("Plot_nVSerror.eps")

  fichero.close()
  
  fichero=open('resultado2.txt','r')
  
  for i in range(250):
    num.append(fichero.readline().strip('\n'))
    err.append(fichero.readline().strip('\n'))
    tiempo.append(fichero.readline().strip('\n'))
    
  num=[float(i) for i in num]
  tiempo=[float(i) for i in tiempo]
  
  diagrama3=plt.figure(3)
    
  plt.plot(num,tiempo)
    
  plt.title('Numero de subintervalos Vs tiempo')
  plt.xlabel('Numero de subintervalos')
  plt.ylabel('tiempo (s)')
  
  plt.xlim(0.0, 500.0)
    
  plt.savefig("Plot_nVStime.eps")


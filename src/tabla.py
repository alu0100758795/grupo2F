import numpy

a=[]
fichero=open('resultado.txt','r')
for i in range(57):
  a.append(fichero.readline().strip('\n'))
  
a=[float(i) for i in a]

numpy.savetxt("mydata.csv", a, delimiter=',', fmt='%2.10f')

fichero.close()
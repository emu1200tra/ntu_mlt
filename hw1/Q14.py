# need to be conti.

from sklearn import svm
from sklearn.svm import SVC  
import numpy as np
import math
from matplotlib import pyplot as plt

filename = 'training.txt'

def readin_data():
  data = []
  datay = []
  with open(filename) as file:
    lines = [line.split() for line in file]
    for i in lines:
      data.append([float(i[1]) , float(i[2])])
      datay.append(float(i[0]))

  return data , datay

def picking_data(data , need_value):
  label = []
  for i in data:
    if i != need_value:
      label.append(-1)
    else:
      label.append(1)
  return label

def kernel(xn , xm):
  vector = xn - xm
  return math.exp(-80*(vector[0]**2 + vector[1]**2))


data , datay = readin_data()
label = picking_data(datay , 0)
C_value = [-3 , -2 , -1 , 0 , 1]
distance = []
SVs = []
for i in C_value:
  clf = svm.SVC(kernel='rbf' , gamma=80 , C=10**i)
  clf.fit(data, label)  

  SVs = clf.support_vectors_
  coef = clf.dual_coef_
  counter = 0
  for j in range(len(coef[0])):
    for k in range(len(coef[0])):
      counter += clf.dual_coef_[0][j]*clf.dual_coef_[0][k]*kernel(clf.support_vectors_[j] , clf.support_vectors_[k])
    
  print counter
  distance.append(1.0/math.sqrt(counter))

  

  print 'C:' , i

  print 'SVs: ' , SVs

  print 'y*alpha: ' , clf.dual_coef_


plt.scatter(distance , C_value)
plt.xlabel('distance')
plt.ylabel('C')
plt.show()



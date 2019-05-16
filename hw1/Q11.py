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

def my_kernel(X, Y):
  return np.dot(X, Y.transpose())

def picking_data(data , need_value):
  label = []
  for i in data:
    if i != need_value:
      label.append(-1)
    else:
      label.append(1)
  return label


data , datay = readin_data()
label = picking_data(datay , 0)
C_value = [-5 , -3 , -1 , 1 , 3]
W = []
SVs = []
for i in C_value:
  clf = svm.SVC(kernel='linear' , C=10**i)
  clf.fit(data, label)  

  counter = [0 , 0]
  SVs = clf.support_vectors_

  for j in range(len(SVs)):
#    print clf.dual_coef_[0][j] , clf.support_vectors_[j]
    counter += clf.dual_coef_[0][j] * clf.support_vectors_[j]
  W.append(math.sqrt(counter[0]**2 + counter[1]**2))

  print 'C:' , i

  print 'SVs: ' , SVs

  print 'y*alpha: ' , clf.dual_coef_

  print 'W: ' , W[-1]



plt.scatter(W , C_value)
plt.xlabel('||W||')
plt.ylabel('C')
plt.show()



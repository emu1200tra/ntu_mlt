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
label = picking_data(datay , 8)
C_value = [-5 , -3 , -1 , 1 , 3]
Ein = []
SVs = []
for i in C_value:
  clf = svm.SVC(kernel='poly' , degree=2 , coef0=1 , gamma=1 , C=10**i)
  clf.fit(data, label)  

  SVs = clf.support_vectors_
  tmpEin = 0.0
  for j in range(len(data)):
    predict_result = clf.predict([data[j]])
    if predict_result != label[j]:
      tmpEin+=1

  Ein.append(tmpEin/len(data))

  print 'C:' , i , 'Ein:' , Ein[-1]

plt.scatter(Ein , C_value)
plt.xlabel('Ein')
plt.ylabel('C')
plt.show()

'''
  print 'SVs: ' , SVs

  print 'y*alpha: ' , clf.dual_coef_

  print 'b: ' , clf.intercept_
'''
#  print 'weight: ' , counter

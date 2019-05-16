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


data , datay = readin_data()
filename = 'testing.txt'
test_data , test_datay = readin_data()
label = picking_data(datay , 0)
test_label = picking_data(test_datay , 0)
C_value = -1
gamma = [0 , 1 , 2 , 3 , 4]
SVs = []
Eout = []
for i in gamma:
  clf = svm.SVC(kernel='rbf' , gamma=10**i , C=10**C_value)
  clf.fit(data, label)  

  SVs = clf.support_vectors_
  tmpEout = 0.0
  for j in range(len(test_data)):
    predict_result = clf.predict([test_data[j]])
    if predict_result != test_label[j]:
      tmpEout+=1

  Eout.append(tmpEout/len(test_data))

  print 'gamma:' , i , 'Eout:' , Eout[-1]
  

plt.scatter(Eout , gamma)
plt.xlabel('Eout')
plt.ylabel('gamma')
plt.show()



from sklearn import svm
from sklearn.svm import SVC  
import numpy as np
import math
from matplotlib import pyplot as plt
from random import shuffle

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

def valid_data(data , datay , number):
  dataset = []
  new_data = []
  new_datay = []
  valid_dataset = []
  valid_datay = []
  for i in range(len(data)):
    dataset.append([data[i] , datay[i]])
  shuffle(dataset)
  for i in range(len(dataset)):
    if i < number:
      valid_dataset.append(dataset[i][0])
      valid_datay.append(dataset[i][1])
    else:
      new_data.append(dataset[i][0])
      new_datay.append(dataset[i][1])
  return new_data , new_datay , valid_dataset , valid_datay


data , datay = readin_data()
label = picking_data(datay , 0)
C_value = -1
gamma = [-1 , 0 , 1 , 2 , 3]
record = [0 , 0 , 0 , 0 , 0]
SVs = []
for index in range(100):
  new_data , new_datay , valid_dataset , valid_datay = valid_data(data , label , 1000)
  minium = 1.0
  best_gamma = 0
  for i in gamma:
    clf = svm.SVC(kernel='rbf' , gamma=10**i , C=10**C_value)
    clf.fit(new_data, new_datay)  

    SVs = clf.support_vectors_
    
    tmpEval = 0.0
    for j in range(len(valid_dataset)):
      predict_result = clf.predict([valid_dataset[j]])
      if predict_result != valid_datay[j]:
        tmpEval+=1

    if minium > tmpEval/len(valid_dataset):
      minium = tmpEval/len(valid_dataset)
      best_gamma = i
  record[best_gamma+1]+=1
  print record

plt.bar(gamma , record)
plt.xticks(gamma)
plt.xlabel('gamma')
plt.ylabel('times')
plt.show()



from sklearn import svm
from sklearn.svm import SVR
import numpy as np
import math
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")

filename = 'hw2_lssvm_all.dat'

def readin_data():
  data = []
  datax = []
  datay = []
  test_data = []
  test_datax = []
  test_datay = []
  with open(filename) as file:
    lines = [line.split() for line in file]
    for i in range(len(lines)):
      record = []
      record.append(1.0)
      if i < 400:
        for j in range(len(lines[i])):
          if j < 10:
            record.append(float(lines[i][j]))
          else:
            datay.append(float(lines[i][j]))
        datax.append(record)
        data.append((datax[-1] , datay[-1]))        
      else:
        for j in range(len(lines[i])):
          if j < 10:
            record.append(float(lines[i][j]))
          else:
            test_datay.append(float(lines[i][j]))
        test_datax.append(record)
        test_data.append((test_datax[-1] , test_datay[-1]))

  return data , datax , datay , test_data , test_datax , test_datay

def num_sign(a):
  if a > 0:
    return 1
  else:
    return 0

lamda = [0.01 , 0.1 , 1.0 , 10.0 , 100.0]
# C = 1/2lamda
data , datax , datay , test_data , test_datax , test_datay = readin_data()
Ein = 21473644
record = 0
record_Ein = np.zeros(len(datay))

for j in lamda:

  for k in range(250):
    index = [np.random.randint(0 , 399) for i in range(400)]
    train_datax = []
    train_datay = []
    for i in range(len(index)):
      train_datax.append(datax[index[i]])
      train_datay.append(datay[index[i]])

    I = np.identity(11)
    #print I.shape
    matrix2 = np.dot(np.transpose(train_datax) , train_datax)
    #print matrix2.shape
    inv_matrix = np.linalg.inv(j*I + matrix2)
    #print inv_matrix.shape
    matrix3 = np.dot(inv_matrix , np.transpose(train_datax))
    #print matrix3.shape
    W = np.dot(matrix3 , np.transpose(train_datay)) #11*1
    for i in range(len(datay)):
      predict_result = np.dot(datax[i] , W)
      record_Ein[i] += predict_result
  for i in range(len(record_Ein)):
    if(record_Ein[i] < 0):
      record_Ein[i] = -1
    else:
      record_Ein[i] = 1

  tmp = 0
  for i in range(len(datay)):
    if(num_sign(record_Ein[i]) != num_sign(datay[i])):
       tmp += 1
  if Ein >= tmp:
    Ein = tmp
    record = j
  print "Ein:" , tmp / 400.0 ,  "lamda:" , j

print "min_Ein:" , Ein / 400.0 , "lamda:" , record

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
tmp = 0


for j in lamda:
  tmp = 0.0
  I = np.identity(11)
  #print I.shape
  matrix2 = np.dot(np.transpose(datax) , datax)
  #print matrix2.shape
  inv_matrix = np.linalg.inv(j*I + matrix2)
  #print inv_matrix.shape
  matrix3 = np.dot(inv_matrix , np.transpose(datax))
  #print matrix3.shape
  W = np.dot(matrix3 , np.transpose(datay)) #11*1
  # W = BZn
  for k in range(len(datay)):
    predict_result = np.dot(datax[k] , W)
    if(num_sign(predict_result) != num_sign(datay[k])):
       tmp += 1
  if Ein >= tmp:
    Ein = tmp
    record = j
  print "Ein:" , tmp / 400.0 ,  "lamda:" , j

print "min_Ein:" , Ein / 400.0 , "lamda:" , record

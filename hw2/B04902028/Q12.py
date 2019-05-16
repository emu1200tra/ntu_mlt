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
          if j < 10:from sklearn import svm
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
  if a >= 0:
    return 1
  else:
    return 0

def L2(x):
  sum_i = 0.0;
  for i in x:
    sum_i += i**2
    #print sum_i
  return sum_i

def kernel(x1 , x2 , gamma):
  record = []
  for i in range(len(x1)):
    record.append(x1[i]-x2[i])
    #print "gamma:" , gamma

  return math.exp(-(gamma*(L2(record))))

def K(data , gamma):
  matrix = [[0.0 for i in range(len(data))] for j in range(len(data))]
  for i in range(len(data)):
    for j in range(len(data)):
      matrix[i][j] = kernel(data[i] , data[j] , gamma)
  return (matrix)


gamma = [32.0 , 2.0 , 0.125]
lamda = [0.001 , 1.0 , 1000]
# C = 1/2lamda
data , datax , datay , test_data , test_datax , test_datay = readin_data()
Eout = 21473644
record = [0 , 0]
tmp = 0

for i in gamma:
  for j in lamda:
    tmp = 0.0
    I = np.identity(len(datay))
    beta = np.dot(np.linalg.inv(j*I + K(datax , i)) , datay)
    # W = BZn
    for k in range(len(test_datay)):
      predict_result = 0
      for l in range(len(datay)):
        predict_result += ((beta[l]) *(kernel(test_datax[k] , datax[l] , i)))
      if(num_sign(predict_result) != num_sign(test_datay[k])):
         tmp += 1
    if Eout >= tmp:
      Eout = tmp
      record[0] = i
      record[1] = j
    print "Eout:" , tmp / float(len(test_datay)), "gamma:" , i , "lamda:" , j

print "min_Eout:" , Eout / float(len(test_datay)) , "gamma:" , record[0] , "lamda:" , record[1]






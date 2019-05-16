import math
from matplotlib import pyplot as plt
import time

train_filename = 'hw3_train.dat'
test_filename = 'hw3_test.dat'

def readin_data(filename):
  data = []
  datax = []
  datay = []
  with open(filename) as file:
    lines = [line.split() for line in file]
    for i in range(len(lines)):
      data.append([float(j) for j in lines[i]])
      datax.append([float(j) for j in lines[i][0:-1]])
      datay.append(int(lines[i][-1]))
  return data , datax , datay

def sort_cmp_0(data):
  return data[0]

def sort_cmp_1(data):
  return data[1]

def split_data(data):
  datax = []
  datay = []
  U = []
  for i in range(len(data)):
    datax.append(data[i][0:-2])
    datay.append(data[i][-2])
    U.append(data[i][-1])
  return datax , datay , U

def count_theta(datax , index):
  theta = [-21473647.0]
  for i in range((len(datax)-1)):
    theta.append((datax[i][index] + datax[i+1][index])/2.0)
  return theta

def sign_my(value):
  if value < 0:
    return -1
  else:
    return 1

def hypothesis(s , i , theta , x):
  return s*sign_my(x - theta)

def error_cmp(error):
  return error[0]

def DSA(data , U):
  i = [0 , 1]
  s = [-1 , 1]
  record = []
  tmp_data = []
  for j in range(len(data)):
    tmp_data.append((data[j][0] , data[j][1] , data[j][2] , U[j]))
  for index in i:
    if(index == 0):
      tmp_data.sort(key=sort_cmp_0)
    else:
      tmp_data.sort(key=sort_cmp_1)

    datax , datay , U = split_data(tmp_data)
    theta = count_theta(datax , index)
    for j in theta:
      for k in s:
        error = 0.0
        for l in range(len(datax)):
          if(int(datay[l]) != hypothesis(k , index , j , datax[l][index])):
            error += U[l]
        error /= float(len(datax))
        record.append((error , k , index , j))
  record.sort(key=error_cmp)
  return record[0]

def measure_error(U , s , i , theta , datax , datay):
  counter1 = 0.0
  counter2 = 0.0
  for j in range(len(datax)):
    counter1 += (U[j] * (int(datay[j]) != hypothesis(s , i , theta , datax[j][i])))
    counter2 += U[j]
  return float(counter1 / counter2)

def adaboost(data , datax , datay , T):
  N = float(len(datax))
  U = [(1.0/N) for i in range(len(datax))]
  alpha = []
  parameter = []
  Ein = []
  for i in range(T):
    error_record = 0.0
    (error , s , feature , theta) = DSA(data , U)

    parameter.append((s , feature , theta))
    eps = measure_error(U , s , feature , theta , datax , datay)
    diamond = math.sqrt(float((1.0-eps)/eps))
    alpha.append(math.log(diamond))
    for j in range(len(datax)):
      if(int(datay[j]) != hypothesis(s , feature , theta , datax[j][feature])):
        U[j] *= diamond
      else:
        U[j] /= diamond
      if(int(datay[j]) != G(alpha , datax[j] , i , parameter)):
        error_record += 1.0

    Ein.append(float(error_record / len(datax)))

  return alpha , s , feature , theta , parameter , Ein

def G(alpha , x , t , parameter):
  counter = 0.0
  for i in range(t+1):
    counter += alpha[i]*hypothesis(parameter[i][0] , parameter[i][1] , parameter[i][2] , x[parameter[i][1]])
  return sign_my(counter)

T = 300
data , datax , datay = readin_data(train_filename)
alpha , s , feature , theta , parameter , Ein = adaboost(data , datax , datay , T)
plt.plot(Ein)
plt.show()
print "Ein(G):" , Ein[-1]

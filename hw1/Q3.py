import math
import numpy as np

alpha = [0 , 0.21970141 , 0.28015714 , 0.33323258 , 0.06819373 , 0.09843225 , 0]
Y = [-1 , -1 , -1 , 1 , 1 , 1 , 1]
x1 = [0 , 0 , 0 , -4 , 0 , 0 , 0]
x12 = [0 , 0 , 0 , 4 , 0 , 0 , 0]
x2 = [0 , 4 , -4 , 0 , 8 , -8 , 0]
x22 = [0 , 4 , 4 , 0 , 16 , 16 , 0]
counter_cons = 0
counter_x1 = 0
counter_x12 = 0
counter_x2 = 0
counter_x22 = 0
for i in range(0 , 7):
  print alpha[i]*Y[i]
  counter_cons += alpha[i]*Y[i]
  counter_x1 += alpha[i]*x1[i]
  counter_x12 += alpha[i]*x12[i]
  counter_x2 += alpha[i]*x2[i]
  counter_x22 += alpha[i]*x22[i]


print counter_cons-1.66633495 , counter_x1 , counter_x12 , counter_x2 , counter_x22

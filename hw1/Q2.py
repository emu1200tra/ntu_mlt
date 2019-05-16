from sklearn import svm
from sklearn.svm import SVC  
X = [[1, 0], [0, 1] , [0 , -1] , [-1 , 0] , [0 , 2] , [0 , -2] , [-2 , 0]]
y = [-1 , -1 , -1 , 1 , 1 , 1 , 1]
clf = svm.SVC(kernel='poly' , degree=2 , coef0=1 , gamma=2 , C=10000000)
clf.fit(X, y)  

print 'SVs: ' , clf.support_vectors_

print 'y*alpha: ' , clf.dual_coef_

print 'b: ' , clf.intercept_
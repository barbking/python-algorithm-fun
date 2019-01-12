# scalar, vector, matrix review in numpy
import numpy as np

myVect = np.array([1, 2, 3, 4])
print(myVect)

myVect1 = np.arange(1, 10, 2)
print(myVect1)

myVect3 = np.array(np.int16([1, 1, 1, 1]))
print(myVect3)
print(myVect3 + 1)
print(myVect1 ** 2)

a = np.array([1, 2, 3, 4])
print(a)
b = np.array([2, 2, 4, 4])
print(a == b)
#np.array([False, True, False, True], dtype=bool)
print(a)
print(a < b)
#array([True, False, True, False], dtype=bool)

#vector multiplication, need a dot product
#https://www.mathisfun.com/algebra/vectors-dot-proudct.html for more info
print(myVect.dot(myVect))

#create matrix
myMatrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(myMatrix[0,0])
print(myMatrix[1,2,])

#matrix with certain start values
myMatrix2 = np.ones([4,4], dtype=np.int32)
print(myMatrix2)
#numpy supports a matrix class
myMatrix1 = np.mat([[1,2,3],[4,5,6],[7,8,9]])
print(myMatrix)

#multiplying matrixes (must be same shape, same rows and columns)
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2,3],[4,5,6]])
print('c*d=',c*d)

#dot products of matrixes
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2,3],[3,4,5],[5,6,7]])
print('c.dot(d):',c.dot(d))

#advanced matrix operations, reshaping
changeIt = np.array([1,2,3,4,5,6,7,8])
results = changeIt.reshape(2,4)
print('results:',results)
results2 = changeIt.reshape(2,2,2)
print('results2:',results2)

#transpose matrix
results3 = np.transpose(results)
print('results3',results3)

#identity matrix
print(np.identity(4))

#create inverse, use to ovtain a dot product and compare dot to identity
a = np.array([[1,2],[3,4]])
b = np.linalg.inv(a)
print(np.allclose(np.dot(a,b), np.identity(2)))
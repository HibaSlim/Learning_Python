import  numpy as np

arr = np.array([1,2,3])
print(arr)
print(type(arr))
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
'''print (arr1)
arr1 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print (arr1)
arr1 = np.array([(1,2,3),(4,5,6)])
print (arr1)
x=(1,2,3),(4,5,6)
arr1 = np.array(x)
print (arr1)'''

# write 2 matrices A(3,3) and B(3,3) and do the operation A+B, A-B, 2*B

A= np.array([[1,2,3],[4,5,6],[7,8,9]])
B= np.array([[10,11,12],[13,14,15],[16,17,18]])
'''C= A+B
D= A-B
E= 2*B
print('A+B =',C)
print('A-B = ',D)
print('2*B = ',E)
#matrix multiplication as per element-wise multiplication
F= A*B
print('A*B = ',F)
#matrix multiplication as per linear algebra rules
res = A.dot(B)
print(res)
# compare A to B
print(A<B)
#compare A elements to 2
print(A==2)
# check if B is pair
print(B%2==0)
# calculate he sqrt of B
print(np.sqrt(B))
# calculate the exp of A
print(np.exp(A))
# calculate sin/cos A/B
print(np.sin(A), np.cos(B))
# find the min/max in the matrix
print(A.min(),  A.max())
print(A.min())
print(A.max())
# find SUM A
print(A.sum())

# find the min/max in all ligne
print(A.min(axis=0))
print(B.max(axis=0))
# find the min/max in all column
print(B.max(axis=1), A.min(axis=1))'''

'''
# how to work with matrice
print(A[0])
print(A[0,2])
print(A[0:2])
print(A[0:2][1:3])
# to find the last element in A
print(A[-1])
# find the pair in matrix
print(A[A%2==0])
# find the impair in B
print(B[B%2==0])
# find the element that are superior to the mean
print(A[A>A.mean()])

# how to print the row of the matrix
for row in A:
    print(row)
# how to print element per element in matrix
for row in B:
    for element in row:
        print(element)'''

# Shape manipulation
C = np.array([[ 1,  2,  3,  4,  5,  6],
              [ 7,  8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18]])
print(C)
print(C.reshape(9,2))
print(C.T) #transpose C

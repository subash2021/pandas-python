import numpy as np

# Indexing, Slicing a 1-D ndarray
print("\n# Indexing, Slicing a 1-D ndarray:")
x = np.array([5, 10, 15, 20, 25, 30, 35])
print('x: \n',x)
print(x[1])  # Indexing
print(x[1:6]) # Slicing
print(x[1:6:2]) # Slicing


# Indexing, Slicing a 2-D ndarray
print("\n# Indexing, Slicing a 2-D ndarray")
y = np.array([[0, 1, 2],
              [3, 4, 5]])
print('y: \n',y)
print(y[1:2, 1:3]) 
print(y[1])   
print(y[:,1])


# Slicing Higher Dimensions ndarrays
print("\n# Slicing Higher Dimensions ndarrays")
z = np.array([[[-1, 1], [-2, 2]],
              [[-4, 4], [-5, 5]],
              [[-7, 7], [-9, 9]]])
print('z: \n',z)
print("**************")
print("z[1,:,1] = ")
print(z[1,:,1]) # index 1 element in row of index 1
print("**************")
print("z[1:,1,:] = ")
print(z[1:,1,:]) # From all outer rows except the first, select 1st index element (which itself is an array) completely.
print("**************")
print("z[2] = ")
print(z[2]) # print 2nd index element


# Iterating using for
print("\n\n***************************************************")
print("# Iterating using for")
x = np.array([[-1, 1], [-2, 2]])
for row in x:
    print('Row :',row)

# Iterating using 'nditer'
# nditer method of numpy creates an iterator, which enable accessing each element one after the other.
print("\n# Iterating using 'nditer'")
x = np.array([[0,1], [2, 3]])
for a in np.nditer(x):
    print(a)


# Boolean Indexing
print("\n# Boolean Indexing")
x = np.arange(10).reshape(2,5)
print("x :\n",x)
condition = x % 2 == 0
print(condition)
print(x[condition])
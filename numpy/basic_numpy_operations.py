import numpy as np


# Scalars
print("\n#Operations in Numpy are carried out element wise.")
x = np.arange(6).reshape(2,3)
print('x: \n', x)
print("x+10: ")
print(x+10)
print("x*3: ")
print(x*3)
print("x%2: ")
print(x%2)


# Basic operations between Arrays
print("\n\n# Operations between arrays also happen element wise.")
x = np.array([[-1, 1], [-2, 2]])
y = np.array([[4, -4], [5, -5]])
print("x: \n",x)
print("y: \n", y)
print("\n x+y: ")
print(x + y, end='\n\n')
print("x*y: ")
print(x * y)


# It is also possible to perform operations on arrays with varying size and shape.
print("\n\n# It is also possible to perform operations on arrays with varying size and shape.")
x = np.array([[-1, 1], [-2, 2]])
y = np.array([-10, 10])
print("x: \n",x)
print("y: \n", y)
print("x*y: ")
print(x * y)


# Universal Functions
print("\n\n#Universal Functions: ")
x = np.array([[0,1], [2,3]])
print("x: \n",x)
print("\nnp.square(x): ")
print(np.square(x))
print("\nsin(x): ")
print(np.sin(x))


# Array Methods
print("\n\n#Many of the universal functions are available as methods of ndarray class for example sum")
x = np.array([[0,1], [2, 3]])
print("x: \n",x)
print("\nx.sum(): ")
print(x.sum())
print("\nx.sum(axis=0)")
print(x.sum(axis=0))
print("\nx.sum(axis=1)")
print(x.sum(axis=1))
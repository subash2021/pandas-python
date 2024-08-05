import numpy as np

# 1.ndarray shape
# Enter your code here. Read input from STDIN. Print output to STDOUT
def ndshape(d, shape1):
    #Write your code here
    #Write your code here
    x1 = np.zeros(shape=(d, d))
    np.fill_diagonal(x1,1)
    print(x1)
    
    
    x2 = np.array(shape1)
    shape = x2.shape
    x2 = np.full(shape=(shape1), fill_value=1.)
    print(x2)

tuple = (2,5)
d = 3
ndshape(d, list)


# 3D Array
def array_3d(n, x, y, z):
    np.random.seed(100)
    x1 = 5 + 2.5*np.random.randn(n)
    A = x1.size * int(x1.itemsize)
    
    
    x2 = np.random.rand(x,y,z)
    print(A)
    print(x2)


# More on ndarray
def arr(a, x, y, z):
    #Write your code here
    x1 = np.arange(2,a,2)
    print(x1)
    
    x2 = np.linspace(x,y,z)
    print(x2)
import numpy as np


# ndarrays from Lists
a = [
    [[4.1, 2.5], [1.1, 2.3], [9.1, 2.5]], 
    [[8.6, 9.9],[3.6, 4.3], [6.6, 0.3]]
    ]
x = np.array(a, dtype='float')
print(type(x), x.ndim, x.shape)


# Array create methods
# zero method
y = np.zeros(shape=(2,4))
print (y)
# full method
z = np.full(shape=(2,3), fill_value=10.5)
print(z)


# Numeric sequence generators
# arrange
a = np.arange(3,15,2.5) # 2.5 is the step
print(a)
# linspace
b = np.linspace(3,15,5) #5 is the size of numpy array b
print(b)


# random module
np.random.seed(100) # setting seed
c = np.random.rand(5) # 5 random numbers between 0 and 1
print(c)
np.random.seed(1000) # setting seed
d = np.random.randint(1,1000,3) #3 random integers between 1 and 1000
print(d)


# simulating normal distribution
print("#simulating normal distribution")
np.random.seed(100)
n = np.random.randn(3) #Standard normal distribution
print(n)
np.random.seed(100)
m = 10 + 2*np.random.randn(5) # normal distribution with mean 10 and sd 2
print(m)


# reading data from a file
# loadtxt is used to read data from a text file or any input data stream.
from io import StringIO
str = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')
s = np.loadtxt(str,delimiter=' ')
print(s)
print(s.ndim, s.shape)




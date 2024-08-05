# Array Manipulation
import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_split(n,n_row,n_col):
    x = np.arange(n)
    z = x.reshape(n_row,n_col)
    a, b = np.vsplit(z,2)
    print(a)
    print(b)

# Join Arrays
def join_array(list1,list2):
    p = np.array(list1).reshape(2,2)
    q = np.array(list2).reshape(2,3)
    r = np.hstack((p,q))
    print(r)




np.random.seed(100)
x = np.random.randint(-30,30,30).reshape(5,6)
print(x.sum(axis=0))
print(x.sum(axis=1))
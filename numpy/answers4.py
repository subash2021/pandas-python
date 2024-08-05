import numpy as np


# Array Indexing
def array_index(n,n_row,n_col):
    x = np.arange(n).reshape(n_row,n_col)
    print(x[-1])
    middle = round(int(n_col-1)/2)
    #print("middle: ", middle)
    print(x[:,middle])
    print(x[:2,-3:])

array_index(30,6,5)


# Slicing
def array_slice(n,n_dim,n_row,n_col):
    x = np.arange(n).reshape(n_dim,n_row,n_col)
    #print(x)
    boolean_array = np.array([True,False]).reshape(2,)
    print("boolean_array: \n", boolean_array)
    print(x[boolean_array])
    print(x[boolean_array, :, 1:3])
    
array_slice(30,2,3,5)
import numpy as np

x = np.array([2,3,4,5,7,2,45,22])
print(type(x))


array2_D = np.array([
    [6,9,5],
    [10,82,34],
    [20,30,40]      ])
print(array2_D)

print(f"ndim: {array2_D.ndim}\nshape: {array2_D.shape}\nsize: {array2_D.size}\ndtype: {array2_D.dtype}\nitemsize: {array2_D.itemsize}\nnbytes: {array2_D.nbytes}")

"""
Numpy dtypes
Numpy supports various data types based on number of bytes required by the data elements.
Data type can be explicitly specified with dtype argument.
A ndarray, holding float values is defined in Example below.
"""
y = np.array([[1,2,3],[4,5,6]],dtype='float')
print(y.dtype)


y = np.array([3+4j, 0.4+7.8j])
print(y.shape)


arr = [1,2,3]
np_arr = np.array(arr)
print(np_arr)
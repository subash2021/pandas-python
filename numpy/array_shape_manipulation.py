

# Reshape
import numpy as np
print("\n Reshape")
np.random.seed(100)
x = np.random.randint(10,100,8)
print(x, end='\n\n')
y = x.reshape(2,4)
print(y, end='\n\n')
z = x.reshape(2,2,2)
print(z)
# Stacking arrays vertically
print("\nVertical Stack: ")
a = np.array([[-1,1],[-3,3]])
b = np.array([[-2,2],[-4,4]])
print(np.vstack((a,b)))

# Stacking arrays horizontally
print("\nHorizontal Stack: ")
c = np.array([[-5,5],[-6,6]])
print("a: \n",a)
print("b: \n",b)
print("c: \n",c)
print("After stacking")
print(np.hstack((a,b,c)))


# Array Split
print("\nSplit: ")
i = np.arange(30).reshape(6,5)
res = np.vsplit(i,2)
print(res[0],end="\n")
print(res[1])

# Split Vertically
print("\n# Splitting Vertically")
print("It is also possible to split at specific row numbers using vsplit: ")
print("The array is splitted vertically at row 2, 4, and 6")
j = np.arange(30).reshape(6,5)
print("j: \n",j)
res = np.vsplit(j,(2,4,6))
print("\nAfter split")
print(res[0])
print(res[1])
print(res[2])

# Splitting Horizontally
print("\n# Splitting Horizontally")
print("Arrays can be split horizontally using the generic hsplit method: ")
print("The array is splitted horizontally at index 2, and 4. The rest elements are kept as it is")
k = np.arange(10).reshape(2, 5)
print("k: \n", k)
res = np.hsplit(k, (2,4))
print("\nAfter split")
print(res[0], end='\n\n')
print(res[1], end='\n\n')
print(res[2])


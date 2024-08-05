
# Operations on Arrays
import numpy as np
def array_oper(num1,num2):
    y = np.arange(num1,num2+1).reshape(2,3)
    x = np.square(y)
    print(x+5)


# Operations on Arrays (Mean Distribution)
def array_oper(n,m,sd):
    np.random.seed(100)
    x = m + sd*np.random.randn(n)
    print(np.mean(x))
    print(np.std(x))
    print(np.var(x))





import numpy as np

x = np.arange(30).reshape(3,5,2)
print("x: \n" ,x)
print(x[1,::2,1])
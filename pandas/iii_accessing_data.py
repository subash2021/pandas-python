# Pandas provide utilities like loc and iloc to get data from a Series, a DataFrame, or a Panel.

import pandas as pd
import numpy as np

print("\n#Accessing Single Value")
z = np.arange(10, 16)
s = pd.Series(z, index=list('abcdef'))
#Accessing 3rd element of s.
print(s[2]) # ---> Returns '12' 
#Accessing 4th element of s.
print(s['d']) # ---> Returns '13'
print(s.get(2))


print("\n#Accessing a slice")
print(s[1:4])
print(s['c':'e'])





import pandas as pd
import numpy as np


print("\n# Knowing a Series")
temp = pd.Series(28 + 10*np.random.randn(10))
print(temp.describe())



print("\n# Knowing a DataFrame")
df = pd.DataFrame({'temp':pd.Series(28 + 10*np.random.randn(10)), 
                'rain':pd.Series(100 + 50*np.random.randn(10)),
             'location':list('AAAAABBBBB')})
print(df.info())
print(df.describe())
print(df.describe(include=['object']))
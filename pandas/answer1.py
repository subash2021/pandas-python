#Write your code here
import pandas as pd
import numpy as np


heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'])
#print(heights_A)
print(heights_A.shape)


weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
print(weights_A.dtype)


columnData= ["Student_height","Student_weight"]
df_A = pd.DataFrame(columns = columnData, index=['s1','s2','s3','s4','s5'])
print(df_A.shape)


np.random.seed(100)
numpy_height = 170.0 + 25.0*np.random.randn(5)
heights_B = pd.Series(numpy_height, index=['s1','s2','s3','s4','s5'])
#print(heights_B)

numpy_weight = 75.0 + 12.0*np.random.rand(5)
weights_B = pd.Series(numpy_weight,index=['s1','s2','s3','s4','s5'])
#print(weights_B)
#print(weights_B.mean())
print(numpy_height.mean())


df_B = pd.DataFrame(index=['s1','s2','s3','s4','s5'])
df_B['Student_height'] = heights_A
df_B['Student_weight'] = weights_B
print(df_B.columns)


"""
(5,)
float64
(5, 2)
172.37417741633146
Index(['Student_height', 'Student_weight'], dtype='object')

"""
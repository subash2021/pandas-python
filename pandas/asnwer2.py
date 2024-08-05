# Python Pandas |2| Accessing Pandas Data Structures

#Write your code here
import pandas as  pd
import numpy as np


# Task 1
heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4],index=['s1','s2','s3','s4','s5'])
print(heights_A[1])


# Task 2
print(heights_A[[1,2,3]])


# Task 3
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height':heights_A, 'Student_weight':weights_A})
height = df_A['Student_height']
#print(height)
print(type(height))

# Task 4
df_s1s2 = pd.DataFrame(df_A.iloc[0:2,:])
print(df_s1s2)


# Task 5
df_s2s5s1 = pd.DataFrame(df_A.loc[['s2','s5','s1'],:])
print(df_s2s5s1)


#Task 6
#df_s1s4 = pd.DataFrame(df_A.loc[['s1','s4'],:])
df_s1s4 = df_A.loc[(df_A.index.str.endswith('1') | df_A.index.str.endswith('4'))]
print(df_s1s4)
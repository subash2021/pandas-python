import pandas as pd

print("\nCreating Panda Series")
# Creating Panda Series with default index
print("\nwith default index: ")
s = pd.Series(["Nepal","USA","Canada","Australia"])
print(s)

# Creating Panda Series with default our own index
print("\nwith index abcd: ")
s = pd.Series(["Nepal","USA","Canada","Australia"], index = ["a","b","c","d"])
print(s)

print("\nwith index wxyz: ")
s = pd.Series(["Nepal","USA","Canada","Australia"], index = list('wxyz'))
print(s)

print("\n*****************************************************************")
print("\nPanda Series using list")
# Creating Panda Series using lists, tuples, dictionary
country = ["Nepal","USA","Canada","Australia"]
amount  = [4000,85000,70000,69000]
income = pd.Series(amount,index = country)
print(income)

print("\nPanda Series using tuple")
country = ("Nepal","USA","Canada","Australia")
amount  = (4000,85000,70000,69000)
income = pd.Series(amount,index = country)
print(income)

print("\nPanda Series using dictionary")
income_dict = {"Nepal":4000,"USA":85000,"Canada":70000,"Australia":69000}
income = pd.Series(income_dict)
print(income)
import pandas as pd

EmployeeData = {

    "Id":[101,102,103,104,105,106,107,108],
    "Name":["Jack","Bella","Eminem",'Ed Sheeran','Taylor','Drake','Tom','Justin'],
    "Salary":[95000,80000,115000,10000,20000,300000,400000,500000],
    "Age":[15,25,35,45,55,65,75,85]
}
print("\n**************************** loc ***********************************")
print("Remember loc range are inclusive")
print("\nInitial Data:")
data = pd.DataFrame(EmployeeData)
print(data)


print("\n# data.loc[0:3,:]")
print(data.loc[0:3,:])


print("\n# data.loc[7,'Salary':'Age']")
print(data.loc[:,'Salary':'Age'])


print("\n# data.loc[:,'Name']")
print(data.loc[:,'Name'])


print("\n# data.loc[data.Salary<100000]")  
print(data.loc[data.Salary<100000])


print("\n# data.loc[data.Age<50,'Name']")
print(data.loc[data.Age<50,'Name'])



print("\n**************************** iloc ***********************************")
print("Remember unlike loc, iloc range are not inclusive ")
print("\n# data.iloc[:,0:2]")
print(data.iloc[:,0:2])


print("\n# data.iloc[:3,:2]")
print(data.iloc[:3,:2])



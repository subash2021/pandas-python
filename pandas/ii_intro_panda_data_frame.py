import pandas as pd

# Pandas Dataframe is the collection of pandas data series
print("\nCreating pandas data frame using dictionary:")
EmployeeData = {

    "Id":[101,102,103],
    "Name":["Jack","Bella","Eminem"],
    "Salary":[95000,80000,115000]
}
pandaDB = pd.DataFrame(EmployeeData)
print(pandaDB)


# Creating Empty Data Frame and adding items into it
print("\n# Creating Empty Data Frame and adding items into it")
empty_df = pd.DataFrame()
print(empty_df)


print("\n#Adding columns to the empty dataframe")
columnData = ['Id','Name','Salary']
empty_df = pd.DataFrame(columns = columnData)
print(empty_df)


print("\n#Adding Values in the data frame")
new_row = {'Id':[101],'Name':['Jack'],'Salary':[95000]}
empData = pd.DataFrame(new_row)
print(empData)


print("\n#Adding new column")
empData['Experience'] = [2]
print(empData)
print(empData.columns.values)


import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

df = sm.datasets.get_rdataset("iris").data 
df.info()
df.Species.unique() 

iris_subset = df[(df.Species == "versicolor") | (df.Species == "virginica")].copy()

print(iris_subset.Species.unique())

df_subset = df[(df.Species == "versicolor") | (df.Species == "virginica" )].copy() 

df_subset.Species = df_subset.Species.map({"versicolor": 1, "virginica": 0}) 

df_subset.rename(columns={"Sepal.Length": "Sepal_Length", "Sepal.Width": "Sepal_Width",	"Petal.Length": "Petal_Length", "Petal.Width": "Petal_Width"}, inplace=True) 

model = smf.logit("Species ~ Petal_Length + Petal_Width", data=df_subset)

result = model.fit()
print(result.summary())



df_new = pd.DataFrame({"Petal_Length": np.random.randn(20)*0.5 + 5,
                       "Petal_Width": np.random.randn(20)*0.5 + 1.7})
df_new["P-Species"] = result.predict(df_new)
df_new["P-Species"].head(3)

df_new["Species"] = (df_new["P-Species"] > 0.5).astype(int)
df_new.head()
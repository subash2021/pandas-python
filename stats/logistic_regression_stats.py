#Write your code here

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

def build_log_reg():
    """
    - Load the R dataset biopsy from the MASS package and capture the data as a pandas dataframe.
    - Rename the column name class to Class. 
    - Transform the Class column values benign and malignant to '0' and '1' respectively.
    - Build a logistic regression model with independent variable V1 and dependent variable Class.
    - Fit the model with data, and return the pseudo R-squared value as float.

    Returns
    -------
    r_squared : float
        r-squared value of the trained logistic regression model
    """
    df = sm.datasets.get_rdataset("biopsy","MASS").data
    df.rename(columns = {'class':'Class'},inplace=True)
    #print(df.info())
    df_subset = df[(df.Class == "benign") | (df.Class=='malignant')].copy()
    df_subset.Class = df_subset.Class.map({"benign":0,"malignant":1})
    model = smf.logit("Class ~ V1",data=df_subset)
    result = model.fit()
    return result.prsquared
print(build_log_reg())
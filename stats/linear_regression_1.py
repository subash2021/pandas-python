#Write your code here

import statsmodels.api as sm
import statsmodels.formula.api as smf

def build_lr():
    """
    - Load the R dataset mtcars and capture the data as a pandas dataframe.
    - Build a linear regression model with independent variable `wt`, and dependent variable `mpg`.
    - Fit the model with data, and return the R-squared value as float.

    Returns
    -------
    r_squared : float
        r-squared value of the trained linear regression model
    """
    mtcars = sm.datasets.get_rdataset("mtcars")
    mtcars_dataset = mtcars.data
    print(mtcars_dataset.columns)
    linear_model = smf.ols('mpg~wt',mtcars_dataset)
    linear_result = linear_model.fit()
    return float(linear_result.rsquared)
x = build_lr()
print(x)

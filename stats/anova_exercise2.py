#Write your code here

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import anova
import numpy as np

def build_anova():
    """
    - Load the R dataset `mtcars`. and capture the data as a pandas dataframe.
    - Build a linear regression model by considering the `log` of independent variable `wt`, and log of dependent variable mpg.
    - Fit the model with data, and perform ANOVA on the linear model. (Hint:Use anova.anova_lm)
    - Return the F-statistic value as a float

    Returns
    -------
    f1_score : float
       F-statistic value of the ANOVA model
    """
    df = sm.datasets.get_rdataset("mtcars").data
    linear_model = smf.ols('np.log(mpg) ~ np.log(wt)',df)
    linear_result = linear_model.fit()
    anova_result = anova.anova_lm(linear_result).F['np.log(wt)']
    return float(anova_result)
print(build_anova())
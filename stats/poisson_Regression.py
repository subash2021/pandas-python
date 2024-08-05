#Write your code here

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
def build_pos_reg():
    """
    - Load the R dataset `Insurance` from the `MASS` package. and capture the data as a pandas dataframe.
    - Build a Poisson regression model with a log of an independent variable `Holders`, and dependent variable `Claims`
    - Fit the model with data, and return the sum of the residuals as float.

    Returns
    -------
    residuals_sum : float
        sum of the residuals for the trained poission regression model
    """
    Insurance_df = sm.datasets.get_rdataset("Insurance","MASS").data
    poisson_model = smf.poisson('Claims ~ np.log(Holders)',Insurance_df)
    poisson_model_result = poisson_model.fit()
    print(poisson_model_result.summary())
    print(float(np.sum(poisson_model_result.resid)))

build_pos_reg()

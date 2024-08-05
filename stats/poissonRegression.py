import pandas as pd
awards_df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/poisson_sim.csv")
print(awards_df)


#creating the  model
import statsmodels.formula.api as smf
poisson_model = smf.poisson('num_awards ~ math + C(prog)', awards_df)

#fitting the model
poisson_model_result = poisson_model.fit()
print(poisson_model_result.summary())
print(poisson_model_result.prsquared)
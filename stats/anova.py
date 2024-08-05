import statsmodels.api as sm
icecream = sm.datasets.get_rdataset("Icecream",'Ecdat')
icecream_data = icecream.data

import statsmodels.formula.api as smf
model1 = smf.ols('cons ~ temp', icecream_data).fit()


from statsmodels.stats import anova
print(anova.anova_lm(model1))

'''
Building New Model
Now let's create a new model with two independent variables and one response variable.
With more that one independent variable, the null hypothesis is stated as Coefficients of all independent variables are zero. i.e B1 = 0, and B2 = 0.
The alternative hypothesis will be that atleast one of the parameters Bj != 0 where j takes the values 1, 2, ...
'''
model2 = smf.ols('cons ~ income + temp', icecream_data).fit()
print(anova.anova_lm(model2))
#print(stats.f.sf(31.81, 2, 27))
print(anova.anova_lm(model1, model2))


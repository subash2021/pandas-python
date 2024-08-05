import statsmodels.api as sm

icecream = sm.datasets.get_rdataset("Icecream", "Ecdat")
icecream_data = icecream.data
#print(icecream_data.columns)

#model using cons and price
import statsmodels.formula.api as smf
linear_model1 = smf.ols('cons ~ price + temp',icecream_data)
linear_result1 = linear_model1.fit()
#print(linear_result1.summary())

# model using income and temp
linear_model2 = smf.ols('cons~income+temp', icecream_data)
linear_result2 = linear_model2.fit()
#print(linear_result2.summary())

#without considering intercept term
linear_model3=smf.ols('cons~-1+income+temp',icecream_data)
linear_result3 = linear_model3.fit()
#print(linear_result3.summary())
print(linear_result3.rsquared)

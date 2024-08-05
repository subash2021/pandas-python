from scipy import stats
import numpy as np

mu, sigma = 0.8, 0.5
X = stats.norm(mu, sigma)

n = 100
X_sample = X.rvs(n)
print(X_sample)
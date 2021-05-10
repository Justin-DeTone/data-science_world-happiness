import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels as ssm

df = pd.read_csv("data\world-happiness-report-2021.csv")

y_feature = ["Ladder score"] * 6
features = ["Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

dependent = df["Ladder score"]
independent = df[["Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]]

model = LinearRegression()

model.fit(independent, dependent)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

intercept = model.intercept_
coefficients=model.coef_

print("R2: ", model.score(independent, dependent))
print("Intercept: ", intercept)
print("coefficients: ", coefficients)

x = ssm.add_constant(independent)
model = ssm.OLS(dependent, independent).fit()
predictions = model.summary()
print(predictions)
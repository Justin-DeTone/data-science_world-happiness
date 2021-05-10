import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data\world-happiness-report-2021.csv")

y_feature = ["Ladder score"] * 6
features = ["Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

dependent = df["Ladder score"]
independent = df["Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

model = LinearRegression()

model.fit(independent, dependent)
LinearRegression(copy_x=True, fit_intercept=True, n_jobs=None, normalize=False)

intercept = model.intercept_
coefficients=reg.coef_

print(model.score(independent, dependent))

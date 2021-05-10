import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data\world-happiness-report-2021.csv")
print(df.columns)
print(df.shape)

quarter1 = df[df['Logged GDP per capita'] < 8.541]
quarter2 = df[(df['Logged GDP per capita'] >= 8.541) & (df['Logged GDP per capita'] < 9.569)]
quarter3 = df[(df['Logged GDP per capita'] >= 9.569) & (df['Logged GDP per capita'] < 10.421)]
quarter4 = df[df['Logged GDP per capita'] >= 10.421]

quarter = quarter1

y_feature = ["Ladder score"] * 6
features = ["Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

fig, axes = plt.subplots(nrows = 2, ncols = 3)

axes = axes.ravel()
for idx, ax in enumerate(axes):
	model = LinearRegression()
	model.fit(quarter[features[idx]].to_numpy().reshape(-1, 1), quarter[y_feature[idx]].to_numpy().reshape(-1,1))
	ax.scatter(quarter[features[idx]], quarter[y_feature[idx]])
	
	xmin, xmax = ax.get_xlim()
	#ymin, ymax = ax.get_ylim()
	
	x_new = np.linspace(xmin, xmax, 100)
	y_new = model.predict(x_new[:, np.newaxis])
	
	ax.plot(x_new, y_new)
	ax.set_xlabel(features[idx], fontsize=10)
	ax.set_ylabel(y_feature[idx], fontsize=10)
	ax.tick_params(axis='both', labelsize=15)
	
	print(model.score(quarter[features[idx]].to_numpy().reshape(-1, 1), quarter[y_feature[idx]].to_numpy().reshape(-1,1)))
	print("coefficient: ", model.coef_)


plt.show()
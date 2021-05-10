import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (20, 10)

fig, axes = plt.subplots(nrows = 2, ncols = 4)
axes[-1, -1].axis('off')

df = pd.read_csv("data\world-happiness-report-2021.csv")
print(df.columns)

features = ["Ladder score", "Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
xaxes = features
yaxes = ["Counts"] * 7

#flatten array of axes
axes = axes.ravel()
for idx, ax in enumerate(axes[:-1]):
	ax.hist(df[features[idx]].dropna(), bins = 30)
	ax.set_xlabel(xaxes[idx], fontsize=20)
	ax.set_ylabel(yaxes[idx], fontsize=20)
	ax.tick_params(axis='both', labelsize=15)
	
plt.show()


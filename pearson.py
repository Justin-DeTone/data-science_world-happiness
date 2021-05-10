import matplotlib.pyplot as plt
import pandas as pd
from yellowbrick.features import Rank2D

df = pd.read_csv("data\world-happiness-report-2021.csv")
features = ["Ladder score", "Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

data_array = df[features].to_numpy()

visualizer = Rank2D(features=features, algorithm='pearson')
visualizer.fit(data_array)
visualizer.transform(data_array)
visualizer.poof()
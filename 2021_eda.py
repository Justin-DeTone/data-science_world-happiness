import pandas as pd
#import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from plot2 import plot_table



df = pd.read_csv("data\world-happiness-report-2021.csv")

plot_table(df.describe(), 3000, 400, "2021_vars.png", True)
plot_table(df.describe(include=['O']), 1000, 400, "2021_categories.png")


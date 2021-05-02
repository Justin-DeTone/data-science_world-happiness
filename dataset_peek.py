import pandas as pd

def peek(df):
	print("The dimensions of this table are: ", df.shape)
	print("The column names are: ", df.columns)
	print("These columns have the following data types:\n", df.dtypes)
	
if __name__ == "__main__":
	happiness2021 = pd.read_csv("data\world-happiness-report.csv")
	peek(happiness2021)
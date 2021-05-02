import pandas as pd
#import matplotlib.pyplot as plt
import plotly.figure_factory as ff


def add_space(str_header):
	header_list = str_header.split()
	output = ""
	for word in header_list:
		output += word + "\n"
	print(output)
	return output[:-1]
	
def clip_title(str_header):
	return str_header[:20]

happiness2021 = pd.read_csv("data\world-happiness-report.csv")
print(happiness2021.columns)
happiness2021.rename(columns=clip_title, inplace=True)
print(happiness2021.columns)

#exit()

#happiness2021.style.set_table_styles([dict(selector="th",props=[('max-width', '50px')])])

print(happiness2021.head(5))

print("The dimensions of this table are: ", happiness2021.shape)

print(happiness2021.dtypes)
print("columns: ", happiness2021.columns)

def plot_table(df, width, height, img_name, truncate_text=False):
	new_df = df
	if truncate_text:
		new_df.rename(columns=clip_title, inplace=True)
	fig = ff.create_table(new_df.reset_index())
	fig.update_layout(
		autosize=False,
		width=width,
		height=height
)
	fig.write_image(img_name, scale=1)
	fig.show()
	return 1
	

fig = ff.create_table(happiness2021.head(20))
fig.update_layout(
	autosize=False,
	width=1500,
	height=400
)
fig.write_image("historical.png", scale=1)
fig.show()



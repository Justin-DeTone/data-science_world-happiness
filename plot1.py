import pandas as pd
import matplotlib.pyplot as plt


happiness2021 = pd.read_csv("data\world-happiness-report-2021.csv")

print(happiness2021.head(8))

print("The dimensions of this table are: ", happiness2021.shape)

print(happiness2021.dtypes)
print("columns: ", happiness2021.columns)

cells_list = happiness2021.head(8).values.tolist()
col_headers = happiness2021.columns.tolist()
print("col headers: ", col_headers)
#print(cells_list)
row_headers = [x.pop(0) for x in cells_list]
print("row headers: ", row_headers)
#print(cells_list)

cell_text = []
for row in cells_list:
	cell_text.append([f'{value:.3f}' if type(value) is not str else value for value in row])
print("CELL TEXT: ", cell_text)

#Create the figure
plt.figure(linewidth=2,
	tight_layout={'pad':1},
	)

table = plt.table(
	#figsize=(15,5),
	cellText=cell_text,
	rowLabels=row_headers,
	rowLoc='right',
	colLabels=col_headers,
	loc='center',
	#bbox=[0,1,0,1]
	)
table.auto_set_font_size(False)

num_cols = len(col_headers)

table.auto_set_column_width([num for num in range(num_cols)])
table.set_fontsize(10)
#table.scale(1, 3)

#Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

#Hide axes border
plt.box(on=None)

#Create image
fig = plt.gcf()

#fig.set_size_inches(18.5, 10.5)
#plt.tight_layout()
plt.rcParams["figure.figsize"] = (20,3)

plt.savefig('test.png',
	bbox_inches='tight',
	dpi=150
	)
#plt.show()
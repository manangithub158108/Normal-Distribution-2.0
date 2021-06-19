import csv;
import plotly.figure_factory as ff;
import plotly.graph_objects as go;

with open('data.csv') as f:
    reader = csv.reader(f);
    file_data = list(reader);

file_data.pop(0);

data = [];

for i in range(0, len(file_data)):
    avg_rating = float(file_data[i][2]);
    data.append(avg_rating);

fig = ff.create_distplot([data], ['Average rating'], show_hist=False);
fig.show();
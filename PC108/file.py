import pandas as pd
import plotly.figure_factory as pff
import csv

df = pd.read_csv("data.csv")

fig = pff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"])

fig.show()
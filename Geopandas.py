import geopandas
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#https://www.nomisweb.co.uk/sources/census_2021_pc

df = pd.read_csv("Household #.csv")
df['Postcode'] = df['Postcode'].str.split(' ').str[0]
df['Postcode'] = df['Postcode'].replace('\d', '', regex=True)
df = df.rename(columns={"Postcode":"id"})
df = df.groupby('id').sum().reset_index()

print(df)

UK = geopandas.read_file("uk-postcode-area.geojson")

UK = pd.merge(right=df, left=UK, on="id")

print(UK)

#UK.crs

fig, ax = plt.subplots(1, 1)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
title1 = "# Households by Postcode 2021"

UK_plot = UK.plot(column='Count',
                  cmap='OrRd',
                  ax=ax,
                  legend=True,
                  cax=cax,
                  legend_kwds={"orientation": "vertical"})

UK_plot.set_axis_off()
ax.set_title(title1)

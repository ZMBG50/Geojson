import geopandas
import pandas as pd 

#https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/articles/subnationalindicatorsexplorer/2022-01-06

df = pd.read_csv("pcd_p002.csv")
df['Postcode'] = df['Postcode'].str.split(' ').str[0]
df['Postcode'] = df['Postcode'].replace('\d', '', regex=True)
df = df.rename(columns={"Postcode":"id"})
df = df.groupby('id').sum().reset_index()

print(df)

UK = geopandas.read_file("uk-postcode-area.geojson")

UK = pd.merge(right=df, left=UK, on="id")


#uk-postcode-area.geojson

print(UK)

UK.crs

#UK = UK.set_geometry("geometry")
#UK2 = UK.to_crs("EPSG:4326")

UK.plot(column='Count', cmap='viridis', legend=True)
#UK.plot(legend=False)

print(UK)
###i am testing the commit
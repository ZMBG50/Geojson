

import geopandas

UK = geopandas.read_file("uk-postcode-area.geojson")

#uk-postcode-area.geojson

print(UK)

UK.crs

UK = UK.set_geometry("geometry")
UK2 = UK.to_crs("EPSG:4326")
UK.plot(legend=True)

###i am testing the commit
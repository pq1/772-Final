# 772-Final
Project files for 772 Final
This houses the files neccessary for the final project. It can be seen at the following link bl.ocks.org/pq1.
This uses the Leaflet.js library as the Web Client to display the data.
Leaflet Ajax to pull in GeoJSONs.
The types of data that is used are .js files, Web GeoJSON files, WebJSON files

Requirements:
• displays data from 3 sources of data via web services.
One should be vector data.
Leaflet ESRI to pull ESRI WMS Services. 
Leaflet TileLayer WMS to pull in a MapServer WMS.
Leaflet LayerJSON to pull in a JSON file.

• provides a faceted search and an event mouse
functionality

Python Script
The houses data is old housing data. It is preprocessed via Python 2.7. It utilizes ESRIs ArcPy and PySHP plugins to convert the csv file into a Shapefile. It selects the houses that are within 1 mile of the Metro stations and creates an new Shapefile. Then the PySHP converts the Shapefile into a GeoJSON file.

#-------------------------------------------------------------------------------
# Name:         House 1 Mile to Metro
# Purpose:      This script uses arcpy to select houses that are within 1 Mile of
# the Metro Stations and creates a Shapefile. It then converts the Shapefile into
# a geojson file using the pyshp module.
# Author:      philip.quach
#
# Created:     17/04/2016
#-------------------------------------------------------------------------------

import arcpy, shapefile

# Workspace location of input and output
workspace = arcpy.env.workspace = r'C:\Users\philip.quach\Downloads\772-hw05'

arcpy.env.overwriteOutput = True

# Variables
print 'Declare workspace'
houses = workspace + '\houses_300_600.csv'
housesTemp = workspace + '\houses'
housesSHP = workspace + '\housesSHP.shp'
metroStations = workspace + '\Metro_Stations_Regional.shp'
sr = arcpy.SpatialReference(4326)

try:
    print 'Make XY from CSV file'
    arcpy.MakeXYEventLayer_management(houses,'Longitude', 'Latitude', housesTemp, sr )

    print 'creating Shapefile'
    arcpy.CopyFeatures_management(housesTemp, housesSHP)

    # Make Temp Feature layer
    arcpy.MakeFeatureLayer_management(housesSHP, workspace + '\tempHouse.shp')

    # Selection of Houses
    print 'Selecting Houses within 1 mile of Metro Stations'
    arcpy.SelectLayerByLocation_management(workspace + '\tempHouse.shp','WITHIN_A_DISTANCE',metroStations,'1 Mile')
    print 'Creating Houses within 1 mile Shapefile'
    arcpy.CopyFeatures_management(workspace + '\tempHouse.shp', workspace + '\houses1mi.shp')
except Exception as err:
    print(err.args[0])

print 'Houses Shapefile Finished'

# using pyshp - https://pypi.python.org/pypi/pyshp#reading-shapefiles-from-file-like-objects
# Source https://gist.github.com/frankrowe/6071443
# read the shapefile
reader = shapefile.Reader( workspace + '\houses1mi.shp')
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
   atr = dict(zip(field_names, sr.record))
   geom = sr.shape.__geo_interface__
   buffer.append(dict(type='Feature', \
    geometry=geom, properties=atr))

# write the GeoJSON file
from json import dumps
geojson = open(workspace + '\pyshp-demo.geojson', 'w')
geojson.write(dumps({'type': 'FeatureCollection',\
'features': buffer}, indent=2) + '\n')
geojson.close()

print 'Script Finished'
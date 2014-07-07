#-------------------------------------------------------------------------------
# Name:        Create polygon from textfile ( name , coordinate strings)
# Purpose:
#
# Author:      Hoa
#
# Created:     04/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import ogr, os, sys
# Working directory
os.chdir(r'E:\GFD_DATA\Study\PYHTHON\Python with GDAL\Week 2 Creating geometries and handling projections\ospy_data2')
# Set driver
driver = ogr.GetDriverByName('ESRI shapefile')

# Create an output shapfile
shp = 'hwa2a.shp'
if os.path.exists(shp):
    driver.DeleteDataSource(shp)
ds = driver.CreateDataSource(shp)
if ds is None:
    print 'Could not create file'
    sys.exit(1)
layer = ds.CreateLayer('hw2a', geom_type = ogr.wkbPolygon)

# Create a field for country name
fieldDefn = ogr.FieldDefn('name', ogr.OFTString)
fieldDefn.SetWidth(30)

# Add the field to shapefile
layer.CreateField(fieldDefn)

# Get the FeatureDefn for the shapefile
featureDefn = layer.GetLayerDefn()

# Open input text file for reading
file = open('ut_counties.txt', 'r')

# Loop through the lines in the text file
for line in file:
    # Create an empty ring geometry
    ring = ogr.Geometry(ogr.wkbLinearRing)

    # Split the line to get country name and coordinate
    tmp = line.split(':')
    name = tmp[0]
    coords = tmp[1]

    # Split coordinates
    coorlist = coords.split(',')


    # Loop through list coordinate
    for coord in coorlist:
        # Split x, y individual
        xy = coord.split()
        x = float(xy[0])
        y = float(xy[1])
        # Add vertex to ring
        ring.AddPoint(x,y)

    # When we have looped through all the coordinates , create a polygon
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)

    # Create a new feature and set its geometry and attribute
    feature = ogr.Feature(featureDefn)
    feature.SetGeometry(poly)
    feature.SetField('name', name)

    # Add the feature to the shapefile
    layer.CreateFeature(feature)
    # Destroy the geomtetries
    ring.Destroy()
    poly.Destroy()
    feature.Destroy()

# Close files
file.close()
ds.Destroy()











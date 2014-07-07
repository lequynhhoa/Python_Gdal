#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Hoa
#
# Created:     03/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, ogr, sys
os.chdir(r'E:\GFD_DATA\Study\PYHTHON\Python with GDAL\Week 2 Creating geometries and handling projections\ospy_data2')
# Get driver
driver = ogr.GetDriverByName('ESRI shapefile')

# Create a new data source and layer
fn = 'test.shp'
if os.path.exists(fn):
    driver.DeleteDataSource(fn)
ds = driver.CreateDataSource(fn)
if ds is None:
    print 'Could not create file'
    sys.exit(1)
layer = ds.CreateLayer('test', geom_type = ogr.wkbPoint)

# Add fields id, cover to the output
idfieldDefn = ogr.FieldDefn('id', ogr.OFTInteger)
coverfieldDefn = ogr.FieldDefn('cover', ogr.OFTString)
layer.CreateField(idfieldDefn)
layer.CreateField(coverfieldDefn)

# Create a new point object
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(150, 75)


# Get the featureDefn for the output layer
featureDefn = layer.GetLayerDefn()

# Create a new feature
feature = ogr.Feature(featureDefn)
feature.SetGeometry(point)
feature.SetField('id', 1)
feature.SetField('cover', 'Apples')


# Add the feature to the output file
layer.CreateFeature(feature)

#Destroy the geometry and feature and close data source
point.Destroy()
feature.Destroy()
ds.Destroy()
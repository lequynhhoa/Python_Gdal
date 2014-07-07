#-------------------------------------------------------------------------------
# Name:        Reproject a shapfile
# Purpose:
#
# Author:      Hoa
#
# Created:     07/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import ogr, os, osr, sys
# Working directory
os.chdir(r'E:\GFD_DATA\Study\PYHTHON\Python with GDAL\Week 2 Creating geometries and handling projections\ospy_data2')
# driver shapfile
driver = ogr.GetDriverByName('ESRI shapefile')

# Create the input spatialreference EPGS 4269
inputCD = osr.SpatialReference()
inputCD.ImportFromEPSG(4269)
# Create the output spatial reference EPGS 26912
outputCD = osr.SpatialReference()
outputCD.ImportFromEPSG(26912)

# Create coordinate transform
coortrans = osr.CoordinateTransformation(inputCD, outputCD)

# Open input data and get the layer
inds = driver.Open('hwa2a.shp', 0)
if inds is None:
    print 'Could not open file'
    sys.exit(1)
inlayer = inds.GetLayer()

# Create a new data source and layer
shp = 'hw2b.shp'
if os.path.exists(shp):
    driver.DeleteDataSource(shp)
outds = driver.CreateDataSource(shp)
if outds is None:
    print 'Could not create file'
    sys.exit(1)
outlayer = outds.CreateLayer('hw2b', geom_type = ogr.wkbPolygon)

# Get the fielddefn for the country name field
feature = inlayer.GetFeature(0)
fieldDefn = feature.GetFieldDefnRef('name')

# Add the field to the output shapefile
outlayer.CreateField(fieldDefn)

# Get the featureDefn for the output file
featureDefn = outlayer.GetLayerDefn()

# Loop through the input features
inFeature =  inlayer.GetNextFeature()
while inFeature:
    # Get input geometry
    geom = inFeature.GetGeometryRef()
    # Reproject the geometry
    # Create a new feature
    outFeature = ogr.Feature(featureDefn)

    # Set the geometry and attribute
    outFeature.SetGeometry(geom)
    outFeature.SetField('name', inFeature.GetField('name'))

    # Add the feature to the shp
    outlayer.CreateFeature(outFeature)
    # Destroy the features and get next input feature
    outFeature.Destroy()
    inFeature.Destroy()
    inFeature = inlayer.GetNextFeature()
# Close the shp
inds.Destroy()
outds.Destroy()

# Create .prj file
outputCD.MorphFromESRI()
file = open('hw2b.prj', 'w')
file.write(outputCD.ExportToWkt())
file.close()





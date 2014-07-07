#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Hoa
#
# Created:     26/06/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Import module
import ogr, os, sys, arcpy
# Create wokspace
os.chdir(r'E:\GFD_DATA\Study\PYHTHON\Python with GDAL\Week 1 Reading and writing vector data with OGR\ospy_data1')
# Create file
file = open('hw_wk1.txt', 'w')
# drive shapfile
driver = ogr.GetDriverByName('ESRI Shapefile')
# Open data source
datasource = driver.Open('sites.shp', 0)
if datasource is None:
    print 'Could not open file'
    sys.exit(1)
#Get data layer
layer = datasource.GetLayer()
#Loops feature in the layer
feature = layer.GetNextFeature()
while feature:
    # Get attribute
    id = feature.GetFieldAsString('id')
    cover = feature.GetFieldAsString('cover')

    # Get geometry Coordinates
    geometry = feature.GetGeometryRef()
    X = str(geometry.GetX())
    Y = str(geometry.GetY())
    # Wirte information to text file

    file.write(id + ' ' + X + ' '+ Y + ' ' + cover + '\n ')

    #Destroy the feature and get a now one
    feature.Destroy()
    feature = layer.GetNextFeature()

datasource.Destroy()
file.close()

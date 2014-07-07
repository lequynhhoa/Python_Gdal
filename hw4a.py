#-------------------------------------------------------------------------------
# Name:        Extract pixel value to text file
# Purpose: Extract pixel value to point and write a textfile
#
# Author:      Hoa
#
# Created:     01/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys, ogr, gdal
from osgeo import ogr, gdal
from osgeo.gdalconst import *
os.chdir(r'E:\GFD_DATA\Study\PYHTHON\Python with GDAL\Week 4 Reading raster data with GDAL\Data')
file = open('extract.csv', 'w')
# open the shapefile and get the layer
driver = ogr.GetDriverByName('ESRI Shapefile')
shp = driver.Open('sites.shp')
if shp is None:
    print 'Could not open sites.shp'
    sys.exit(1)
shpLayer = shp.GetLayer()

# register all of the GDAL drivers
gdal.AllRegister()

# open the image
img = gdal.Open('aster.img', GA_ReadOnly)
if img is None:
    print 'Could not open aster.img'
    sys.exit(1)

# get image size
rows = img.RasterYSize
cols = img.RasterXSize
bands = img.RasterCount

# get georeference info
transform = img.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
#write header file
file.write('id band1 band2  band3\n')
# loop through the features in the shapefile
feat = shpLayer.GetNextFeature()
while feat:
    geom = feat.GetGeometryRef()
    x = geom.GetX()
    y = geom.GetY()
    # compute pixel offset
    xOffset = int((x - xOrigin) / pixelWidth)
    yOffset = int((y - yOrigin) / pixelHeight)

    # create a string to print out
    s = feat.GetFieldAsString('ID') + ' '

    # loop through the bands
    for j in range(bands):
        band = img.GetRasterBand(j+1) # 1-based index
        # read data and add the value to the string
        data = band.ReadAsArray(xOffset, yOffset, 1, 1)
        value = data[0,0]
        s = s + '  ' + str(value) +'   '

    # print out and write file text
    print s
    s = s + '\n'
    file.write(s)

    # get the next feature
    feat.Destroy()
    feat = shpLayer.GetNextFeature()

# close the shapefile
shp.Destroy()
file.close()
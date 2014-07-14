#-------------------------------------------------------------------------------
# Name:        Unzip and delete (_num.tif) files in folder, Mosaic file, extract file
# Purpose:
#
# Author:      Hoa
#
# Created:     14/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import module
import zipfile, glob, os, arcpy
from arcpy.sa import *
# Working directory
output = r'C:\Users\Hoa\Desktop\mosaic\Unzip'
# Get *.zip file in path
fname = glob.glob(r'C:\Users\Hoa\Desktop\mosaic\*.zip')
print fname
#Unzip all files
for name in fname:
    source = zipfile.ZipFile(name, 'r')
    source.extractall(output)
# Delete *_num.tif file
filelist = glob.glob(output + '\*num.tif')

for file in filelist:
    os.remove(file)
# List new .tif file when removed _num.tif file
listnew = glob.glob( r'C:\Users\Hoa\Desktop\mosaic\Unzip\*.tif')
# Mosaic files
arcpy.MosaicToNewRaster_management(listnew, output, 'testmosa.tif', '',"16_BIT_SIGNED", '','1',"LAST", "FIRST")
# Extract file by mask
shpFile = r'C:\Users\Hoa\Desktop\demo\Results\RG_QT_CM_fix.shp'
Extract = ExtractByMask(r'C:\Users\Hoa\Desktop\mosaic\Unzip\testmosa.tif', shpFile)
arcpy.CopyRaster_management(Extract,r'C:\Users\Hoa\Desktop\mosaic\Unzip\extract_DEM.tif')
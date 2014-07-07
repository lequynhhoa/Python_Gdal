#-------------------------------------------------------------------------------
# Name:        splitting strings
# Purpose:
#
# Author:      Hoa
#
# Created:     04/07/2014
# Copyright:   (c) Hoa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys, ogr
# List country name and coordinates
country = 'VietNam 1, Lao 2, Campuchia 3: 100 200, 200 300, 300 400'
# Add a vertex to geometry
ring = ogr.Geometry(ogr.wkbLinearRing)
# Split country and coordinate
tmp = country.split(':')
names = tmp[0]
coords = tmp[1]
# Split coutry and id
namelist =  names.split(',')
for name in namelist:
    naid = name.split()
    na = str(naid[0])
    id = int(naid[1])
    print id, na
print '___***___\n'*2

# Split x, y coordinate
coordlist = coords.split(',')
for coord in coordlist:
    xy = coord.split()
    x = int(xy[0])
    y = int(xy[1])
    ring.AddPoint(x,y)
poly =  ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)

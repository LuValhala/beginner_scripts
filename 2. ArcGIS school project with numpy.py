"""
This script is working with ArcGIS arcpy library. It was also needed for a school subject (programming 1).
It takes the input points feature and creates a raster with it. After that, with numpy library, the raster dataset is 
converted to an array. A simple operation is used and then the process continues with array transfered to raster.
This whole script is a core part of arcgis tool, which is a GUI used to work in this desktop software
Ľuboš Valčo, november 2014
"""

import arcpy
import numpy
from arcpy import env 
from arcpy.sa import *
                                        
workspace = arcpy.GetParameterAsText(0)
body = arcpy.GetParameterAsText(1)
velkost_bunky = arcpy.GetParameterAsText(2)
atribut = arcpy.GetParameterAsText(3)
spline = arcpy.GetParameterAsText(4)   
raster = arcpy.GetParameterAsText(5)
sklon = arcpy.GetParameterAsText(6)
orientacia = arcpy.GetParameterAsText(7)
reclas1 = arcpy.GetParameterAsText(8)
reclas2 = arcpy.GetParameterAsText(9)
polygon1 = arcpy.GetParameterAsText(10)
polygon2 = arcpy.GetParameterAsText(11)
prienik = arcpy.GetParameterAsText(12)

env.workspace = workspace                                         

outSpline = Spline(body, atribut, velkost_bunky, "REGULARIZED", 0.1)
outSpline.save(spline)
  
array = arcpy.RasterToNumPyArray(spline)
for row in range(0,1):
    for col in range(0,1):
        array2 = array - numpy.amin(array) 
        raster2  = arcpy.NumPyArrayToRaster(array2)
        raster2.save(raster)

outSlope = Slope(raster, "DEGREE", 1)
outSlope.save(sklon)

outAspect = Aspect(raster)
outAspect.save(orientacia)


outReclass = Reclassify(sklon, "Value", RemapRange([[0,25,1],[25,100,"NODATA"]]))
outReclass.save(reclas1)

outReclass2 = Reclassify(orientacia, "Value", RemapRange([[0,90,"NODATA"],[90,270,1],[270,360,"NODATA"]]))
outReclass2.save(reclas2)

arcpy.RasterToPolygon_conversion(reclas1, polygon1)
arcpy.RasterToPolygon_conversion(reclas2, polygon2)
                              
inFeatures = [polygon1, polygon2]
intersectOutput = prienik
arcpy.Intersect_analysis(inFeatures, intersectOutput)

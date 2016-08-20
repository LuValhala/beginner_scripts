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
  
#pouzitie numpy na odcitanie najnizsej vysky od celej tabulky


#tool zo vstupnych bodov najde polygony sklonu do 25stupnov a orientacie na juzny polobzor

#aj ked to mozno velmi nedava zmysel, lebo vyjde to iste pri numpy alebo aj nie 
#ale matematicka zmena rastra sa da upravit pripadne, islo len o pokus

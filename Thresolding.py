
import arcpy
from arcpy import env
from arcpy.sa import *



#Allow output file to overwrite any existing file of the same name
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
#Inputs
arcpy.env.workspace = arcpy.GetParameter(0)
NDVICD= arcpy.GetParameter(1)
DEM=arcpy.GetParameter(2)
Post_Event= arcpy.GetParameter(3)
classes = 3

#Outputs
OutIso = 'Iso.tif'
Clip_CD='Clip_CD.tif'
inSQLClause1 = "Value > 15"
inSQLClause2 = "Value <> 2"
IsoEx = "IsoEx.tif"
Slope1 = 'SlopeMap.tif'
SlopeThresh = 'Slope_Thresh.tif'
Clip_Im = 'Post_Fin_Clip.tif'
Seg= 'SEGMENTED_CLIPPED_IMAGE.tif'
dsc = arcpy.Describe(Post_Event)
#Create Slope Map
outMeasurement = "DEGREE"
zFactor = "1"
outSlope = Slope(DEM, outMeasurement, zFactor)
outSlope.save(Slope1)

#Remove Slopes Less than 15
RemoveSlopes = ExtractByAttributes(Slope1, inSQLClause1)
RemoveSlopes.save(SlopeThresh)

#Clip Change Detection, Removing Slopes
arcpy.gp.ExtractByMask_sa(NDVICD,
                          SlopeThresh,
                          Clip_CD)

#Change Detection Clustering
outUnsupervised = IsoClusterUnsupervisedClassification(Clip_CD,classes)
outUnsupervised.save(OutIso)
attExtract = ExtractByAttributes(OutIso, inSQLClause2)
attExtract.save(IsoEx)

#Clip Post Event Image
outExtractByMask = ExtractByMask(Post_Event, IsoEx)
outExtractByMask.save(Clip_Im)

#Segment Image
arcpy.gp.SegmentMeanShift_sa(Clip_Im,
                             Seg,
                             "20",
                             "20",
                             "5",
                             "")




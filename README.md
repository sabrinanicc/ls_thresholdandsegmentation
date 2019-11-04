# ls_thresholdandsegmentation
ArcGIS Toolbox/ArcPy Script

The inputs for this tool are an NDVI change detection map, DEM and post-event RGB image. The tool uses the inputs to remove flat areas and areas of no-change from the post-event image. The clipped image is then segmented for use in the desired classifier. The final  image will be named  'SEGMENTED_CLIPPED_IMAGE.tif' and saved in the workspace defined. 


# Description
This toolbox can be used to threshold and segment RGB images for the purpose of landslide detection. This thresholding method removes flat areas and area of no-change in the imagery so as to reduce the amount of false-positives when classifying the imagery for landslide detection purposes. 

![TEST](Seg1.JPEG)

![TEST](Seg2.JPEG)


# Installation
Please refer to 'ls_eval' repository readme  for installation instructions. 

# ls_thresholdandsegmentation
The inputs for this tool are an NDVI change detection map, DEM and post-event RGB image.   The tool uses the inputs to remove flat areas and areas of no-change from the post-event image.   The clipped image is then segmented for use in the desired classifier. The final  image will be named  'SEGMENTED_CLIPPED_IMAGE.tif' and saved in the workspace defined. 

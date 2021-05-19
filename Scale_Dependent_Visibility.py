#Run on QGIS Python Console

#Same as 'Layer Properties > Rendering > Scale Depent Visibility
#Souce Layer
fn = "C:/Path/of/your/shapefile.shp"

#Add the layer to canvas
iface.addVectorLayer(fn, '', 'ogr')

#make a new variale
layer = iface.activeLayer()

#Set scale of the layer
layer.setScaleBasedVisibility(True)
layer.setMaximumScale(0)
layer.setMinimumScale(30001)

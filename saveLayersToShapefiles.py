# For all the layers in Qgsproject, .mapLayers = dict = {layer_x_id: layer_x, layer_y_id: layer_y, ....}
layers = QgsProject.instance().mapLayers()
layers = layers.values()

#Folder in which you want to save the shape files.
fn = 'C:/Users/WooY/Desktop/Grundkarte_LOKAL/BSK/V1.1/SHAPES/vonQGIS/'

#loop through all the layers.
for layer in layers: 
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn+layer.name()+'.shp', 'utf-8', driverName = 'ESRI shapefile', onlySelected = True)


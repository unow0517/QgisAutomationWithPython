#Run on QGIS python console

#Set Current Node
current_node = iface.layerTreeView().currentNode()

#mapLayers returns a dictionary structure, values returns the same values but in a list form
layers = QgsProject.instance().mapLayers().values()

#Loop to export all layers as qlr, qml, sld
for layer in layers:
    #set saving path
    path = 'C:/Path/That/You/Want/To/Save/the/File/' + str(layer.name())+'.qlr'
    #export QLR
    QgsLayerDefinition().exportLayerDefinition(path,[current_node])
    
    #set saving path
    pathqml = 'C:/Path/That/You/Want/To/Save/the/File/' + layer.name() + '.qml'
    pathsld = 'C:/Path/That/You/Want/To/Save/the/File/' + layer.name() + '.sld'
    #export QML,SLD
    layer.saveNamedStyle(pathqml)
    layer.saveSldStyle(pathsld)

## QLR contains a layer source pointer + style information, you can drag qlr file into a project,
## and it adds the layer with all its saved styling.
## A QML file isn't tied to any specific data source.
## QLR = Data + Style, QML = Style
## SLD contains layer properties information
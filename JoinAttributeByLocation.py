import processing

#QGIS Docs for JoinAttributeByLocation
#https://docs.qgis.org/3.16/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location

#list of the groups in Layer window
root = QgsProject.instance().layerTreeRoot()

##All layer objects in the second group
#backgroundLayer = root.children()[1].findLayers()
#print(root.children()[1].findLayers())

#layer object name when just one layer exist in the second group
backgroundLayerName = backgroundLayer[0].name()

#The name of first group 
# print(root.children()[0].name())


#number of layers in the first group
print(len(root.children()[0].findLayers()))

#print(root.children()[0])
#processing.algorithmHelp("native:joinattributesbylocation")

for layer in root.children()[0].findLayers():
   layerName = layer.name()
   processing.run("native:joinattributesbylocation",{
       'INPUT':layerName,
       'JOIN': backgroundLayerName,
       'PREDICATE' : 0,
       'JOIN_FIELDS' : ['name','schluessel'],
       'METHOD' : 2,
       'DISCARD_NONMATCHING' : False,
       'OUTPUT' :  'C:/Users/myname/Desktop/myFolder/' + layerName + '.shp',
       'NON_MATCHING' : 'TEMPORARY_OUTPUT'
   })
       

print('done')


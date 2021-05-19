#Run on QGIS Python Console

#Source layer
fn = 'C:/Path/of/Your/Shapefile.shp'

#Add layer on canvas
iface.addVectorLayer(fn,'','ogr')

#make a new variable layer
layer = iface.activeLayer()

#Make 'settings' objects, ex)settings12 == setting for text size 12
settings12 = QgsPalLayerSettings()
settings14 = QgsPalLayerSettings()
settings26 = QgsPalLayerSettings()
settings35 = QgsPalLayerSettings()

#find the column(field) for labeling
settings12.fieldName ='myFieldName'
settings14.fieldName ='myFieldName'
settings26.fieldName ='myFieldName'
settings35.fieldName ='myFieldName'

#Make textFormat objects.
textFormat12 = QgsTextFormat()
textFormat14 = QgsTextFormat()
textFormat26 = QgsTextFormat()
textFormat35 = QgsTextFormat()

#Set text size for each labeling
textFormat12.setSize(12)
textFormat14.setSize(14)
textFormat26.setSize(26)
textFormat35.setSize(35)

#apply text format for each setting
settings12.setFormat(textFormat12)
settings14.setFormat(textFormat14)
settings26.setFormat(textFormat26)
settings35.setFormat(textFormat35)

#label placement
# Placement: Cartographic = 6; Around point = 0; Offset from point = 1
settings12.placement = 1
settings14.placement = 1
settings26.placement = 1
settings35.placement = 1

#set X offset of label
settings12.xOffset = 0
settings14.xOffset = 0
settings26.xOffset = 0
settings35.xOffset = 0

#set Y offset of label
settings12.yOffset = 0
settings14.yOffset = 0
settings26.yOffset = 0
settings35.yOffset = 0

#data defined properties with expression
pc = QgsPropertyCollection()
pc.setProperty(QgsPalLayerSettings.LabelRotation,QgsProperty.fromExpression('360 - Drehwinkel'))
settings12.setDataDefinedProperties(pc)
settings14.setDataDefinedProperties(pc)
settings26.setDataDefinedProperties(pc)
settings35.setDataDefinedProperties(pc)

###make Rules based Labeling with setting object
rule12 = QgsRuleBasedLabeling.Rule(settings12)
rule14 = QgsRuleBasedLabeling.Rule(settings14)
rule26 = QgsRuleBasedLabeling.Rule(settings26)
rule35 = QgsRuleBasedLabeling.Rule(settings35)

rule12.setFilterExpression('\"SignaturNr\" =\'7800\'')
rule14.setFilterExpression('\"SignaturNr\" =\'4074\'')
rule26.setFilterExpression('\"SignaturNr\" =\'4074\'')
rule35.setFilterExpression('\"SignaturNr\" =\'4074\'')

rule12.setMinimumScale(1010)
rule12.setMaximumScale(0)


rule14.setMinimumScale(1010)
rule14.setMaximumScale(0)

rule26.setMinimumScale(1011)
rule26.setMaximumScale(2010)

rule35.setMinimumScale(2011)
rule35.setMaximumScale(5010)

###Add rules  
root = QgsRuleBasedLabeling.Rule(QgsPalLayerSettings())
root.appendChild(rule12)
root.appendChild(rule14)
root.appendChild(rule26)
root.appendChild(rule35)

#Make Labels with rules
rules = QgsRuleBasedLabeling(root)

#Make Null Symbol
renderer = QgsNullSymbolRenderer()
layer.setRenderer(renderer)

##Set labels and repaint
layer.setLabeling(rules)
layer.setLabelsEnabled(True)
layer.triggerRepaint()


layer.setName('NewLayerName')
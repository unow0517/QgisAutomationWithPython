#Run on QGIS Python Console
#Categorized Symbol Automationi

#Souce Layer
fn = "C:/Path/of/Your/Shapefile.shp"

#Open layer
layer = iface.addVectorLayer(fn, 'prefix', 'ogr')

#select active layer.
layer = iface.activeLayer()

##Symbol Setting##

symbol1 = QgsFillSymbol.createSimple(
    {'color':'#cccccc', 'outline_color': 'black'})

symbol2 = QgsFillSymbol.createSimple(
    {'color': '#6e6e6e', 'outline_color': 'black'})
    
symbol3 = QgsFillSymbol.createSimple(
    {'color': '#ff8080', 'outline_color': 'black'})

symbol4 = QgsFillSymbol.createSimple(
    {'color': '#FFFFFF', 'outline_style': 'dash'})

symbol5 = QgsFillSymbol.createSimple(
    {'color': '#FFFFFF', 'outline_color': 'black'})

symbol5 = QgsFillSymbol.createSimple(
    {'color': '#FFFFFF', 'outline_color': 'black'})
##Symbol Setting End##

#Make Categories with symbol
c1 = QgsRendererCategory('value1',symbol1,"legend1")
c2 = QgsRendererCategory('value2',symbol2,"legend2")
c3 = QgsRendererCategory('value3',symbol3,"legend3")
c4 = QgsRendererCategory('value4',symbol4,"legend4")
c5 = QgsRendererCategory('value5',symbol5,"legend5")

#NULL = with value 0, None = with no value
c6 = QgsRendererCategory(None,symbol6,"No value")

#Make renderer with target column
renderer = QgsCategorizedSymbolRenderer("column Name", [c1,c2,c3,c4,c5,c6])

#set layer renderer
layer.setRenderer(renderer)

#repaint layer
layer.triggerRepaint()

#rename layer
layer.setName('NewNameLayer')
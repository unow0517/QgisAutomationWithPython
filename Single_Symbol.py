#Source shape(polygon) file
fn ='fn = "C:/Path/of/Your/Shapefile.shp"'

#Add layer to canvas
iface.addVectorLayer(fn,'','ogr')

#Make a new variable
layer = iface.activeLayer()

#see which properties symbolLayers have
print(layer.renderer().symbol().symbolLayers()[0].properties())

#ex) {'border_width_map_unit_scale': '3x:0,0,0,0,0,0', 'color': '125,139,143,255', 'joinstyle': 'bevel', 'offset': '0,0', 'offset_map_unit_scale': '3x:0,0,0,0,0,0', 'offset_unit': 'MM', 'outline_color': '35,35,35,255', 'outline_style': 'solid', 'outline_width': '0.26', 'outline_width_unit': 'MM', 'style': 'solid'}

#Make Simple Fill Symbol with properties you want
symbol = QgsFillSymbol.createSimple({'color':'0,0,0,0','outline_color': '0,0,0,255'})

#render symbol you made 
layer.renderer().setSymbol(symbol)

#repaint layer
layer.triggerRepaint()

#rename layer
layer.setName('NewLayerName')

##Copy features from a layer to another layer with fields

#set variable layers
sourceLYR = QgsProject.instance().mapLayersByName('TRASSEN')[0]
destLYR = QgsProject.instance().mapLayersByName('Linie')[0]

#set sourceLYR field names in list 
attrs = sourceLYR.dataProvider().fields().toList()    

#edit mode
with edit(destLYR):
    #add AttrList to destLYR
    for attr in attrs:
        destLYR.addAttribute(attr)
    #select all features in sourceLYR
    sourceLYR.selectAll()
    #copy and paste
    iface.copySelectionToClipboard(sourceLYR)
    iface.pasteFromClipboard(destLYR)
    destLYR.removeSelection()

#QgsProject.instance().addMapLayer(destLYR)
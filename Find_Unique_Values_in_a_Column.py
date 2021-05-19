#Run on QGIS Python Console

#Souce Layer111
fn = "C:/Path/of/your/layer.shp"

#Add layer to canvas
iface.addVectorLayer(fn, 'NEU', 'ogr')

#make a new variable
layer = iface.activeLayer()

#The number of features of the layer.
fc = layer.featureCount()
print('How many Features?', fc)

#Make empty list for unique values
unique_value_list = []

#Put all the values in the column into the list.
for i in range(0,fc):
    feat = layer.getFeature(i)
    unique_value_list.append(feat['MyColumn'])

#Get unique values with set()
unique_value_set = set(unique_value_list)
print('Which unique values in MyColumn?', unique_value_set)

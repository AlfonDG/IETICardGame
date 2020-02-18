import xml.etree.cElementTree as tree

barajaEnemigo = tree.parse("../FicherosXML/IETI_Card_Game.xml")
print(barajaEnemigo)
CargarCartaRaizEnemigo = barajaEnemigo.getroot()
print(CargarCartaRaizEnemigo)

myBaraja = tree.parse("../FicherosXML/IETI_Card_Game.xml")
print()
CargarCartaRaiz = myBaraja.getroot()
print(CargarCartaRaiz)

import xml.etree.ElementTree as arbol

barajaEnemigo = arbol.parse("../FicherosXML/IETI_Card_Game.xml")
print(barajaEnemigo)
CargarCartaRaizEnemigo = barajaEnemigo.getroot()
print(CargarCartaRaizEnemigo)

myBaraja = arbol.parse("../FicherosXML/IETI_Card_Game.xml")
print(myBaraja)
CargarCartaRaiz = myBaraja.getroot()
print(CargarCartaRaiz)

from xml.dom import minidom

from Menu import menu

barajaEnemigo = minidom.parse("../FicherosXML/IETI_Card_Game.xml")
print(barajaEnemigo)
CargarCartaEnemigo = barajaEnemigo.getElementsByTagName("PlayerConfig")[0]
print(CargarCartaEnemigo.firstChild.data)

mybaraja = minidom.parse("../FicherosXML/IETI_Card_Game.xml")
print(mybaraja)
CargarMisCartas = mybaraja.getElementsByTagName("PlayerConfig")[0]
print(CargarMisCartas.firstChild.data)
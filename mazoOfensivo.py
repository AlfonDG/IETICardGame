import xml.etree.ElementTree as arbol

tree = arbol.parse("../FicherosXML/myBaraja.xml")
root = tree.getroot()
minataque=0
numminataque=0
baraja=[]
barajaAtaque=[]
barajaDefensa=[]

for card in root.findall('deck/card'):
    carta = []
    summonPoints = int(card.attrib['summonPoints'])
    tipo = str(card.attrib['type'])
    nombre = str(card.find('name').text)
    descripcion = str(card.find('description').text)
    ataque = int(card.find('attack').text)
    defensa = int(card.find('defense').text)
    minaAtaque = 0
    carta.append(summonPoints)
    carta.append(tipo)
    carta.append(nombre)
    carta.append(descripcion)
    carta.append(ataque)
    carta.append(defensa)
    baraja.append(carta)
baraja.sort(reverse=True)
barajaordatt=sorted(baraja, key=lambda h: h[4])
barajaordatt.reverse()
longitud=len(baraja)-1
for i in range (0,10):
    barajaAtaque.append(barajaordatt[i])
print(barajaAtaque)

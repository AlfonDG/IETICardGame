import xml.etree.ElementTree as arbol

#Parseamos el arbol mediante la librería ElementTree de xml y recorremos el árbol del fichero xml myBaraja.xml
tree = arbol.parse("myBaraja.xml")
root = tree.getroot()
minataque=0
numminataque=0
baraja=[]
barajaAtaque=[]
barajaDefensa=[]

#Creamos un for de manera que debemos de encontrar mediante el metodo findall los tags dentro de deck/card
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

#Ordenamos la variable barajaordatt y le decimos que comienze desde la posición de la lista 4
#En este caso será la puntuación más alta de ataque que será la primera del mazo en generar
barajaordatt=sorted(baraja, key=lambda h: h[4])
barajaordatt.reverse()
longitud=len(baraja)-1

#Creamos un for de manera que añadimos a la lista barajaAtaque la variable que guardará la otra lista barajaordatt
for i in range (0,10):
    barajaAtaque.append(barajaordatt[i])
print(barajaAtaque)
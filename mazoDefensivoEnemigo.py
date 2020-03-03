import xml.etree.ElementTree as arbol

#Parseamos el arbol mediante la librería ElementTree de xml y recorremos el árbol del fichero xml Enemigo.xml
tree = arbol.parse("Enemigo.xml")
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

#Ordenamos la variable barajaordedef y le decimos que comienze desde la posición de la lista 5
#En este caso será la puntuación más alta de defensa la primera del mazo en generar
barajaorddef=sorted(baraja, key=lambda h: h[5])
barajaorddef.reverse()
longitud=len(baraja)-1

#Creamos un for de manera que añadimos a la lista barajaDefensa la variable que guardará la otra lista barajaordedef
for i in range (0,10):
    barajaDefensa.append(barajaorddef[i])
print(barajaDefensa)
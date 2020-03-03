import xml.etree.ElementTree as arbol

doc = arbol.parse("../FicherosXML/myBaraja.xml")
element = doc.getroot()
element.findall('deck/card/name')
print(element)
minataque=0
numminataque=0
baraja=[]
for i in range (0,19):
    name = str(element.tag)
    attack = int(element.tag)
    if i<10:
        baraja.append(name)
        baraja.append(attack)
        if attack>minataque:
            minataque = attack
            numminataque = i
    elif i>10:
        if attack<minataque:
            continue
        elif attack>=minataque:
            baraja.append(name)
            baraja.append(attack)
            minataque = attack
            baraja.pop(numminataque)
            baraja.pop(numminataque)
            numminataque = i
print(baraja)

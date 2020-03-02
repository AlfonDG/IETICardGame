import xml.etree.ElementTree as arbol

tree = arbol.parse("myBaraja.xml")
root = tree.getroot()

minataque=0
numminataque=0
baraja=[]
for i in range (0,19):
    name=root.tag("name")[i]
    nombre=str(root.tag)
    attack = root.tag("attack")[i]
    ataque=int(root.tag)

 '''   if i<10:
        baraja.append(nombre)
        if ataque>minataque:
            minataque=ataque
            numminataque=i
    elif i>10:
        if ataque<minataque:
            continue
        elif ataque>=minataque:
            baraja.append(nombre)
            minataque=ataque
            baraja.pop(3)
print(baraja)'''
from xml.dom import minidom

barajaEnemigo = minidom.parse("/media/super/AlfonsoDominguezPracticas/FP informática Alfonso Grado Superior Primer y Segundo año 2019/M4-LENGUAJE DE MARCAS Y SISTEMAS DE GESTIÓN DE PRÁCTICAS/LOGROS/UF1/LOGRO 4/streamers.xml")
print(barajaEnemigo)
titulo = barajaEnemigo.getElementsByTagName("titulo")[0]
print(titulo.firstChild.data)
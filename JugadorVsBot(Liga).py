
'''Importamos la librería random'''

import random

'''Importamos la libreria pickle que lo que nos permite es guardar y restaurar el juego y retomarlo.'''

import pickle

fichero = open('jornada1.txt', 'a+')

vidas1 = 10

vidas2 = 10

#Número de bots que juegan por cada jornada.
bots=[0,0,0,0,0,0]

#Establecemos las vidas estáticas de cada jugador.
vidaslocal=5
vidasvisitante=0
liga=[] #Creamos una lista vacía la cual contendrá todas las cartas cargadas

#Organizamos la liga conforme cargaremos en una lista de tuplas las posiciones con el número del bot y jugador.

def organizarliga():
    i=0
    while(i<15):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        while (num2==num1):
            num2=random.randint(1,6)
        if (num1,num2) not in liga and (num2,num1) not in liga:
            liga.append((num1,num2))
            i+=1
organizarliga()
print(liga)

#Esta función definirá las variables para guardar las vidas dentro de los ficheros de jornadas 1 al 10.

def guardarVidas():
    if vidas1==0:
        fichero.write(vidaslocal)
        fichero.write(vidasvisitante)
    elif vidas2==0:
        fichero.write(vidaslocal)
        fichero.write(vidasvisitante)
cont=3
contjornadas=1

for i in liga:
    a, b = i
    print(f"El bot {a} va a jugar contra el bot {b}")
    #lucha
    if vidaslocal>vidasvisitante:
        bots[a-1]+=3
        bots[b-1]+=1
    elif vidasvisitante>vidaslocal:
        bots[a-1]+=1
        bots[b-1]+=3
    vidaslocal=vidas1 #vidas1 será la vida del jugador local
    vidasvisitante=vidas2 #vidas2 será la vida del jugador visitante
    if cont%3==0:
        fichero = open(f'jornada{contjornadas}.txt', 'w+')
        contjornadas += 1
    vidaslocal = f"{vidas1}|"
    vidasvisitante = f"{vidas2}|"
    guardarVidas()
    cont+=1
print(bots)

#Gardar Clasificación y puntuación de cada partida en el fichero clasificaciones.txt

ficheroClasificacion = open("clasificaciones.txt","w+")

ganarPartida = 3

perderPartida = 0

def guardarClasificacion():
    if ganarPartida == 3:
        ficheroClasificacion.write(str(ganarPartida))
    elif perderPartida == 0:
        ficheroClasificacion.write(perderPartida)
print(guardarClasificacion())

guardarPuntuacion = ganarPartida and perderPartida

#Creamos las variables que contendran el nombre de la partida guardada

nombrePartida = "partida1"

tiempoJuego = "99h:59min:59s"

puntuacion = guardarPuntuacion

guardarJuego = [nombrePartida,"|" + str(tiempoJuego),"|"+str(puntuacion)]

guardarPartida = open("PartidaGuardada.txt","w+")

#Guardamos el estado de la partida.

def guardarPartidaCompleta():

    for index in guardarJuego:
        guardarPartida.write(str(index))
    guardarPartida.close()

print(guardarPartidaCompleta())

#Restauramos el estado de la partida.

def recuperarPartidaCompleta():

    for index in guardarJuego:
        guardarPartida.read()

print(recuperarPartidaCompleta())
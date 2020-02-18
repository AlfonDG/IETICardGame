#Creación menu

menu = True

while menu:
    print("=================================")
    print("1. Cargar Cartas")
    print("2. Cargar cartas Enemigo")
    print("3. Cargar mazo aleatorio")
    print("4. Crear mazo ofensivo")
    print("5. Crear mazo defensivo")
    print("6. Crear mazo equilibrado")
    print("7. Crear mazo aleatorio Enemigo")
    print("8. Crear mazo ofensivo Enemigo")
    print("9. Cargar mazo defensivo Enemigo")
    print("10. Crear mazo equilibrado Enemigo")
    print("11. Luchar Jugador vs Jugador")
    print("12. Luchar Jugador vs Bot (arcade)")
    print("13. Luchar Jugador vs Bot (liga)")
    print("=================================")

if menu == "Cargar Cartas":
    print("Cargando Cartas.....")

elif menu == "Cargar cartas Enemigo":
    print("Generando cartas Enemigo....")

elif menu == "Cargar mazo aleatorio":
    print("Cargando un mazo aleatorio.....")

elif menu == "Crear mazo defensivo":
    print("Creando mazo defensivo......")

elif menu == "Crear mazo ofensivo":
    print("Creando mazo ofensivo......")

elif menu == "Crear mazo equilibrado":
    print("Creando mazo equilibrado......")

elif menu == "Crear mazo aleatorio Enemigo":
    print("Creando mazo aleatorio Enemigo")

elif menu == "Crear mazo ofensivo Enemigo":
    print("Creando mazo ofensivo Enemigo......")

elif menu == "Crear mazo equilibrado Enemigo":
    print("Creando mazo equilibrado Enemigo.......")

elif menu == "Luchar Jugador vs Jugador":
    print("Encontrando partida....... Partida Encontrada")

elif menu == "Luchar Jugador vs Bot (arcade)":
    print("Luchando Jugador vs Bot...... Partida Encontrada")

elif menu == "Luchar Jugador vs Bot (liga)":
    print("Luchando Jugador vs Bot......Partida Encontrada")


menu_seleccion = {}
menu_seleccion["1"] = "Cargar Cartas"
menu_seleccion["2"] = "Cargar cartas Enemigo"
menu_seleccion["3"] = "Cargar mazo aleatorio"
menu_seleccion["4"] = "Crear mazo ofensivo"
menu_seleccion["5"] = "Crear mazo defensivo"
menu_seleccion["6"] = "Crear mazo equilibrado"
menu_seleccion["7"] = "Crear mazo aleatorio Enemigo"
menu_seleccion["8"] = "Crear mazo ofensivo Enemigo"
menu_seleccion["9"] = "Cargar mazo defensivo Enemigo"
menu_seleccion["10"] = "Crear mazo equilibrado Enemigo"
menu_seleccion["11"] = "Luchar Jugador vs Jugador"
menu_seleccion["12"] = "Luchar Jugador vs Bot (arcade)"
menu_seleccion["13"] = "Luchar Jugador vs Bot (liga)"

while True:
    opciones = menu_seleccion.keys()
    for seleccion in opciones:
        print(seleccion, menu_seleccion[seleccion])

    seleccion=input("Por favor seleccione: ")

    if seleccion == "1":
        print("Cargando Cartas.....")
    elif seleccion == "2":
        print("Generando cartas Enemigo....")
    elif seleccion == "3":
        print("Cargando un mazo aleatorio.....")
    elif seleccion == "4":
        print("Creando mazo ofensivo......")
    elif seleccion == "5":
        print("Creando mazo ofensivo......")
    elif seleccion == "6":
        print("Creando mazo ofensivo......")
    elif seleccion == "7":
        print("Creando mazo aleatorio Enemigo")
    elif seleccion == "8":
        print("Creando mazo ofensivo......")
    elif seleccion == "9":
        print("Creando mazo ofensivo Enemigo......")
    elif seleccion == "10":
        print("Creando mazo equilibrado Enemigo.......")
    elif seleccion == "11":
        print("Encontrando partida....... Partida Encontrada")
    elif seleccion == "12":
        print("Luchando Jugador vs Bot...... Partida Encontrada")
    elif seleccion == "13":
        print("Luchando Jugador vs Bot......Partida Encontrada")
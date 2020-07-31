def mensaje():                       
    print("\n\n\t\t\t\t¡adios! 👊🏽")
    print("\n\n")


menu = """       
                               bienvenido a peso en otro planeta
           aqui podras averiguar cuanto pesas en cualquier planeta del sistema solar

                                 🌖      1. mercurio        🚀         👾        🌛
     💫           🌏                    2. venus                    ☄️     ☀️
                             👾          3. tierra       🌝                          🌙
                    🌒                  4. marte                       ⭐️
     ⭐️     🛸                  🚀      5. jupiter       🛸      ✨ 
                           ☀️             6. saturno                             🌑
             ✨                         7. urano               ☀️             
     ☄️                   🛰               8. neptuno     💫         🌎      🛰       
               🌛                🌑     9. pluton                                 ☄️  
                                                                🌒          🛸          🛰
escoge un planeta para averiguar tu peso: """

opcion = int(input(menu))
gravedad_terrestre = 9.8

    
def operacion():# esta es la funcion que cambia el peso digitador el usuario a el peso del planeta que el mismo usuario escogio
    
    peso_int = float(input("\n¿cuanto pesas? "))
    if peso_int > 0 and peso_int < 150:
       peso = (peso_int * gravedad)/gravedad_terrestre
       peso = str(round(peso, 2))
       print("¡genial!  tu peso en este planeta es de "+peso+" kg es increible no? 🚀")
       print("\n\n\n")
       mensaje()
    else:
        print("🤦‍♂️ ¡nooooo! 😩 ese peso no es valido, intenta otra vez")
        print("\n\n\n")
# fin de la funcion
# inicio condicionales para validar la opcion escogida por el usuario

if opcion == 1:
    print("\nescogiste mercurio 💥")
    gravedad = 3.7
    operacion()
elif opcion == 2:
    print("\nescogiste venus 💥")
    gravedad = 8.87
    operacion()
elif opcion == 3:
    print("\nescogiste tierra 💥")
    gravedad = 9.8
    operacion()
elif opcion == 4:
    print("\nescogiste marte 💥")
    gravedad = 3.7
    operacion()
elif opcion == 5:
    print("\nescogiste jupiter 💥")
    gravedad = 24.7
    operacion()
elif opcion == 6:
    print("\nescogiste saturno 💥")
    gravedad = 10.4
    operacion()
elif opcion == 7:
    print("\nescogiste urano 💥")
    gravedad = 8.8
    operacion()
elif opcion == 8:
    print("\nescogiste neptuno 💥")
    gravedad = 11.1
    operacion()
elif opcion == 9:
    print("\nescogiste pluton 💥")
    gravedad = 0.62
    operacion()
else: 
    print("🤦‍♂️ ¡nooooo! 😩 esa opcion no es valida intenta de nuevo eligiendo una opcion correcta ")
    print("\n\n\n")

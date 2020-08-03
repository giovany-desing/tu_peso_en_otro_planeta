def mensaje():       # este mensaje se imprimira cuando el usuario salga del programa               
    print("\n\n\t\t\t\t¡adios! 👊🏽")
    print("\n\n")

def menu():  # este es el menu principal del programa
    menu = """        
                                bienvenidos a peso en otro planeta
           aqui podras averiguar cuanto pesas en cualquier planeta del sistema solar

                                 🌖     1. mercurio        🚀         👾        🌛
     💫           🌏                    2. venus                    ☄️     ☀️
                             👾         3. tierra       🌝                          🌙
                    🌒                  4. marte                       ⭐️
     ⭐️     🛸                  🚀      5. jupiter       🛸      ✨ 
                           ☀️            6. saturno                             🌑
             ✨                         7. urano               ☀️                       💫
     ☄️                   🛰             8. neptuno     💫         🌎      🛰       
               🌛                🌑     9. pluton
                                        10. salir                                 ☄️  
                                                                🌒          🛸          🛰

    🚀 """
    print(menu)

def operacion(gravedad,planeta):# esta es la funcion que cambia el peso digitador el usuario a el peso del planeta que el mismo usuario escogio
    gravedad_terrestre = 9.8
    print(f'\nescogiste {planeta} 💥')
    peso_int = float(input("\n¿cuanto pesas? "))
    if peso_int > 0 and peso_int < 150:
       peso = (peso_int * gravedad)/gravedad_terrestre
       peso = str(round(peso, 2))
       print("\n\n¡G E N I A L!  tu peso en este planeta es de "+peso+" kg es increible no? 🚀")
       print("\n\n\n")
    else:
        print("🤦‍♂️ ¡N O O ! 😩 ese peso no es valido, intenta otra vez")
        print("\n\n\n")
# fin de la funcion

def main():
    opcion =0 
    while opcion != 10:
        menu()    
        try:
            opcion = int(input('\n\nselecciona una opcion: '))      
        except ValueError: # esta en una excepcion en caso de que el usuario digite una letra o un caracter diferente
            print(' ')
 # inicio condicionales para validar la opcion escogida por el usuario
        if opcion == 1:
            operacion(3.7,'mercurio')
        elif opcion == 2:
            operacion(8.87,'venus')
        elif opcion == 3:
            operacion(9.8,'tierra')
        elif opcion == 4:
            operacion(3.7,'marte')
        elif opcion == 5:
            operacion(24.7,'jupiter')
        elif opcion == 6:
            operacion(10.4,'saturno')
        elif opcion == 7:
            operacion(8.8,'urano')
        elif opcion == 8:
            operacion(11.1,'neptuno')
        elif opcion == 9:
            operacion(0.62,'pluton')
        elif opcion == 10:
            mensaje()
            break
        else: 
            print("🤦‍♂️ ¡N O O O! 😩 esa opcion no es valida intenta de nuevo eligiendo una opcion correcta ")
            print("\n\n\n")

   
if __name__ == "__main__":
    main()
    
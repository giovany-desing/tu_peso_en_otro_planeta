class User:
    def __init__(self, weight_user):
        self.weight_user = weight_user

    def live_time(self):
        print(f"Si estuvieras en este planeta sin traje espacial sobreviviras unos segundos")
        print()
class Planet:
    def __init__(self, gravity, planet_name):
        self.gravity = gravity
        self.planet_name = planet_name
      

    def welcome_to_planet(self):
        print(f'\nestas en el planeta {self.planet_name}, la gravedad de este planeta es de {self.gravity} m/s²💥')
        print()

class Menus:
    def __init__(self):
        self.menu_planet = """        
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

        self.bye = "\n\n\t\t\t\t¡adios! 👊🏽\n\n"
        
    def show_menu(self):
        print(self.menu_planet)
    def goodbye(self):
        print(self.bye)

class Operation:
    def __init__(self):
        self.earth_gravity = 9.8

    def calculator(self,user,planet):
        self.peso = round((user.weight_user * planet.gravity)/self.earth_gravity, 1)
        print(f"\n\n¡G E N I A L!  tu peso en el planeta {planet.planet_name} es de {self.peso } kg es increible no? 🚀")
        print()
    
class Result():
    def __init__(self):
        self.weight = 0
        
    def main(self, planet):
        calculate_weight = Operation()
        
        while True:
            try:
                self.weight = int(input('Ingresa tu peso '))
                if self.weight > 0:
                    user = User(self.weight)
                    calculate_weight.calculator(user,planet)
                    user.live_time()
                    break
                else:
                    print("🤦‍♂️ ¡N O O ! 😩 ese peso no es valido, intenta otra vez")
                    print("\n\n\n")
            except ValueError:
                print("🤦‍♂️ ¡N O O ! 😩 ese peso no es valido, intenta otra vez")
                print("\n\n\n")

class App():
    def __init__(self):
        self.option = 0
    def result(self):
        result = Result()
        menus = Menus()
        while self.option != 10:
            menus.show_menu()
            try:
                self.option = int(input('\n\nselecciona una opcion: '))
            except ValueError:
                print(' ')
            if self.option == 1:
                planet = Planet(3.7,'Mercurio')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 2:
                planet = Planet(8.87,'venus')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 3:
                planet = Planet(9.8,'tierra')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 4:
                planet = Planet(3.7,'marte')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 5:
                planet = Planet(24.7,'jupiter')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 6:
                planet = Planet(10.4,'saturno')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 7:
                planet = Planet(8.8,'urano')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 8:
                planet = Planet(11.1,'neptuno')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 9:
                planet = Planet(0.62,'pluton')
                planet.welcome_to_planet()
                result.main(planet)
            elif self.option == 10:
                menus.goodbye()
                break
            else:
                print("🤦‍♂️ ¡N O O O! 😩 esa opcion no es valida intenta de nuevo eligiendo una opcion correcta ")
                print("\n\n\n")


if __name__ == "__main__":
    app = App()
    app.result()

    
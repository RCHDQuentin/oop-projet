class Cli:
    def __init__(self):
        print('===Welcome To The Library System===')

    def start(self):
        print(
                """
Bienvenue que désirez vous faire ? 
    1 Chercher un livre
    2 Choisir un utilisateur
    3 Emprunter un livre
    4 Gestion des livres
    5 Gestion des utilisateurs
    6 Exit
                """
        )

        print ('===>', end=" ")
        action = input()

        match action:
            case '6':
                return False
            case _:
                return True

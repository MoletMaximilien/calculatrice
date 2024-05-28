# Fonctions pour chaque opération
def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur : Division par zéro"

# Fonction principale de la calculatrice
def calculatrice():
    print("Bienvenue dans la calculatrice")
    print("Choisissez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    # Lire le choix de l'utilisateur
    choix = input("Entrez votre choix (1/2/3/4) : ")

    # Vérifier si le choix est valide
    if choix in ['1', '2', '3', '4']:
        # Lire les deux nombres pour l'opération
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides.")
            return

        # Effectuer l'opération choisie
        if choix == '1':
            print(f"Résultat : {num1} + {num2} = {addition(num1, num2)}")
        elif choix == '2':
            print(f"Résultat : {num1} - {num2} = {soustraction(num1, num2)}")
        elif choix == '3':
            print(f"Résultat : {num1} * {num2} = {multiplication(num1, num2)}")
        elif choix == '4':
            resultat = division(num1, num2)
            print(f"Résultat : {num1} / {num2} = {resultat}")

    else:
        print("Erreur : Choix invalide")

# Exécuter la calculatrice
if __name__ == "__main__":
    calculatrice()
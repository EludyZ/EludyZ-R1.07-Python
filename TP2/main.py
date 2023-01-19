# Exercice 1 : variables/affectation

def swap():
    x = int(input("entrez x: "))
    y = int(input("entrez y: "))

    print(f"avant permutation  \n x : {x} \n y: {y}")

    # méthode algorithmique classique
    temp = x
    x = y
    y = temp

    print(f"aprés une première permutation  \n x : {x} \n y: {y}")

    # méthode python

    x, y = y, x

    print(f"aprés une seconde permutation  \n x : {x} \n y: {y}")


# swap()

# Exercice 2 : Année de naissance

def birth():
    age = int(input("Donnez votre age :"))
    naissance = 2023 - age

    print(f"Votre annee de naissance est : {naissance}")


# birth()

# Exercice 3 : Echange de trois valeurs
def threeSwap():
    a = input("Entrez la premiere  valeur : ")
    b = input("Entrez la deuxieme  valeur : ")
    c = input("Entrez la troisieme valeur : ")

    print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
    print("Permutation: a ==> b, b ==> c, c ==> a")

    a, b, c, = b, c, a

    print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)


# threeSwap()

# Exercice 4 : Fondue
def fondue():
    base = 4
    fromage = 800
    eau = 2
    ail = 2
    pain = 400

    nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
    fromage *= nbConvives / base
    eau *= nbConvives / base
    ail *= nbConvives / base
    pain *= nbConvives / base
    print(
        f"Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :\n-{fromage}gr de fromage\n-{eau}dl d'eau\n-{ail} gousse(s) d'ail\n-{pain}gr de pain")


# fondue()

# Exercice 5 : expressions conditionnelles

def cond():
    entier = int(input("entrez un nombre entier:"))
    if (entier < 0):
        msg = "négatif"
        if (entier % 2 == 0):
            msg += " pair"
        else:
            msg += " impair"
    elif entier > 0:
        msg = "positif"
        if (entier % 2 == 0):
            msg += " pair"
        else:
            msg += " impair"
    else:
        msg = "zéro (et il est pair)"

    print(f"{entier} est un nombre {msg}")


# cond()


# Exercice 6 :
def random():
    import random
    random = random.randint(1, 100)

    if random < 50:
        print("Pile!")
    else:
        print("Face!")


# random()

# Exercice 7 :
def random2():
    import random
    random = random.randint(1, 150)

    if random < 50:
        print("Face!")
    else:
        print("Pile!")


# random2()

# Exercice 8 : intervalle
def intervalle():
    import random
    x = int(input("Entre un entier: "))
    if (2 <= x < 3) or (0 < x <= 1) or (-10 <= x <= -2):
        print("x appartient à I")
    else:
        print("x n'appartient pas à I")

# intervalle()

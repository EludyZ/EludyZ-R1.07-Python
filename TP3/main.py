# Exercice 1 : Choix de la structure itérative
def sumFact():
    N = int(input())
    somme = 0
    for i in range(1, N + 1, 1):
        print(f"{i}")
        somme += i
    print(f"{somme}")


def enterRightNumberBitch():
    n = 0
    while n != 100:
        n = int(input())
    print("Eh bah enfin FDP")


# enterRightNumberBitch()

def count():
    count10 = 0
    count1015 = 0
    count15 = 0

    for i in range(0, 10, 1):
        n = -1
        while (n < 0 or n > 20):
            n = int(input("saisr un entier entre 0 et 20"))
        if n < 10:
            count10 += 1
        elif n < 15:
            count1015 += 1
        else:
            count15 += 1

    print(
        f"nb de valeurs < 10 {count10} \n nb de valeurs entre 10 et 15 {count1015} \n nb de valeurs supérieures {count15}")


# count()

# Exercice 2 : Compte à rebours
def counter():
    import time
    n = int(input())

    while n != -1:
        print(f"{n}")
        n -= 1
        time.sleep(0.2)
# counter()

def mystery():
    from random import randint
    count = 1
    x = randint(1, 100)
    print("vous devez trouver un nombre entre 0 et 100")
    var = int(input("saisir un entier"))
    while var != x:
        if var > x:
            print(f"{var} est plus grand que le nombre à trouver")
        else:
            print(f"{var} est plus petit que le nombre à trouver")
        count += 1
        var = int(input("saisir un entier"))

    print(f"vous avez trouver {x} en {count} essai")
mystery()
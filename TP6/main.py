# EXERCICE 1:
def ex1():
    L1 = [0] * 3
    print(L1)
    print(type(L1))
    print(id(L1))

    for i in L1:
        print(type(i))
        print(id(i))

    L1[1] += 1
    print(L1)
    print(type(L1))
    print(id(L1))

    for i in L1:
        print(type(i))
        print(id(i))
ex1()

# EXERCICE 2:
def ex2():
    def ajouter_elt(lst, elt):
        lst.append(elt)
        return lst

    lst1 = [0, 1, 2]
    lst2 = ajouter_elt(lst1, len(lst1))

    print(lst1)
    print(type(lst1))
    print(id(lst1))

    print(lst2)
    print(type(lst2))
    print(id(lst2))

# ex2()

# EXERCICE 3: Valeur par défaut et référence
"""
a) Le résultat de l'instruction print(ajouter_elt()) serait [0, 1, 2, 3], car la fonction utilise les valeurs par défaut pour les arguments lst et elt.
b) Si l'on répète l'instruction print(ajouter_elt()), on remarque que le résultat est toujours [0, 1, 2, 3], même si on ajoute une nouvelle valeur à la
liste. Cela est dû au fait que les valeurs par défaut des arguments sont créées une seule fois lors de la définition de la fonction et sont ensuite 
utilisées comme références pour toutes les appels de la fonction. En utilisant la fonction id() on peut constater que les références des objets listes 
sont les mêmes.
c) La fonction ajouter_carac peut être définie comme suit:
"""
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt
"""
d) Le résultat de l'instruction print(ajouter_carac()) serait "abcd"
e) Si l'on répète l'instruction print(ajouter_carac()), on remarque que le résultat est toujours "abcd". Cela est dû au fait que les valeurs par défaut
des arguments sont créées une seule fois lors de la définition de la fonction et sont ensuite utilisées comme références pour toutes les appels de la fonction.
En utilisant la fonction id() on peut constater que les références des objets chaine sont les mêmes.
"""

# EXERCICE 4:

def ex4():

    # a
    import random

    def generer(nbr, vmin, vmax):
        return [random.randint(vmin, vmax) for _ in range(nbr)]

    def combienInferieur(table, vseuil):
        return sum(1 for v in table if v < vseuil)

    # b
    nb = int(input("Combien de nombres voulez-vous générer ? "))
    vmin = int(input("Entrez la valeur minimale : "))
    vmax = int(input("Entrez la valeur maximale : "))
    tab = generer(nb, vmin, vmax)
    tab.sort()
    print(tab)

    seuil = input("Voulez-vous préciser le seuil ? (O/N) ")
    if seuil.upper() == "O":
        vseuil = int(input("Entrez la valeur du seuil : "))
    else:
        vseuil = 30

    total = combienInferieur(tab, vseuil)
    print(f"Il y en a {total} inférieurs à {vseuil}")
ex4()

# EXERCICE 5: : Palindrome - version avec les fonctions
def Palindrome():
    def nettoyer_texte(chaine):
        chaine = chaine.lower()
        chaine = "".join(x for x in chaine if x.isalpha())
        return chaine

    def est_palindrome(chaine):
        chaine_nettoyee = nettoyer_texte(chaine)
        return chaine_nettoyee == chaine_nettoyee[::-1]

    chaine = input("Entrez un mot ou une phrase : ")
    if est_palindrome(chaine):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")
# Palindrome()

# EXERCISE 1: Operations sur les chaines de caractères
def nomprenom():
    print("Entrez le nom et le prénom de la première personne :")
    prenom1 = input("Prénom : ")
    nom1 = input("Nom : ")

    print("Entrez le nom et le prénom de la seconde personne :")
    prenom2 = input("Prénom : ")
    nom2 = input("Nom : ")

    if nom1 < nom2:
        print(prenom1.capitalize() + " " + nom1.upper())
        print(prenom2.capitalize() + " " + nom2.upper())
    elif nom2 < nom1:
        print(prenom2.capitalize() + " " + nom2.upper())
        print(prenom1.capitalize() + " " + nom1.upper())
    else:
        if prenom1 < prenom2:
            print(prenom1.capitalize() + " " + nom1.upper())
            print(prenom2.capitalize() + " " + nom2.upper())
        else:
            print(prenom2.capitalize() + " " + nom2.upper())
            print(prenom1.capitalize() + " " + nom1.upper())
# nomprenom()

# EXERCISE 2: Notes
def Notes():
    notes = []
    coefs = []

    for i in range(5):
        user_input = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ")
        note, coef = user_input.split(" ")
        notes.append(float(note))
        coefs.append(int(coef))

    moyenne = sum([notes[i] * coefs[i] for i in range(5)]) / sum(coefs)

    if moyenne > 10 and all(note >= 8 for note in notes):
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")


#Notes()

# EXERCISE 3: Palindromes
def Palindromes():
    user_input = input("Entrez un mot ou une phrase : ")
    cleaned_input = ""
    for char in user_input:
        if char.isalpha():
            cleaned_input += char.lower()
    if cleaned_input == cleaned_input[::-1]:
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

# Palindromes()




# EXERCISE 4: La monnaie (TD1)

def Monnaie():
    somme = int(input("Entrez une somme d'argent : "))
    input_somme = somme

    b100 = somme // 100
    somme = somme % 100

    b50 = somme // 50
    somme = somme % 50

    b10 = somme // 10
    somme = somme % 10

    p2 = somme // 2
    somme = somme % 2

    p1 = somme

    print(
        f"{input_somme} euros, c'est donc {b100} billets de 100, {b50} de 50, {b10} de 10, {p2} pièces de 2 et {p1} pièce 1.")
#Monnaie()

# EXERCICE 5: Fiche de paye (TD2)

def FicheDePaye():
    heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = float(input("Entrez le salaire horaire : "))

    salaire_base = heures_travaillees * salaire_horaire

    if heures_travaillees > 200:
        salaire_supplementaire = (heures_travaillees - 200) * (salaire_horaire * 0.5) + (40 * salaire_horaire * 0.25)
    elif heures_travaillees > 160:
        salaire_supplementaire = (heures_travaillees - 160) * (salaire_horaire * 0.25)
    else:
        salaire_supplementaire = 0

    salaire_total = salaire_base + salaire_supplementaire
    print(f"Le salaire total est de {salaire_total} euros.")
# FicheDePaye()

# EXERCICE 6: Chaînes de caractères (TD4)

def Char():
    T = input("Entrez une chaîne de caractères : ")

    taille_T = 0
    for caractere in T:
        taille_T += 1
    print(f"La taille de la chaîne T est : {taille_T}")

    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = 0
    for caractere in T:
        if caractere in voyelles:
            nombre_voyelles += 1

    pourcentage_voyelles = nombre_voyelles / taille_T * 100
    print(f"Le pourcentage de voyelles dans T est : {pourcentage_voyelles}%")

    position_wagon = -1
    for i in range(taille_T - 4):
        if T[i] == "w" and T[i + 1] == "a" and T[i + 2] == "g" and T[i + 3] == "o" and T[i + 4] == "n":
            position_wagon = i
            break
    if position_wagon != -1:
        print(f"La chaîne 'wagon' est une sous-chaîne de T, elle commence à la position {position_wagon}")
    else:
        print("La chaîne 'wagon' n'est pas une sous-chaîne de T.")

    occurrences_wagon = 0
    for i in range(taille_T - 4):
        if T[i] == "w" and T[i + 1] == "a" and T[i + 2] == "g" and T[i + 3] == "o" and T[i + 4] == "n":
            occurrences_wagon += 1
    print(f"Il y a {occurrences_wagon} occurrences de la chaîne 'wagon' dans T.")
#Char()

# EXERCICE 7: Dernière modification
def LastEdit():
    import os
    from datetime import datetime

    file1 = input("Entrez le nom du premier fichier : ")
    file2 = input("Entrez le nom du second fichier : ")

    if os.path.isfile(file1):
        file1_size = os.path.getsize(file1)
        file1_time = os.path.getmtime(file1)
        print(
            f"Le fichier {file1} existe, sa taille est de {file1_size} octets, et sa dernière modification était le {datetime.fromtimestamp(file1_time)}")
    else:
        print(f"Le fichier {file1} n'existe pas.")

    if os.path.isfile(file2):
        file2_size = os.path.getsize(file2)
        file2_time = os.path.getmtime(file2)
        print(
            f"Le fichier {file2} existe, sa taille est de {file2_size} octets, et sa dernière modification était le {datetime.fromtimestamp(file2_time)}")
    else:
        print(f"Le fichier {file2} n'existe pas.")
# LastEdit()

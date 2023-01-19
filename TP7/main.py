# Exercice 1
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Veuillez entrer le nom du dossier comme argument.")
        sys.exit()
    else:
        folder_name = sys.argv[1]
        if os.path.isdir(folder_name):
            for filename in os.listdir(folder_name):
                print(filename)
        else:
            print(f"Le dossier {folder_name} n'existe pas.")

print("*******************************************")
print("*DEVINEZ LE NOMBRE ET SOYEZ LE PLUS FORT !*")
print("*******************************************")
import random
nombre_secret = random.randint(0, 100)


def correction():
    n = int(input("Veillez entrer un nombre s'il vous plait: "))
    while n > 100:
        n = int(input("Le nombre est trop grand. Entrez un autre nombre s'il vous plait: "))
    return n

def nombre_magic(nombre_secret):
    i= 0
    while i < 10:
        nbre_utilisateur = correction()
        i+= 1
        if nbre_utilisateur < nombre_secret:
            print("Trop petit, essaie encore !")
            print(f"Il te reste {10 - i} essai(s)")
        elif nbre_utilisateur > nombre_secret:
            print("Trop grand, essaie encore !")
            print(f"Il te reste {10 - i} essai(s)")
        else:
            print(f"Bravo tu as trouvé le bon nombre en {i} essai(s) !")
            return
    print(f"Tu as utilisé tes 10 essais, le bon nombre était {nombre_secret}.")


nombre_magic(nombre_secret)

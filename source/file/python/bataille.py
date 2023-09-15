import random
import time


#-------- Interface files ------------------

def creer_file():
    return []

def enfiler(file,val):
    file.append(val)
    return file

def defiler(file):
    return file.pop(0)

def est_vide(file):
    return file==[]

#----------- Construction du jeu de cartes ------------

def cree_paquet(n=32):
    """crée un paquet de carte;
    - n est le nombre de cartes;
    """
    P=list()
    couleurs = ('coeur','carreau','pique','trefle')
    nb_cartes_couleur = n // 4
    if n == 52:
        for i in range(1,nb_cartes_couleur+1):
            for j in range(4):
                P.append((i,couleurs[j]))
    elif n == 32:
        for i in range(1,nb_cartes_couleur+1):
            for j in range(4):
                P.append((i+6,couleurs[j]))
    return P

def melanger(paquet):
    """Mélange la liste de cartes du paquet avec la méthode shuffle de la bibliothèque random"""
    random.shuffle(paquet)

def distribuer(paquet):
    paquet_A = creer_file()
    paquet_B = creer_file()
    while paquet!=[]:
        carte=paquet.pop(0)
        enfiler(paquet_A,carte)
        carte=paquet.pop(0)
        enfiler(paquet_B,carte)
    return paquet_A,paquet_B

def jouer(tasA,tasB):
    tapis=creer_file()
    while not est_vide(tasA) and not est_vide(tasB):
        a = defiler(tasA)
        b = defiler(tasB)
        #time.sleep(0.5)
        print("A:",a,"B:",b)
        if a[0] > b[0]:
            tasA = enfiler(tasA,a)
            tasA = enfiler(tasA,b)
            while not est_vide(tapis):
                tasA = enfiler(tasA,defiler(tapis))
            print("A remporte la manche:",len(tasA),"cartes")
        elif a[0] < b[0]:
            tasB = enfiler(tasB,a)
            tasB = enfiler(tasB,b)
            while not est_vide(tapis):
                tasB = enfiler(tasB, defiler(tapis))
            print("B remporte la manche",len(tasB),"cartes")
        else:
            # il y a bataille !
            tapis = enfiler(tapis, a)
            tapis = enfiler(tapis, b)
            tapis = enfiler(tapis, defiler(tasA))
            tapis = enfiler(tapis, defiler(tasB))
            print("BATAILLE!",tapis)
    # on sort de la boucle, on affiche le vainqueur
    if est_vide(tasA):
        print("A a perdu ! B gagne")
    else:
        print("B a perdu ! A gagne")


# Programme de jeu
paquet = cree_paquet()
melanger(paquet)
print(paquet)
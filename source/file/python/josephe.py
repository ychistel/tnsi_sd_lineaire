"""
Le reste d'une armée encore composée de 40 soldats, ayant perdu la bataille, refuse de se rendre à l'ennemi et préfère mettre fin à leurs jours eux-mêmes. L'historien Josephe, n'approuvant pas le suicide car déshonnorant tout combattant qui s'y soumet propose une alternative. Il explique, que tous les hommes seront disposés en cercle, qu'il chosira au hasard le début de la funeste exécution et qu'ensuite un homme sur trois sera exécuté jusqu'au dernier qui devra se suicider. Seul le survivant sera déshonnoré.

N'ayant nullement envie d'être exécuté ni de se suicidé, il cherche la position qui lui permettra d'être le dernier survivant après avoir désigné le début de la ronde meurtrière.

Comment déterminer la position qui sera la dernière ?

Écrire un algorithme qui résout le problème.
"""

class File:
    """
    Création d'une structure de file basée sur les listes Python
    Interface:
    - est_vide()
    - enfiler(valeur)
    - defiler()
    """
    def __init__(self):
        self.contenu = []
    
    def est_vide(self):
        return self.contenu == []

    def enfiler(self, valeur):
        self.contenu.append(valeur)

    def defiler(self):
        sommet = self.contenu.pop(0)
        return sommet
    
def creer_file():
    return File()

"""Résolution du problème avec une file représentant les 40 soldats et l'empereur."""

def suite_josephe(n,k):
    F = creer_file()
    for i in range(n):
        F.enfiler(i + 1)

    while not F.est_vide():
        for i in range(1,k):
            epargne = F.defiler()
            F.enfiler(epargne)
        derniere_position = F.defiler()

    return derniere_position

for i in range(21,32):
    print(suite_josephe(i,3))

.. TNSI
   Exercices sur les listes chainées
   
.. toctree
   :maxdepth: 1

Exercices sur les listes
========================

On redonne l'interface qui sera utilisée dans les exercices.

- Le constructeur ``creer_liste()`` qui crée une liste vide, c'est à dire un tuple vide;
- L'opérateur ``inserer(liste, element)`` qui ajoute un élément en tête de liste;
- Les accesseurs ``tete(liste)`` qui renvoie la tête de liste (sans le supprimer) et ``queue(liste)`` qui renvoie la liste sans son premier élément;
- L'accesseur ``est_vide(liste)`` qui teste si la liste est vide.

Exercice 1
----------

1. On donne la représentation d'une liste (chainée):

   .. image:: ../img/liste_chainee_1.svg
      :align: center
      :width: 360px
 
   Donner la suite d'instruction en Python pour créer cette liste (chainée).
2. En utilisant la liste ``L1``, créer les différentes listes  de l'illustration ci-dessous.

   .. image:: ../img/liste_chainee_2.svg
      :align: center
      :width: 360px

Exercice 2
----------

On donne une implémentation de liste avec les tuples.

.. code:: python
   
   def creer_liste():
       return ()

   def est_vide(liste):
      return liste == ()

   def inserer(liste, element):
      return (element, liste)

   def tete(liste):
      assert not est_vide(liste), "tête, liste vide !"
      element, _ = liste
      return element

   def queue(liste):
      assert not est_vide(liste), "queue, liste vide !"
      _,queue = liste
      return queue

1. Créer et afficher la liste ``L1`` de l'exercice précédent.
2. On souhaite créer une fonction ``afficher(liste)`` qui prend en paramètre une liste et affiche la liste sous forme de chaine:
   
   - chaque valeur sera écrite entre crochets
   - les valeurs seront reliées par des flèches "->".
   
   Voici le début du code de la fonction à compléter:

   .. code:: python

      def afficher(liste):
          chaine = ""
          while not est_vide(liste):
             tete, liste = ...
             chaine += "[" + ... + "]->"
          chaine += ...
          return ...

Exercice 3
----------

On souhaite ajouter quelques fonctions pour agir sur une liste chainée.

1. La fonction ``longueur`` prend en paramètre une liste et renvoie le nombre d'éléments de la liste. Coder cette fonction sachant que si la liste est vide, la longueur est égale à 0.
2. La fonction ``atteint`` prend en paramètres une liste et un nombre entier positif. La fonction renvoie le nombre de la liste situé à la position indiquée par le nombre entier saisi en argument. On gèrera le cas ou la position est supérieure à la longueur de la liste pour éviter une erreur. La tête de la liste a pour position 0. Coder en Python la fonction.

Exercice 4
----------

Soit L une liste chainée qui contient les valeurs ``Bob``, ``Alice``, ``Patrick``, ``Gary`` et ``Carlo``. On considère que le nom ``Bob`` est la tête de la liste et que l'ordre est respecté.

1. Créer en Python cette liste chainée.
2. La fonction ``renverse`` prend en paramètre une liste et renverse les valeurs de la liste. La tête de liste devient la dernière valeur de la liste. La fonction renvoie une liste chainée.
   
   a. Coder la fonction ``renverse``.
   b. Créer la liste chainée K en renversant la liste L.
   
3. La fonction ``inserer_fin`` prend en paramètre une liste et une valeur à insérer en fin de liste. La fonction renvoie la liste chainée avec la valeur insérée en fin de liste. On peut utiliser l'algorithme suivant pour notre fonction:

   .. code:: text
      
      1. créer une liste tmp contenant la valeur à insérer
      2. renverser la liste qui doit accueillir la nouvelle valeur
      3. insérer les éléments de la liste renversée dans la liste tmp.

Coder la fonction et insérer une nouvelle valeur en fin de liste.
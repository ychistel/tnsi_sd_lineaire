Exercices sur les tableaux
==========================

Exercice 1
-----------

On donne le programme Python ci-dessous:

.. code:: python
   
   >>> a=3
   >>> b=5
   >>> t=(a,b)
   >>> a=a+1
   >>> print(t)
   
Quel est l'affichage obtenu à l'issu de ce programme ? Justifier.

Exercice 2
-----------

Écrire une fonction ``recherche_min`` qui prend en paramètre un tableau de nombres non trié ``t``, et qui renvoie
l’indice de la première occurrence du minimum de ce tableau. Les tableaux seront représentés sous forme de liste
Python. Voici quelques exemples de la fonction:

.. code:: python

   >>> recherche_min([5])
   0
   
   >>> recherche_min([2,4,1])
   2
   
   >>> recherche_min([5,3,2,2,4])
   2

Exercice 3
-----------

On considère la fonction ``separe`` ci-dessous qui prend en argument un tableau ``tab`` dont les éléments sont des 0 et des 1 et qui sépare les 0 des 1 en les plaçant en début de tableau et les 1 à la suite.

.. code:: python

   def separe(tab):
      i = 0
      j = ...
      while i < j:
         if tab[i] == 0:
            i = ...
         else:
            tab[i], tab[j] = ...
            j = ...
      return tab

Compléter la fonction ``separe`` ci-dessus. Quelques exemples de la fonction :

.. code:: python

   >>> separe([1,0,1,0,1,0,1,0])
   [0,0,0,0,1,1,1,1]
   
   >>> separe([1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0])
   [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]

.. TNSI
   Exercices sur les files

.. toctree::
   :maxdepth: 1
   
Exercices sur les files
=======================

Pour les exercices ci-dessous, on utilise l'interface de **file** rappelée ci-dessous:

- ``creer_file()`` fonction qui crée une file vide.
- ``est_vide(F)`` fonction qui prend en paramètre une file F et renvoie un booléen permettant de savoir si la file est vide ou non.
- ``enfiler(F,e)`` fonction qui prend en paramètre une file F et un élément e et l'ajoute à la file.
- ``defiler(F)`` fonction qui prend en paramètre une file F et renvoie la tête de la file en la supprimant.

Exercice 1
----------

On donne ci-dessous la représentation d'une file F dans différents états. Donner les instructions en Python qui permettent d'obtenir ces différents états de la file F.

.. image:: ../img/file_ex1.svg
   :align: center
   :width: 300px
   
Exercice 2
----------

1. En utilisant les listes Python, créer une implémentation de l'interface de file.

.. code:: python

   def creer_file():
       ...
   
   def est_vide(file):
       ...
   
   def enfiler(file,elt):
       ...
   
   def defiler(file):
       ...
   
2. On souhaite compléter cette interface avec 2 nouvelles fonctions : ``tete_de_file`` et ``longueur``.
   
   a. La fonction ``tete_de_file`` prend en paramètre une file et renvoie la valeur de la tête de file sans la supprimer. Si la file est vide, la fonction renvoie ``None``.
   b. La fonction ``longueur`` prend en paramètre une file et renvoie le nombre d'éléments qu'elle contient. La file doit rester dans le même état après avoir renvoyé le nombre d'éléments.
   
   Coder en Python ces 2 fonctions.

Exercice 3
----------

John Conway est un mathématicien et informaticien britannique qui est l'auteur d'une suite numérique particulière. Chaque terme de la suite se déduit du terme précédent par énumération des chiffres qui le constituent.

- Le premier terme vaut 1. Ce terme est constitué de un 1 qui s'écrit en chiffres 11, second terme de la suite;
- Le second terme vaut 11. Ce terme est constitué de deux 1 qui s'écrit en chiffres 21;
- Le troisème terme de la suite est donc 21. Ce terme est constitué de un 2 et un 1 qui s'écrit en chiffres 1211;
- Le quatrième terme de la suite est donc 1211. Ce terme est constitué de un 1, un 2 et deux 1 qui s'écrit 111221;

Cette suite de **Conway** s'appelle *look and say* et se construit à partir d'un chiffre appelé graine. L'objectif de l'exercice est d'écrire les différents termes de la suite de Conway.

Pour cela, on utilise 2 files pour écrire les termes de la suite de Conway. La file ``f1`` contient les chiffres d'un terme de la suite et la file ``f2`` contient son énumération à l'aide de **tuple**.

1. Donner le cinquième terme de la suite de Conway.
2. Pour ce dernier terme de la suite de Conway, donner les contenus des files ``f1`` et ``f2``.
3. Coder la fonction ``terme_en_file`` qui prend en paramètre un terme de la suite sous forme de chaine de caractères et renvoie une file contenant chaque chiffre de ce terme.
4. Coder la fonction ``enumere_terme`` qui prend en paramètre une file ``f1`` dont les valeurs sont les chiffres d'un terme de la suite. Cette fonction doit parcourir la file ``f1`` et renvoyer une file ``f2`` qui contient les tuples énumérant les chiffres de la file ``f1``.
5. Coder la fonction ``terme_suivant`` qui prend en paramètre la file ``f2`` contenant l'énumération des chiffres d'un terme de la suite de Conway et qui renvoie le terme suivant de la suite sous forme d'une chaine de caractères.
6. La fonction ``suite_conway`` prend en paramètre le nombre entier *n* et renvoie la liste des *n* premier termes de la suite de Conway construite avec les fonctions ``terme_en_file``, ``enumere_terme`` et ``terme_suivant``.

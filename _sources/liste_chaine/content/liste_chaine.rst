.. TNSI

.. toctree::
   :maxdetph: 1
   
Les listes (chainées)
=====================

La liste chainée ne doit pas être confondue avec la liste python (associée à un tableau dynamique). En Python, chaque élément d'une liste est repéré par son **index**, c'est à dire sa position dans la liste, comme pour les tableaux.

La **liste chainée** est une structure de données qui lie ses éléments comme les maillons d'une chaine. Chaque maillon a une valeur et en même temps se trouve relié au maillon suivant.

.. admonition:: Exemple

   On donne une représentation schématique d'une liste chainée.
   
   .. image:: ../img/liste_chainee_exemple.svg
      :align: center
      :width: 360px
      
   - La liste ``L`` pointe sur un premier maillon de la cahine de valeur 1;   
   - Le maillon de valeur 1 pointe sur le maillon suivant de valeur 2;
   - Le maillon de valeur 2 pointe sur le maillon de valeur 4;
   - Le dernier maillon ne pointe sur rien; c'est la fin de la liste chainée.
   
Interface de la liste chainée
-----------------------------

L'interface d'une liste chainée se compose des primitives suivantes:

- Créer une liste vide ;
- Ajouter un élément en tête de liste;
- Renvoyer la valeur de l'élément en tête de liste;
- Renvoyer la liste sans son premier élément (queue de liste);
- Tester si la liste est vide;

Implémentation d'une liste chainée
----------------------------------

L'implémentation d'une liste chainée en Python peut être réalisée avec des **tuples**.
Le tuple étant **immuable**, la liste créée par cette implémentation est non mutable. Une fois créée, on ne peut pas supprimer les éléments, seulement ajouter des éléments en tête de liste. La modification d'une telle liste implique de construire de nouveaux tuples ce qui rend l'implémentation coûteuse en mémoire.

Les fonctions qui assurent l'interface de liste sont:

- Le constructeur ``creer_liste()`` qui crée une liste vide, c'est à dire un tuple vide;
- L'opérateur ``inserer(liste, element)`` qui ajoute un élément en tête de liste;
- Les accesseurs ``tete(liste)`` qui renvoie la tête de liste (sans le supprimer) et ``queue(liste)`` qui renvoie la liste sans son premier élément;
- L'accesseur ``est_vide(liste)`` qui teste si la liste est vide.

.. note::

   1. Une implémentation peut être faite en programmation objet plus efficace en mémoire que celle présentée ici.
   2. Les noms des fonctions peuvent être différents de ceux  donnés ici.
   
   
.. admonition:: Exercice

   On reprend la liste chainée donnée en exemple:

   .. image:: ../img/liste_chainee_exemple.svg
      :align: center
      :width: 360px
      

   Cette liste est constituée de trois maillons repésentés par des rectangles. Chaque maillon se compose de 2 parties:

   - la tête qui contient une valeur;
   - la queue qui contient la suite de la liste.
   
   Pour schématiser cette liste, on pourra la noter L->[1]->[2]->[4]->[].
   
   1. Vers quelle liste pointe la dernière cellule ?
   2. On souhaite représenter cette liste en écrivant chaque cellule sous la forme d'un couple (tête, queue). Donner une repésentation de cette liste.
   3. Quelles sont les instructions qui permettent de créer cette liste chainée ?
   4. Comment mémoriser dans une variable Q la liste chainée [2]->[4]->[] sans la recréer ?
   5. Comment mémoriser dans une variable R la liste chainée [4]->[] sans la recréer ?
   
   .. _`solution de l\'exercice`: exemple.html
   
   `Solution de l\'exercice`_

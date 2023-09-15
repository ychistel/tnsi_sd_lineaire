.. TNSI

Un tableau est un type de données structuré. Cela signifie qu'il peut contenir plusieurs valeurs dans une même variable. Dans un tableau, chaque valeur est repérée par sa position appelée **indice**.
  
Les tableaux
------------

Un **tableau** est une collection ordonnée d'éléments de même type. En Python, les tableaux sont  de type **tuple** ou de type **list**. On rappelle qu'un tableau représenté par le type **list** est un *tableau dynamique* car le nombre de valeurs est extensible, il est donc possible de supprimer ou d'ajouter des valeurs.

.. warning::

   Python autorise des types différents dans un même tableau, qu'il soit un tuple ou une liste.

Les tuples en Python
********************

Un **tuple** est une collection ordonnée d'éléments qui correspond aux p-uplets en mathématiques. Si le tuple contient 2 éléments c'est une paire, s'il en contient 3 c'est un triplet, etc ...

Un tuple est noté entre **parenthèses** et les valeurs sont séparées par des virgules.

Pour extraire les éléments d'un tuple, on peut utiliser :

- l'affectation multiple.
- l'indice de position de la valeur dans le tuple.

.. admonition:: Exemple

   Un point est repéré par des coordonnées que l'on place dans un tuple:
   
   .. code:: python
   
      Point = (3,5)
      
   Pour récupérer l'abscisse et l'ordonnée de ce point:
   
   .. code:: python
   
      x,y = Point
      # x prend la première valeur
      # y prend la seconde valeur
      
      abscisse, ordonnee = Point[0], Point[1]
      # abscisse prend la première valeur
      # ordonnee prend la seconde valeur
   
 
.. admonition:: Attention 
   :name: attention
   
   Un tuple est **immuable**, une fois créé, celui-ci ne peut pas être modifié. Si on construit un tuple avec des variables, les valeurs contenues dans le tuple sont celles des variables à l'instant de la construction. Si on change les valeurs des variables, le tuple reste inchangé.

   
Les listes en Python
********************

Les valeurs contenues dans une liste se notent entre crochets. Elles sont modifiables après la création du tableau. Le tableau est une structure muable (ou mutable).

L\'**interface** d'une liste s'appuie sur les fonctions et les méthodes suivantes:

- Le **constructeur** ``list()`` qui permet de créer une liste en Python; si on ajoute en paramètre un iterateur, celui-ci est transformé en liste.
- L'accès aux valeurs de la liste se fait par l'indice de position de la valeur noté entre crochets.
- Il existe d'autres **accesseurs** comme la fonction ``len()`` qui renvoie le nombre d'éléments de la liste et la méthode ``count()`` qui donne le nombre d'occurrences d'une valeur (en paramètre) de la liste.
- Les principaux **opérateurs** de listes sont les méthodes ``pop()`` et ``append()`` qui permettent de supprimer une valeur et d'en ajouter une nouvelle.

.. admonition:: Exemple

   La variable L contient une liste de valeurs telle que ``L=[5,1,3,8]``.
   
   .. code:: python
   
      L = [5,1,3,8] # construction de la liste
      a = L[2] # donc a vaut 3, valeur d'indice 2
      b = len(L) # b vaut 4 car la liste a 4 valeurs
      L.pop() # L vaut [5,1,3] puisque la dernière valeur a été supprimée.
      L.append(7) # L vaut [5,1,3,7] puisqu'on a ajouté la valeur 7

Un tableau et une liste Python sont **itérables**. Cela signifie que l'on peut parcourir les éléments un à un avec une boucle.

.. admonition:: Exemple

   On rappelle que la fonction ``range()`` est un itérateur. On peut le transformer en liste avec le constructeur ``list()``.
   
   .. code:: python
   
      L = list(range(4)) # construction de la liste
      for v in L:
         print(v)
      
      >>> 0
          1
          2
          3


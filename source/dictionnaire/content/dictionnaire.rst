.. TNSI

Un dictionnaire est un type de données structuré. Cela signifie qu'il peut contenir plusieurs valeurs dans une même variable. Dans un dictionnaire chaque valeur est associée à une **clé**.

  
Les dictionnaires
-----------------

Un dictionnaire est appelé, dans d'autres langages, tableau associatif. C'est un type de données qui associe à des **clés** des **valeurs** de type quelconque. Les **clés** sont uniques et sont souvent des chaines de caractères.

.. note::

   Les clés d'un dictionnaires peuvent aussi être des nombres ou des tuples. Il est important qu'elles soit immuables, ce qui exclut les variables.
   
Un dictionnaire se note entre **accolades**. Chaque entrée d'un dictionnaire est composée d'une clé et d'une valeur séparées par les deux points ":".

.. admonition:: Exemples

   >>> personne = {
      'nom': 'Van Rossum',
      'prenom': 'Guido',
      }
      
   >>> triangle = {
      'A': (0,1),
      'B': (3,-2),
      'C': (-1,3)
      }


L\'**interface** d'un dictionnaire s'appuie sur les fonctions et les méthodes suivantes:

- Le **constructeur** ``dict()`` qui permet de créer un dictionnaire en Python; une entrée de dictionnaire peut être précisée entre les parenthèses suivant la syntaxe ``clé=valeur``.

   >>> triangle = dict(A=(0,1))

- L'accès aux valeurs du dictionnaire se fait par la clé. La méthode ``get`` prend en paramètre une clé et renvoie la valeur associée.

   >>> triangle.get('A')
   (0,1)
   
   .. note::
      
      L'accès à une valeur peut également se faire par le nom du dictionnaire suivi du nom de la clé entre crochets :code:`triangle['A']`
      
- Il existe d'autres **accesseurs** comme la fonction ``len()`` qui renvoie le nombre d'éléments du dictionnaire.

   >>> len(triangle)
   3
   
- Les principaux **opérateurs** d'un dictionnaire sont l'ajout d'une entrée, la modification d'une valeur et la suppression d'une entrée (item). 

   - L'ajout d'une entrée et la modification d'une valeur se font par assignation.

   >>> triangle
   {'A': (0, 1), 'B': (3, -2), 'C': (-1, 3)}
   
   >>> triangle['D']=(2,1) # ajout d'une valeur
   >>> triangle
   {'A': (0, 1), 'B': (3, -2), 'C': (-1, 3), 'D': (2, 1)}
   
   >>> triangle['A']=(0,2) # modification d'une valeur
   >>> triangle
   {'A': (0, 2), 'B': (3, -2), 'C': (-1, 3), 'D': (2, 1)}

   - La suppression d'une entrée se fait avec la méthode ``pop`` qui prend en paramètre la clé à supprimer. La valeur associée à la clé est aussi supprimée.

   >>> triangle.pop('A')
   (0,2)
   >>> triangle
   {'B': (3, -2), 'C': (-1, 3), 'D': (2, 1)}

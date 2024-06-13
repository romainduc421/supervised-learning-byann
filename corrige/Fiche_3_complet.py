#!/usr/bin/env python
# -*- coding: utf-8 -*-

epsilon = 0.1

N = 5 # nombre de lignes (et de colonnes) d'une forme

alphabet = \
[ [ [False, True,  True,  True,  False],  # { A }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  True,  True,  True,  False],  # { B }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [False, True,  True,  True,  True],   # { C }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [False, True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { D }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { E }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  True],   # { F }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { G }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True] ],
   [ [True,  False, False, False, True],   # { H }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [False, False, True,  False, False],  # { I }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [False, False, True,  True,  True],   # { J }
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [True,  True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { K }
     [True,  False, False, True,  False],
     [True,  True,  True,  False, False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, False],  # { L }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  False, True,  True],   # { N }
     [True,  False, True,  False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { M }
     [True,  True,  False, False, True],
     [True,  False, True,  False, True],
     [True,  False, False, True,  True],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  False],  # { O }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  False],  # { P }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { Q }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, True,  True],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { R }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  True],   # { S }
     [True,  False, False, False, False],
     [False, True,  True,  True,  False],
     [False, False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { T }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { U }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { V }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  False, True,  False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { W }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, True,  False, True],
     [False, True,  False, True,  False] ],
   [ [True,  False, False, False, True],   # { X }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { Y }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  True,  True,  True,  True],   # { Z }
     [False, False, False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, False, False],
     [True,  True,  True,  True,  True] ] ]

# Initialisation du réseau
#
# -> 0.0 pour les seuils
# -> 0.5 pour les poids (avec des 0.0 sur la diagonale)

N_cell = N*N

seuils = [ 0.0 for _ in range(N_cell) ]

poids  = [ [ 0.5 for _ in range(N_cell)] for _ in range(N_cell) ]
for i in range(N_cell):
  poids[i][i]=0


# Apprentissage des 26 lettres

print ("\nApprentissage : ", end="")

modifications = 1 # Initialisation à 1 pour entrer dans la boucle

while modifications !=0:

  modifications = 0

  for lettre in alphabet:

    # Présentation d'une lettre

    etats = []
    for i in range(N):
      etats += lettre[i]

    for cellule in range(N_cell):

      # Activation d'une cellule

      somme = 0
      for i in range(N_cell):
        if etats[i]:
          somme += poids[cellule][i]
      somme -= seuils[cellule]
      sortie = somme > 0

      # Modification des poids si nécessaire

      if sortie != etats[cellule]: # si on est "pas content" de la sortie

        modifications += 1

        if somme>0:
          somme += epsilon
        else:
          somme -= epsilon

        delta = somme / (sum(etats) - etats[cellule] + 1)

        for i in range(N_cell):
          if etats[i] and i!=cellule:
            poids[cellule][i] -= delta # modification des poids
            poids[i][cellule] -= delta # conservation de la symétrie
        seuils[cellule] += delta       # modification du seuil

        # Début vérification de l'efficacité de la modification (facultatif)
  
        somme = 0
        for i in range(N_cell):
          if etats[i]:
            somme += poids[cellule][i]
        somme -= seuils[cellule]
        sortie = somme > 0
  
        if sortie != etats[cellule]:
          print ("ERREUR : modification des poids erronée")
          import sys
          sys.exit()

        # Fin vérification de l'efficacité de la modification (facultatif)

  print (modifications, end=" ")
  
print ("\n")

# Test du réseau en essayant de reconnaître un N bruité

lettre = [ [True,  False, True,  False, True],
           [True,  True,  False, False, True],
           [False, False, True,  False, True],
           [True,  False, False, True,  True],
           [True, False, False, False, True] ]

# Affichage de la forme

print ("Forme à reconnaître :\n")

box = chr(0x2588) + chr(0x2588)
for i in range(N):
  for j in range(N):
    if lettre[i][j]:
      print (box, end="")
    else :
      print ("  ", end="")
  print ("")
print ("")

etats = []
for i in range(N):
  etats += lettre[i]

# Propagation de l'activation

dejavu = [list(etats)]
while True:
  for cellule in range(N_cell):
    somme = 0
    for i in range(N_cell):
      if etats[i]:
        somme += poids[cellule][i]
    somme -= seuils[cellule]
    etats[cellule] = somme > 0

  if etats in dejavu:
    break
  else:
    dejavu.append(list(etats))

stable  = [ [ True for _ in range(N)] for _ in range(N) ]
for i in range(N):
  for j in range(N):
    stable[i][j] = etats[i*N+j]

print ("Forme stable :\n")
  
for i in range(N):
  for j in range(N):
    if stable[i][j]:
      print (box, end="")
    else :
      print ("  ", end="")
  print ("")
print ("")

print ("Forme reconnue :", chr(alphabet.index(stable)+65), "\n")


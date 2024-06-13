from random import random

f_activation = lambda x: 0 if x < 0 else 1

OU = [ ([0,0,1], 0),
       ([0,1,1], 1),
       ([1,0,1], 1),
       ([1,1,1], 1) ]

ET = [ ([0,0,1], 0),
       ([0,1,1], 0),
       ([1,0,1], 0),
       ([1,1,1], 1) ]

XOR = [ ([0,0,1], 0),
        ([0,1,1], 1),
        ([1,0,1], 1),
        ([1,1,1], 0) ]

exemples = ET
w        = [random(), random(), random()]
eta      = 0.5
erreurs  = []
nbmi=1000

ok = False
while (ok != True) and (nbmi != 0):
 ok = True
 nbmi -= 1
 for i in range(4):
  x, etiquette = exemples[i]
  wx=w[0]*x[0]+w[1]*x[1]+w[2]*x[2]
  erreur = etiquette - f_activation(wx)
  erreurs.append(erreur)
  for j in [0, 1, 2]:
   w[j] += eta * erreur * x[j]
  if erreur!=0 :
   ok = False

if nbmi == 0 :
    print("Pas de convergence !")
else:

    for x, _ in exemples :
     wx=w[0]*x[0]+w[1]*x[1]+w[2]*x[2]
     print ("[", x[0], x[1], "] : ", wx,
            " -> ",f_activation(wx))

    print(erreurs)

    from matplotlib.pylab import plot, xlim, ylim, show,title

    ylim([-1,1])
    title("Erreur en fonction du nombre d'iterations")
    plot(erreurs, linewidth=4)
    show()

    xlim([0,1])
    ylim([0,1])
    title("Hyperplan separateur")
    h = lambda x: - w[0]/w[1] * x - w[2]/w[1]
    plot([h(x) for x in [0,1]], linewidth=4)

    show()










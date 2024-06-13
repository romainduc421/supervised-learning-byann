from numpy import array, dot, add, random
from matplotlib.pyplot import xlim, ylim, show, title, plot, legend

f_activation = lambda x: 0 if x < 0 else 1

OU = [ (array([0,0,1]), 0),
       (array([0,1,1]), 1),
       (array([1,0,1]), 1),
       (array([1,1,1]), 1), ]

ET = [ (array([0,0,1]), 0),
       (array([0,1,1]), 0),
       (array([1,0,1]), 0),
       (array([1,1,1]), 1), ]

XOR = [ (array([0,0,1]), 0),
        (array([0,1,1]), 1),
        (array([1,0,1]), 1),
        (array([1,1,1]), 0), ]

exemples = ET
w        = random.rand(3)
eta      = 0.2

def error(w, exemples):
    error = 0
    for X,d in exemples:
        error += (d - f_activation(dot(w, X)))
    return error

k=-1
noms = ["OU", "ET", "XOR"]
for exemples in [OU, ET, XOR]:
    k+=1
    epochs=100
    errors = []
    for epoch in range(epochs):
        erreur = error(w, exemples)
        errors.append(erreur)
        for X,d in exemples:
            S = f_activation(dot(w, X))
            for i in range(len(X)):
                w += eta * (d - S) * X
        
        if erreur == 0:
            break

    for i, erro in enumerate(errors):
        print(f"Epoch {i+1} : Erreur = {erro}")

    w_1,w_2,w_3 = w
    print(f"Hyperplan de séparation : {w_1}x1 + {w_2}x2 + {w_3} = 0")
    
    if epoch < 99:
        print("Convergence en", epoch, "epochs")
        title("Hyperplan de séparation")
        xlim([0, 1])
        ylim([0, 1])
        x=array([0,1])
        y_eq = -w_1/w_2 * x - w_3/w_2
        plot(x, y_eq, label=noms[k])
        legend(loc="upper left")
    else:
        print("Pas de convergence")  
show()
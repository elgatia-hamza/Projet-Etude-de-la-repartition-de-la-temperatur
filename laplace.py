""" ################################################################
# Etude de la répartition de température dans les parois d'un four #
# Methode utilisée : Methode de difference fini                    #
#                                                                  #
# Realiser par:                                                    #
# * EL Gatia Hamza                                                 #
# * Fadili Elmostafa                                               #
# * Hablatou Youssef                                               #
# * Awanyo Kossi Jean Baptiste Christson                           #
# ################################################################ """


import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (10, 6)


# Definir notre meta-variables (i.e. epsilon est la limite de convergence, k la limite des iterations)
eps = 1e-6
k = 300


# définir les données initiales
# L1,L2,L3,L4 sont les dimentions de notres systeme:
L1 = float(input('Entrer la valeur de L1 : '))
L2 = float(input('Entrer la valeur de L2 : '))
L3 = float(input('Entrer la valeur de L3 : '))
L4 = float(input('Entrer la valeur de L4 : '))

# Condition aux limites
# Theta_i : température interieur du four
Theta_i = float(input('Entrer la valeur de Theta intern : '))

# Theta_e : température exterieur du four
Theta_e = float(input('Entrer la valeur de Theta extern : '))

# Maillage :  descritisation (Calculer les indices m,n m1,m2 n1,n2)
h = float(input('Entrer la valeur du pas de déscritisation h : '))
n = round(L1//h) + 1
m = round(L2//h) + 1
n1 = round((L1 - L3)//2*h) + 1
m1 = round((L2 - L4)//2*h) + 1
n2 = n1 + round(L3//h)
m2 = m1 + round(L4//h)

#print(f'n = {n} , n1 = {n1}, n2 = {n2}')
#print(f'm = {m} , m1 = {m1}, m2 = {m2}')

# Initialisation des données
# Initialisation de la température dans le four
dim = (n,m)
T = np.full(dim, Theta_i)

# Température de la paroi externe
T[0:n, 0] = Theta_e
T[0:n, m-1] = Theta_e

T[0, 0:m] = Theta_e
T[n-1, 0:m] = Theta_e

for it in range(k):
    for i in range(1,n-1):
        for j in range(1,m1-1):
            T[i,j] = 0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
        
        for j in range(m2, m-1):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
            
    for i in range(1, n1-1):
        for j in range(m1-1,m2):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
    
    for i in range(n2, n-1):
        for j in range(m1-1,m2):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
    
    # Test Condition de convergence:
    if abs(T[n-2, m-2] - T[1,1]) <= eps:
        print(f"Nombre des iteration {it}")
        break

# Tracé des courbes de température en 3D
fig = plt.figure()
fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)

# contriure grid 2d base figure:
Xindex = np.arange(0, n, h)
Yindex = np.arange(0, m, h)
Xindex, Yindex = np.meshgrid(Xindex, Yindex)

# Plot surface.
surf = ax.plot_surface(X = Xindex, Y = Yindex, Z=T,cmap=cm.coolwarm,linewidth=5, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Evolution de la température dans le four')

plt.show()

# tracer contour de temperature isotherme:
Xindex = np.arange(0, n, h)
Yindex = np.arange(0, m, h)
plt.contour(Xindex, Yindex, T, cmap = cm.coolwarm)
plt.title('Contour de temperature isotherme')
plt.show()

    

            





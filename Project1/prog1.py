import numpy as np
import matplotlib.pyplot as  plt
########################    PRE - PROCESSING  ########################

c=0
f=0

x_a = 0
x_b = 1

l_wezlow = 4

#wezly= np.array([1, 2, 3, 4, 5])

wezly = np.array([[1, 0],
                  [2, 1],
                  [3, 0.5],
                  [4,0.75]])


elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1

################### Funkcja generujaca tablice ###################

def generujTabliceGeometrii(x_a,x_b, n):
    # l_elementow = n-1
    odstep = (x_b - x_a) / (n - 1) #wyliczenie odstepu
    wezly = np.array([1, x_a]) #pierwszy wiersz tablicy wezly
    elementy = np.array([1,1,2]) #pierwszy wiersz tablicy elementy

    for i in range(1, n, 1):
       wezly = np.block([
            [wezly ],
            [i+1, i * odstep+x_a],
        ])

    for j in range(2, n,1):
        elementy = np.block([
            [elementy],
            [j,j,j+1]])

    return wezly,elementy

# Wywolanie zwroci tablice wezlow i tablce elementow dla podanego 1 wezla, ostatniego wezla i liczby wezlow
tablica_w, tablica_e = generujTabliceGeometrii(1,5,10)


print(tablica_w)
print(tablica_e)

################### Funkcja wyswietlajaca ################

def rysujgeometrie (tab_w):
    y = np.zeros(tab_w.shape[0])
    plt.plot(tab_w[:, 1], y, marker='o') #wyrysowanie elementow

    for i in range(0, np.size(y), 1): #podpis wezlow
        plt.text(x=tab_w[i, 1], y=y[i]-0.007, s=int(tab_w[i, 0]),fontsize=7,color ='green' )
        # plt.text(x=tab_w[i, 1]+, y=y[i] - 0.007, s=tab_w[i, 0], fontsize=12, color='green')

    for i in range(0, np.size(y) - 1, 1): #podpis elementow
        plt.text(x=(tab_w[i, 1] + tab_w[i + 1, 1]) / 2, y=y[i] + 0.003, s=int(i + 1),fontsize=7, color='blue')
    plt.show()

# jako wywolanie podajemy tablice wezlow a otrzymujemy wyplotowana geometirie
rysujgeometrie(tablica_w)


### Lab implementacja FEM -  1  ###


import numpy as np
import matplotlib.pyplot as  plt
import scipy.integrate as plt
########################    PRE - PROCESSING  ########################

c=0
#wymuszenie
f= lambda x: 0*x

x_a = 0
x_b = 1
x = 5 # ilosc wezlow NOODES

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1

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

WB = [{"ind":1, "typ":'D', "wartosc":1},
      {"ind":2, "typ":'D', "wartosc":2}]
      {"ind":x, "typ":'D', "wartosc":2}]

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

### Lab implementacja FEM -  2  ###

def Alokacja(x):
    tmp = (x,x)
    tmp1 = (x,1)
    A = np.zeros(tmp)
    b = np.zeros(tmp1)
    return A, b
A,b = Alokacja(x)
print(A)
print(b)


#def Bazowa(x):
def FunkcjeBazowe(x):
    #x stpoień funkcji kształtu
    #zwraca liste funkcji kształtu

    if x==0:
        f = (lambda x: 1+0*x)
        df = (lambda x: 0*x)

    elif x==1:

        f = (lambda x: -1/2*x + 1/2, lambda x: 0.5*x + 0.5)
        df = (lambda x: -1/2 + 0 * x, lambda x: 0.5 + 0 * x )

    #elif n==2:

        #f = (lambda,lambda,lambda)
    else:
        raise Exception("Błąd")

    return f,df
stopien_funkcji_bazowych = 1
phi,dphi = FunkcjeBazowe(stopien_funkcji_bazowych)

print(phi)
print(dphi)

xx = np.linspace(-1,1,101)
plt.plot(xx,phi[0](xx),'r')
plt.plot(xx,phi[1](xx),'g')
plt.plot(xx,dphi[0](xx),'b')
plt.plot(xx,dphi[1](xx),'c')
plt.show()

#Preprocesing

liczbaElementow = np.shape(elementy)[0]
for ee in np.arange(0,liczbaElementow):

    elemRowInd = ee
    elemGlobalInd = elemety[ee,0]

    elemWezel1 = elemety[ee,1]  #indeks wezla poczatkowego elementu ee
    elemWezel2 = elemety[ee, 2] # indeks wezla koncowego elementu ee

    Ml = np.zeros(stopien_funkcji_bazowych + 1, stopien_funkcji_bazowych + 1)

    def Aij(df_i, df_j, c, f_i, f_j):

        fun_podc = lambda x: -df_i(x)*df_j(x) + c * f_i(x)*f_j(x)

        return fun_podc

    p_a = wezly[elemWezel1-1,1]
    p_b = wezly[elemWezel2-1,1]

    J = (p_b-p_a)/2

    Ml[0,0] = J * spint.quad(Aij(dphi[0],dphi[0],c,phi[0],phi[0]),-1,1)
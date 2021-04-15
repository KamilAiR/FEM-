import numpy as np
import matplotlib as  mp
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


def generujTabliceGeometrii(x_a,x_b, n):
    odstep = (x_b - x_a) / (n - 1)
    matrix = np.array([1, x_a])

    for i in range(1, n, 1):
        matrix = np.block([
            [matrix],
            [i+1, i * odstep+x_a],
        ])
    return matrix


print(generujTabliceGeometrii(1,4,5))
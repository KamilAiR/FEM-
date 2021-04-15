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
print(wezly)

elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1
import numpy as np
#-------------------------------------------zad 3--------------------------------------------------------


a = np.arange(1,6)
b = np.arange(5,0, -1) # co 1 w dol
c = np.zeros([3,2], dtype = int) #tablica zer
d=2* np.ones((2,3),  dtype = int) # mnozac ones przez 2 bedziemy miec same 2-ki
e = np.linspace(-90,-70,3,dtype = int)
f=np.array([[10],[10],[10],[10],[10]])

X= np.block([[a],[b]])
B= np.block([[d],[e]])
C= np.block([[c,B]])
D= np.block([[X],[C]])
A= np.block([[D,f]])
print(A)

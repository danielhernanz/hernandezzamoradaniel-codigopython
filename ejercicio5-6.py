#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

print("Ingresa los valores de la ecuacion de segundo grado")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("{}x^2+{}x+{}".format(a,b,c))


raiz = math.sqrt((b**2)-(4*a*c))
chA = (-b) + raiz
chA2 = (-b)- raiz

chD = (chA/(2*a))
chD2 = (chA2/(2*a))

print("Valor de x1: {} y valor de x2: {}".format(chD,chD2))


# In[5]:


posi = float(input("Ingresa un numerito:  "))

if posi > 0: 
    print("El numero es positivo")
elif posi < 0:
    print("El numero es negativo")
else:
    print("El numero es un cero")


# In[ ]:





# In[ ]:





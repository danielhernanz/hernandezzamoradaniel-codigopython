#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Re1 = float(input("Ingresa la primer resistencia en paralelo: "))
Re2 = float(input("Ingresa la segunda resistencia en paralelo: "))

print("La resistencia total es:", ((Re1*Re2)/(Re1+Re2)))


# In[3]:


print("Ingresa los 4 valores de la matriz empezando por el primer renglon")
num1 = int(input(": "))
num2 = int(input(": "))
num3 = int(input(": "))
num4 = int(input(": "))
print("|{} {}|".format(num1,num2))
print("|{} {}|".format(num3,num4))

print("La determinante es: ", ((num1*num4)-(num3*num2)))


# In[ ]:





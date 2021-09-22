#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nombre = str(input("Ingresa tu nombre para comienzo al proceso de evaluacion crediticio:  "))
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    telefono = int(input("Ingresa tu telefono: "))
    ingm= int(input("De cuanto es tu ingreso mensual? : "))
    egrm= int(input("De cuanto es tu egreso mensual? : "))
    if ingm > egrm : 
        plazom= int(input("En caso de otorgarte el credito,en cuantos meses cubririas la cuota: "))
        monto = int(input("Cuanto efectivo requieres? :"))
        
        cuota = monto / plazom
        if cuota < (ingm - egrm):
            print("Felicidades fuiste aceptado, posteriormente nos comunicaremos al siguiente numero : {}".format(telefono))
        else:
            print("No cumple con los requisitos para la evaluacion crediticia")
           
    else:
        print("No cumple con los requisitos para la evaluacion crediticia")
        
else:
    print("No cumple con los requisitos para la evaluacion crediticia")




# In[9]:


lista = []
for i in range(1,5+1,1):
    lista.append('*'*(i))
    
for recorrer in lista:
    print(recorrer)


# In[ ]:





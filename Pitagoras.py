#Programa del teorema de pitagoras
import math
lado=input("Que buscas cateto opuesto=1,Cateto adyacente=2 o hipotenusa=3")
if int (lado)==1:
    hipotenusa=input("\tIngresa el valor de la hipotenusa")
    catetoad=input("\tIngresa el cateto adyacente")
    catop=math.sqrt(int(hipotenusa)**2- int(catetoad)**2)
    print(catop)
    input()
elif int(lado)==2:
    catop=input("\tIngresa el valor del contexto opuesto")
    hipotenusa=input("\tIngresa el valor de la hipotenusa")
    catetoad=math.sqrt(int(hipotenusa)**2-int(catop)**2)
    print(catetoad)
    input()
elif int(lado)==3:
    catetoad = input("\tIngresa el cateto adyacente")
    catop = input("\tIngresa el valor del contexto opuesto")
    hipotenusa=math.sqrt(int (catop)**2+ int(catetoad)**2)
    print(hipotenusa)
    input()
else:
    print("Ingresa un valor valido")

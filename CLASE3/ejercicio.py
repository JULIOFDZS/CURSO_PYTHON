'''
Crea un programa que pida dos numeros y 
obtengan como resultado cual de ellos es 
par o si ambos lo son
'''
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos numeros son pares")
elif n1 % 2 == 0:
    print("El primer numero es par")
elif n2 % 2 == 0:
    print("El segundo numero es par")
else:
    print("Ninguno de los dos numeros es par") 
'''
CREAR UN PROGRAMA QUE PIDA DOS NUMEROS Y OBTENGA
COMO RESULTAFO CUAL DE ELLOS ES PAR O SI AMBOS LO SON
'''

n1=int(input("Ingrese el primer nunero:"))
n2=int(input("Ingrese el segundo numero"))

par1=0
par2=0
par1=n1%2==0
par2=n2%2==0

if par1 and par2:
    print("Los dos numero son pares")
elif par1:
    print(f"El numero {n1} es par, minetras que el numero {n2} es impar")
elif par2:
    print(f"El numero {n1} es impar, mientras que el numero {n2} es par")
else:
    print("Ninguno de los numero es par")


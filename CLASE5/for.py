'''
Bucle For 
'''


for i in [6,8,9,4,7, True, "Hola", [0,1,2]]:
    print(f"Datos: {i}")
print("------")
data={"Futbol","PC",18.6,18,[6,7,10.5],True,False,"PC"}
for i in data:
    print(f"Datos: {i}")



print("---for range---")
for i in range(0, 20):  # Desde 0 hasta 20
    print(f"Datos: {i}")
          
          
print("---while---")
numero = 0
while numero <= 20:
    print("El Número es:", numero)
    numero += 1  # Incrementa en 1
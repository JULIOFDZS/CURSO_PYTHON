'''
introduccion a las listas en python
'''
#definicion de una lista
array=["futbol","Pc",18.6,18,[6,7,10.5],True,False]
print(array)

# Acceso a elementos de la lista
print(array[0])  # Primer elemento
print(array[4][1])  # Segundo elemento de la sublista  
print(array[-1])  # Último elemento

print("Pc" in array)  # Verificar si "Pc" está en la lista
print(array.index("futbol"))  # Devuelve el índice de "Pc"
print(array.count("Pc"))  # Cuenta cuántas veces aparece "Pc"
array.clear()  # Limpia la lista
print("Array", array)

array = ["futbol","Pc", 18.6, 18, [6,7,10.5], True, False]
array.reverse()  # Invierte la lista
print("Array invertido", array)
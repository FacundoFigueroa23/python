# Calculador de promedio

apellido = input("Ingrese Apellido: ")
nombre = input("Ingrese Nombre: ")

notas = int(input("Ingrese la cantidad de notas: "))

suma = 0

for n in range(notas) :
    suma += int(input("Ingrese nota: "))

promedio = suma/notas

if (promedio >= 8) :
    print("El alumno", nombre, apellido, "promocionó con un promedio de", round(promedio, 2))
elif (promedio >= 4) :
    print("El alumno", nombre, apellido, "aprobó con un promedio de", round(promedio, 2))
else :
    print("El alumno", nombre, apellido, "reprobó con un promedio de", round(promedio, 2))
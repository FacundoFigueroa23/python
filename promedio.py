# Calculo de promedio

apellido = input("Ingrese Apellido: ")
nombre = input("Ingrese Nombre: ")

nota1 = int(input("1° Nota:"))
nota2 = int(input("2° Nota:"))
nota3 = int(input("3° Nota:"))

promedio = (nota1 + nota2 + nota3)/3

if (promedio >= 8) :
    print("El alumno", nombre, apellido, "promocionó con un promedio de", round(promedio, 2))
elif (promedio >= 4) :
    print("El alumno", nombre, apellido, "aprobó con un promedio de", round(promedio, 2))
else :
    print("El alumno", nombre, apellido, "reprobó con un promedio de", round(promedio, 2))
def operacion (opcion, a, b) :
    if opcion == 1 :
        return a + b
    elif opcion == 2 :
        return a - b
    elif opcion == 3 :
        return a / b
    elif opcion == 4 :
        return a * b
    else :
        return "No existe la operacion!"

def menu () :
    print("|----- Operaciones -----|")
    print("1 -> Suma")
    print("2 -> Resta")
    print("3 -> Division")
    print("4 -> Multiplicacion")
    print("")

operaciones = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "x"
}

auxiliar = True
    
while auxiliar :
    menu()
    op = int(input("Que operacion desea realizar? "))
    if op > 4 or op < 1 :
        print("Operacion no definida")
        print("")
    else : 
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("")
        print(f"-> {num1}  {operaciones[str(op)]}  {num2}  =  {operacion(op, num1, num2)}")
        print("")
        pregunta = input("Quiere seguir operando? (SI / NO): ")
        print("")
        if pregunta.lower() == "no" :
            auxiliar = False

print("Fin del programa.")
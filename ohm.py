def ohm (vol, cor, res) :
    if vol == 0 :
        while True :
            if cor == 0 or res == 0 :
                print("Los datos ingresados no pueden ser cero! Ingreselos nuevamente.")
                cor = int(input("Ingrese corriente: "))
                res = int(input("Ingrese resistencia: "))
            else :
                print(f"Voltaje = {cor * res}, corriente = {cor}, resistencia = {res}")
                break
    elif cor == 0 :
        while True :
            if vol == 0 or res == 0 :
                print("Los datos ingresados no pueden ser cero! Ingreselos nuevamente.")
                vol = int(input("Ingrese voltaje: "))
                res = int(input("Ingrese resistencia: "))
            else :
                print(f"Voltaje = {vol}, corriente = {vol / res}, resistencia = {res}")
                break
    else :
        while True :
            if vol == 0 or cor == 0 :
                print("Los datos ingresados no pueden ser cero! Ingreselos nuevamente.")
                vol = int(input("Ingrese voltaje: "))
                cor = int(input("Ingrese corriente: "))
            else :
                print(f"Voltaje = {vol}, corriente = {cor}, resistencia = {vol / cor}")
                break

voltaje = int(input("Ingrese voltaje: "))
corriente = int(input("Ingrese corriente: "))
resistencia = int(input("Ingrese resistencia: "))

ohm(voltaje, corriente, resistencia)
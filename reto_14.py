# ENUNCIADO
# Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
# No está permitido usar funciones propias del lenguaje de programación que realicen esas operaciones directamente.

def decAOct (dec) :
    oct = ""
    while dec / 8 >= 1 :
        oct += str(dec % 8)
        dec //= 8
    oct += str(dec)
    print("Octal = " + oct[::-1])

def decAHex (dec) :
    hex = []
    valores = ['10', '11', '12', '13', '14', '15']
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    while dec / 16 >= 1 :
        hex.append(str(dec % 16))
        dec //= 16
    hex.append(str(dec))
    hex.reverse()
    for i in range(len(hex)) :
        for j in range(len(valores)) :
            if hex[i] == valores[j] :
                hex.pop(i)
                hex.insert(i, letras[j])
    valor = ''
    for i in hex :
        valor += i
    print("Hexadecimal = " + valor)
#!usr/bin/python

# El siguiente codigo es la prueba de como aprender Python facil y rapido en 3 dias,
# Se utilizo el curso del Dr. Chuck https://online.dr-chuck.com/index.php

# Dia 1
def ejercicio1():
    print("Ejercicio 1")
    print("Hola Mundo\n")

def ejercicio2():
    print("Ejercicio 2")
    name = input("Escribe tu Nombre: ")
    print("Hola",name)
    print()

def ejercicio3():
    print("Ejercicio 3")
    hrs = float(input("Enter Hours:"))    
    rate = float(input("Enter Rate:"))
    total = hrs * rate
    print(type(hrs),  type(rate), type(total))
    print(total)
    print()

def ejercicio4():
    print("Ejercicio 4")
    Cs = float(input("score: "))
    if Cs > 1.0: 
        print("Bad Input, try again")
    elif Cs < 0:
        print("Bad Input, try again")
    elif Cs < 0.6:
        print("F")
    elif Cs >= 0.6 and Cs < 0.7:
        print("E")
    elif Cs >= 0.7 and Cs < 0.8:
        print("D")
    elif Cs >= 0.8 and Cs < 0.9:
        print("B")
    elif Cs >= 0.9 and Cs < 1:
        print("A")
    print()

def ejercicio5():
    print("Ejercicio 5")
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    pago = computepay(hrs,rate)  # Llamado a la función
    print("Pay:",pago)
    print("**********Final del dia 1**********")

def computepay(h, r) :
    if h > 40:
        ex = h - 40
        total = 40.0 * r + ex * 1.5 * r
    else :
        total = h * r
    return total

ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
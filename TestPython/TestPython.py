#!usr/bin/python

# El siguiente codigo es la prueba de como aprender Python facil y rapido en 3 dias,
# Se utilizo el curso del Dr. Chuck https://online.dr-chuck.com/index.php

# Dia 1

def computepay(h, r) :
    if h > 40:
        ex = h - 40
        total = 40.0 * r + ex * 1.5 * r
    else :
        total = h * r
    return total
#  Fin de la función ahora viene el código que normalmente se ejecuta
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pago = computepay(hrs,rate)  # Llamado a la función
print("Pay:",pago)
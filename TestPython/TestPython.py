#!usr/bin/python

# El siguiente codigo es la prueba de como aprender Python facil y rapido en 3 dias,
# Se utilizo el curso del Dr. Chuck https://online.dr-chuck.com/index.php

# Dia 1

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
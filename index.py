def ganador():
    return random.randint(1,2)

import random
saldo_total = 0
while True:
    equipos = ['Uruguay', 'Brazil', 'Argentina']
    index = random.randint(0,2)
    contrincante = equipos[index]
    partido = ['bolivia', contrincante]
    print("partido ", partido[0] + " vs " + partido[1])
    print("seleccione la opcion a apostar")
    print("1. Bolivia")
    print("2. " + contrincante)
    opcion = int(input())
    saldo_inicial = int(input("introduzca el monto\n"))
    
    if ganador() == opcion:
        saldo_total = saldo_total + 2*saldo_inicial
        print("Felicidades, gano la apuesta, su nuevo saldo es:", saldo_total)
    else:
        saldo_total = saldo_total - saldo_inicial
        print("Apuesta perdida, su nuevo saldo es ", saldo_total)
    print("quiere seguir jugando? si/no")
    respuesta = input()
    if respuesta == "no":
        break

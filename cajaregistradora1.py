# Caja registradora: calcula la cantidad de cambio a entregar
# v. 1.3
# (c) 2024, José Enrique Álvarez
denominacion = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
billete = [ True, True, True, True, True, True, False, False, False, False]
cantidad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cambio = 5921

c = len(denominacion)

for i in range(0,c):
    cantidad[i] = cambio // denominacion[i]
    cambio = cambio % denominacion[i]

for i in range(0,c):
    if cantidad[i]:
        if billete[i] == True:
            print(cantidad[i], " billetes de $", denominacion[i])
        else:
            print(cantidad[i], " monedas de $", denominacion[i])

# Programa generador de cuentas de correo electrónico
# v. 0.1
# (c) 2024, José Enrique Alvarez
prefijo = ['a','b','c','d','e','f','g']
infijo = ['alvarez','castillo','sanchez','martinez','canul','martin','rojas']
sufijo = ['60','70','80','90']
dominio = ['hotmail.com','gmail.com','mail.com','lawrence.com']

for p in prefijo:
    for i in infijo:
        for s in sufijo:
            for d in dominio:
                print(p + i + s + '@' + d)

# Ahora hagamos un listado de contraseñas:
digitos = ['0','1','2','3','4','5','6','7','8','9']

#for d1 in digitos:
#    for d2 in digitos:
#        for d3 in digitos:
#            for d4 in digitos:
#                print( d1 + d2 + d3 + d4)

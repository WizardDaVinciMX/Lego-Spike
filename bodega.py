
def altas():
    print("Bienvenido al módulo de altas")

def bajas():
    print("Bienvenido al módulo de bajas")

def cambios():
    print("Bienvenido al módulo de cambios")

def consultas():
    print("Bienvenido al módulo de consultas")

def main():
    r = ""
    while r != "s":
        r = input("Qué desea hacer: ")
        if r == "a":
            altas()
        elif r == "b":
            bajas()
        elif r == "c":
            cambios()
        elif r == "o":
            consultas()

main()

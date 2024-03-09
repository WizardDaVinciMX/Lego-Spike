# Cálculo de la fuerza de gravitación o de atracción
# (c) 2024 José Enrique Álvarez
# v. 0.1
# Sirve para ejemplificar cómo trabajan los módulos

G = 6.67e-11    # N.m²/kg²

def fuerza(m1, m2, d):
    r = G * m1 * m2 /d**2
    return r

def main():
    s = input("Masa 1: ")
    m1 = float(s)
    s = input("Masa 2: ")
    m2 = float(s)
    s  = input("Distancia: ")
    d  = float(s)
    f  = fuerza(m1, m2, d)
    print("La fuerza de atracción es", f)

main()

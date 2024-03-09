# Caja registradora v. 0.2
# (c) 2024, José Enrique Álvarez

pago = 4787

b1000 = pago // 1000
resto = pago % 1000
b500 = resto // 500
resto = resto % 500
b200 = resto // 200
resto = resto % 200
b100 = resto // 100
resto = resto % 100
b50 = resto // 50
resto = resto % 50
b20 = resto // 20
resto = resto % 20
m10 = resto // 10
resto = resto % 10
m5 = resto // 5
resto = resto % 5
m2 = resto // 2
resto = resto % 2
if b1000 != 0:
    print("Billetes $1,000: ", b1000)
if b500 != 0:
    print("Billetes $500: ", b500)
if b200 != 0:
    print("Billetes $200: ", b200)
if b100 != 0:
    print("Billetes $100: ", b100)
if b50 != 0:
    print("Billetes $50: ", b50)
if b20 != 0:
    print("Billetes $20: ", b20)
if m10 != 0:
    print("Monedas $10: ", m10)
if m5 != 0:
    print("Monedas $5: ", m5)
if m2 != 0:
    print("Monedas $2: ", m2)
if resto != 0:
    print("Monedas $1: ", resto)
print("Gracias por usar nuestro software.")
print("Vuelva pronto.") 
# Simulación de bala de cañón
# (c) 2024, José Enrique Álvarez

delta_t = 1 / 10    # Incremento de tiempo: décima de segundo


# Variables del movimiento horizontal
bx = 0
vx = 1
ax = 0

# Variables del movimiento vertical
by = 0
vy = 144 * 1000 / 3600 # km/h * m/km / s/hora
ay = -9.81 # Debiera ser 9.81 pero redondeamos

#for t in range(0,11):
while by >= 0:
    print("x= ", bx, " y= ", by)
    bx = bx + delta_t * vx
    vx = vx + delta_t * ax
    by = by + delta_t * vy
    vy = vy + delta_t * ay

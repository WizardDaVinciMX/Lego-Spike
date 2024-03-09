import random
import pygame
import time

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
RADIO = 20

def posicionDistinta(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return False
    else:
        return True

def mover(h):
    p = h[0]
    actualizarPosiciones(p)
    pActual = p[0]
    if random.random() > 0.5:
        pActual[0] = pActual[0] + RADIO
    else:
        pActual[0] = pActual[0] - RADIO
    if random.random() > 0.5:
        pActual[1] = pActual[1] + RADIO
    else:
        pActual[1] = pActual[1] - RADIO
    ajustar(pActual)

def actualizarPosiciones(p):
    for i in range(4,0,-1):
        # ¡Cuidado! Como p[i] son listas, si hacemos
        # p[i] = p[i-1]
        #sólo cambiamos referencias, no valores.
        #Así que debemos hacer:
        p[i][0] = p[i-1][0]
        p[i][1] = p[i-1][1]

def ajustar(h):

    if h[0] < 0:
        h[0] = 0
    elif h[0] > SCREEN_WIDTH:
        h[0] = SCREEN_WIDTH
    if h[1] < 0:
        h[1] = 0
    elif h[1] > SCREEN_HEIGHT:
        h[1] = SCREEN_HEIGHT
    

def visualizar(h, screen):
#    print(h)
    p = h[0]
    for i in range(4,0,-1):
        c = ( h[1][0] // (1+i), h[1][1], h[1][2])
        pygame.draw.circle(screen, \
                           c, \
                           (p[i][0], \
                            p[i][1]), \
                            RADIO - 2*i)

def inicializar():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT)  )
    pygame.display.set_caption("Hormiga borracha browniana")
    return screen

def flip(s):
    pygame.display.flip()
    time.sleep(0.15)
    s.fill((255,255,255))

def finJuego(h):
    # Guardamos en "p" la lista de posiciones de la hormiga "h"
    p = h[0]
    # Guardamos en "pActual" la lista de posiciones x,y actual de la hormiga
    pActual = p[0]
    if  pActual[0] < 0 or \
        pActual[0] > SCREEN_WIDTH or \
        pActual[1] < 0 or \
        pActual[1] > SCREEN_HEIGHT:
        return True
    else:
        return False

def main():
    s = inicializar()

    # Las últimas "n" posiciones que ha ocupado la hormiga
    p = [ [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [0,0], [0,0], [0,0], [0,0]]

    # La hormiga, compuesta por sus últimas "n" posiciones y su color
    h1 = [p,(255,0,0)]
#    h2 = [200,100,(0,255,0)]

#    while posicionDistinta(h1, h2):
    while not finJuego(h1):
        mover(h1)
#        mover(h2)
        visualizar(h1, s)
#        visualizar(h2, s)
        flip(s)
main()

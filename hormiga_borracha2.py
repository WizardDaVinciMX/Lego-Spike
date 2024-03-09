import random
import pygame
import time

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

def posicionDistinta(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return False
    else:
        return True

def mover(h):
    if random.random() > 0.5:
        h[0] = h[0] + 10
    else:
        h[0] = h[0] - 10
    if random.random() > 0.5:
        h[1] = h[1] + 10
    else:
        h[1] = h[1] - 10

def visualizar(h, screen):
#    print(h)
    pygame.draw.circle(screen, h[2], (h[0], h[1]), 10)

def inicializar():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT)  )
    pygame.display.set_caption("Hormiga borracha browniana")
    return screen

def flip():
    pygame.display.flip()
    time.sleep(0.5)

def main():
    s = inicializar()

    h1 = [100,100,(255,0,0)]
    h2 = [200,100,(0,255,0)]

    while posicionDistinta(h1, h2):
        mover(h1)
        mover(h2)
        visualizar(h1, s)
        visualizar(h2, s)
        flip()
main()

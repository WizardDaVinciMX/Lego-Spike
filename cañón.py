# Simulación gráfica de una bala de cañón
# (c) 2024, José Enrique Álvarez

import time
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():

    g = 10	#Aprox. 9.81 m/seg2
    bx = 0
    by = 0
    vx = 25
    vy = 0

    pygame.init()

    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT)  )
    pygame.display.set_caption("Tiro horizontal")

    while bx < 640 and by < 480:
        screen.fill( (0,0,0) )
        pygame.draw.circle(screen, (255,255,255), (bx, by), 10)
        time.sleep(0.5)
        bx = bx + vx
        by = by + vy
        vy = vy + g
        pygame.display.flip()
main()

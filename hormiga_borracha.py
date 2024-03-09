# Hormiga borracha, o simulación de movimiento browniano
# v. 0.1
# (c) 2024 José Enrique Álvarez Estrada

import pygame
from pygame.locals import *
import time
import random

# Tamaños normales de ventana
# 640x480 VGA
# 800x600 SVGA
# 1024x768 UVGA
# 1366x768 ...
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    PASO = 10

    pygame.init()
    x1 = 1 * SCREEN_WIDTH // 4
    y1 = SCREEN_HEIGHT // 2
    x2 = 3 * SCREEN_WIDTH // 4
    y2 = SCREEN_HEIGHT // 2

    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT)  )
    pygame.display.set_caption("Hormiga borracha browniana")

 #   for t in range(0,500):
    while x1 != x2 or y1 != y2:
        screen.fill( (0,0,0) )
        pygame.draw.circle(screen, (255,0,0), (x1, y1), PASO)
        pygame.draw.circle(screen, (0,255,0), (x2, y2), PASO)
        time.sleep(0.01)
        id1 = random.random()
        ar1 = random.random()
        id2 = random.random()
        ar2 = random.random()
        if id1 > 0.5:
            x1 = x1 + PASO
            if x1 > SCREEN_WIDTH:
                x1 = SCREEN_WIDTH
            elif x1 < 0:
                x1 = 0
        else:
            x1 = x1 - PASO
            x1 = x1 + PASO
            if x1 > SCREEN_WIDTH:
                x1 = SCREEN_WIDTH
            elif x1 < 0:
                x1 = 0
        if ar1 > 0.5:
            y1 = y1 + PASO
        else:
            y1 = y1 - PASO
        if id2 > 0.5:
            x2 = x2 + PASO
        else:
            x2 = x2 - PASO
        if ar2 > 0.5:
            y2 = y2 + PASO
        else:
            y2 = y2 - PASO
        pygame.display.flip()
        
main()
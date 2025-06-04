# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ingame = True
    while ingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill
        pygame.display.flip
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


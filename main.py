# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:  
                if bullet.collision_check(asteroid):
                    bullet.kill()
                    asteroid.split(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over")
                return
            
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit the framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()


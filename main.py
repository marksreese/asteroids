import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from player import Player
import sys

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        frame_time = clock.tick(60)
        dt = frame_time / 1000.0
        screen.fill("black")
    
        updatable.update(dt)
        for object in asteroids:
            if player.collides_with(object):
                log_event("player hit")
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

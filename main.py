import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    msg = (
        f"""Screen width: {SCREEN_WIDTH}\n"""
        f"""Screen height: {SCREEN_HEIGHT}"""
    )
    print(msg)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    x0 = SCREEN_WIDTH / 2
    y0 = SCREEN_HEIGHT / 2
    player = Player(x0, y0)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        for thing in updatable:
            thing.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()

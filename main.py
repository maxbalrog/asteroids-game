import pygame

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

    x0 = SCREEN_WIDTH / 2
    y0 = SCREEN_HEIGHT / 2
    player = Player(x0, y0)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

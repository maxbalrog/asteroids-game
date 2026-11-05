import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    msg = (
        f"""Screen width: {SCREEN_WIDTH}\n"""
        f"""Screen height: {SCREEN_HEIGHT}"""
    )
    print(msg)

if __name__ == "__main__":
    main()

import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle_for_new_astr = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle_for_new_astr)
            velocity2 = self.velocity.rotate(-angle_for_new_astr)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astr1 = Asteroid(self.position[0], self.position[1], new_radius)
            astr2 = Asteroid(self.position[0], self.position[1], new_radius)
            astr1.velocity = 1.2 * velocity1
            astr2.velocity = 1.2 * velocity2

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

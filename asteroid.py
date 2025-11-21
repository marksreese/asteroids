import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white"
            (int(self.x), int(self.y)),
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        asteroid_vector = unit_vector * self.velocity * dt
        self.position += asteroid_vector

    
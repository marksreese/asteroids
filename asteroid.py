import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the original asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        right_velocity = self.velocity.rotate(new_angle)
        left_velocity = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = right_velocity * 1.2
        left_asteroid.velocity = left_velocity * 1.2
    
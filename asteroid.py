import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle) * 1.2
        vec2 = self.velocity.rotate(-angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid01 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid01.velocity = vec1
        new_asteroid02 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid02.velocity = vec2

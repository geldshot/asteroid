import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)

        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid1.velocity = angle1 * 1.2
        asteroid2.velocity = angle2 * 1.2

        
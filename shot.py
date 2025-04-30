import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation


    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        elif self.position.x < 0:
            self.position.x += SCREEN_WIDTH

        if self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        elif self.position.y < 0:
            self.position.y += SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
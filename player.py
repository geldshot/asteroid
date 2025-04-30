from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.speed = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(-dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.accelerate(dt)

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.accelerate(-dt)

        else:
            self.deaccelerate(dt)

        self.move(dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * self.speed * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        elif self.position.x < 0:
            self.position.x += SCREEN_WIDTH

        if self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        elif self.position.y < 0:
            self.position.y += SCREEN_HEIGHT    

    def accelerate(self, dt):
        self.speed += dt * PLAYER_ACCELERATION
        if self.speed > PLAYER_MAX_SPEED:
            self.speed = PLAYER_MAX_SPEED
        if self.speed < -PLAYER_MAX_SPEED:
            self.speed = -PLAYER_MAX_SPEED
    
    def deaccelerate(self, dt):
        if abs(self.speed) < abs(dt * PLAYER_ACCELERATION):
            self.speed = 0
        else:
            self.speed -= dt * PLAYER_ACCELERATION
    

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

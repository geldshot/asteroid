import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    keys = list()
    run = True

    

    while run:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_ESCAPE]:
            run = False

        updateable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                run = False
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        #player.update(dt)    
        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000                            

if __name__ == "__main__":
    main()

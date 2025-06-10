import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    game_dt = 0

    # create groups for entities
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_grp = pygame.sprite.Group()
    shot_grp = pygame.sprite.Group()

    # assign entities to groups
    # pyright would need ClassVar definition, but we ignore this error for now
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_grp, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shot_grp, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(game_dt)

        for asteroid in asteroid_grp:
            if asteroid.check_collision(player):
                print("Game Over!")
                running = False
            for shot in shot_grp:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        game_dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()

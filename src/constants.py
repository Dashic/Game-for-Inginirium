import pygame

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

bullet_img = pygame.Surface((10, 20))
bullet_img.fill((0, 255, 0))
player_img = pygame.transform.scale(pygame.image.load("images/playerr.png"), (60, 60))
enemy_img = pygame.transform.scale(pygame.image.load("images/enemy.png"), (70, 70))




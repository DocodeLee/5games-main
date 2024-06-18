from settings import *
import pygame
import sys
from random import randint, uniform
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/player/down/0.png')
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.mask = pygame.mask.from_surface(self.image)
    
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Vampire Sur")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player(all_sprites)

while True:
    dt = clock.tick(200) / 1000
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    
    
    all_sprites.update(dt)
    display_surface.fill((179, 224, 255))
    all_sprites.draw(display_surface)
    pygame.display.update()
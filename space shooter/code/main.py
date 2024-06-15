import pygame
import sys
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.rect =  self.image.get_frect(center=(window_width / 2, window_height / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300
    def update(self,dt):
        keys = pygame.key.get_pressed()
        recent_keys = pygame.key.get_just_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        
        if recent_keys[pygame.K_SPACE]:
            print("Fire")        

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,window_width),randint(0, window_height)))

class Planet(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,window_width),randint(0, window_height)))
#General setup

pygame.init()
window_width = 1280
window_height = 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Space shooter")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

def load_and_scale_planet(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, size)

pla1 = load_and_scale_planet('images/mars.png',(15,15))
pla2 = load_and_scale_planet('images/neptune.png',(30,15))
pla3 = load_and_scale_planet('images/blue.png',(15,15))

for i in range(10):
    if i % 2 == 0:
        Planet(all_sprites,pla1)
        Planet(all_sprites,pla3)
    else:
        Planet(all_sprites,pla2)
        Planet(all_sprites,pla3)

    
star_surf = pygame.image.load('images/star.png').convert_alpha()
for i in range(30):
    Star(all_sprites,star_surf)
player = Player(all_sprites)

#importing meteor
meteor_surf =pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (window_width / 2, window_height /2 ))

#importing laser
laser_surf = pygame.image.load('images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft =(20 , window_height - 20) )



while True:
    # make a delta time to second
    dt = clock.tick(200) / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #update
    all_sprites.update(dt)
    #draw the game
    display_surface.fill('gray')
    all_sprites.draw(display_surface)
    pygame.display.update()
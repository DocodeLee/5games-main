import pygame
import sys
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.rect =  self.image.get_frect(center=(window_width / 2, window_height / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.life = 2
        
        # cooldown
        self.can_shoot =True
        self.laser_shoot_time = 0
        self.cooldown_duration = 200
    
    def laser_timer(self):
        if not self.can_shoot:
            # check the time
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    
    def movement(self):
        if self.rect.bottom > window_height :
            self.rect.bottom = window_height
        if self.rect.top < 0 :
            self.rect.top = 0
        if self.rect.right > window_width:
            self.rect.right = window_width
        if self.rect.left< 0 :
            self.rect.left = 0
            
    def increase_life(self):
        self.life += 1
      
    def update(self,dt):
        keys = pygame.key.get_pressed()
        recent_keys = pygame.key.get_just_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        self.movement()
            
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            

        self.laser_timer()
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


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos,  groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos )
    
    def update(self, dt):
        ## i need to parse the dt to become framerate-independent
        self.rect.centery -= 800 * dt
        if self.rect.bottom < 0 :
            self.kill()
            
class Meteor(pygame.sprite.Sprite):
    
    def __init__(self,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.meteor_time = pygame.time.get_ticks()
        self.lifetime = 2000
        self.rect =  self.image.get_frect(center = (randint(0, window_width ),randint(-200, -100)))
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(500,800)
        
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.meteor_time > self.lifetime or self.rect.top > window_height :
            self.kill()

class Heart(pygame.sprite.Sprite):

    def __init__(self,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 1600
        self.rect =  self.image.get_frect(center = (randint(0, window_width ),randint(-200, -100)))
        self.direction = pygame.Vector2(uniform(-0.4, 0.4), 1)
        self.speed = randint(400,500)
    def update(self,dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time > self.lifetime :
            self.kill()

def collisions():
    
    collisions_sprites = pygame.sprite.spritecollide(player, meteor_sprites,True)
    if collisions_sprites:
        player.life -= 1
        if player.life == 0 :
            pygame.quit()
            sys.exit()
        
    for laser in laser_sprites:
        collide_sprites = pygame.sprite.spritecollide(laser,meteor_sprites, True)
        if collide_sprites:
            laser.kill()
    heart_collide = pygame.sprite.spritecollide(player,heart_sprites, True)
    if heart_collide and player.life < 2 :
        player.life += 1
    
    print(player.life)
        
    
    
#General setup
pygame.init()
window_width = 1280
window_height = 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Space shooter")
clock = pygame.time.Clock()

#import
laser_surf = pygame.image.load('images/laser.png').convert_alpha()
star_surf = pygame.image.load('images/star.png').convert_alpha()
meteor_surf =pygame.image.load('images/meteor.png').convert_alpha()



all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
heart_sprites = pygame.sprite.Group()

def load_and_scale_planet(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, size)

pla1 = load_and_scale_planet('images/mars.png',(15,15))
pla2 = load_and_scale_planet('images/neptune.png',(30,15))
pla3 = load_and_scale_planet('images/blue.png',(15,15))
heart = load_and_scale_planet('images/heart.png', (100,100))
for i in range(10):
    if i % 2 == 0:
        Planet(all_sprites,pla1)
        Planet(all_sprites,pla3)
    else:
        Planet(all_sprites,pla2)
        Planet(all_sprites,pla3)

    

for i in range(30):
    Star(all_sprites,star_surf)
player = Player(all_sprites)


# custom events -> meteor event
## make a custom event and set the timer for repeat
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 300)

#make extra life
heart_event = pygame.event.custom_type()
pygame.time.set_timer(heart_event,2000)

while True:
    # make a delta time to second
    dt = clock.tick(200) / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            Meteor(meteor_surf,(all_sprites,meteor_sprites))
        if event.type == heart_event:
            #classify in two groups doesn't matter all sprites for display
            # meteor sprites for collision event
            Heart(heart,(heart_sprites, all_sprites))
    #update
    all_sprites.update(dt)
    collisions()
    
    #draw the game
    display_surface.fill('gray')
    all_sprites.draw(display_surface)
    

    
    pygame.display.update()
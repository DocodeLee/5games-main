from settings import *
from math import atan2, degrees

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True
        


class CollisonSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        #player connection
        self.player = player
        self.diistance = 140
        self.player_direction = pygame.Vector2(0,1)
        
        #sprite setup
        super().__init__(groups)
        self.gun_surf =pygame.image.load(join('images','gun','gun.png')).convert_alpha()
        self.image = self.gun_surf
        self.rect =self.image.get_frect(center = self.player.rect.center + self.player_direction * self.diistance)
    
    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2 , WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()

    def rotate_gun(self):
        angle = degrees(atan2(self.player_direction.x , self.player_direction.y)) -90
        if self.player_direction.x > 0 :
            self.image = pygame.transform.rotozoom(self.gun_surf, angle , 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle) , 1)
            self.image = pygame.transform.flip(self.image, False, True)

            
    def update(self, _):
        self.get_direction()
        self.rotate_gun()
        
        self.rect.center = self.player.rect.center + self.player_direction * self.diistance

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surf, pos, direction, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000
        self.direction = direction
        self.speed = 900
        
    def update(self, dt):
        self.rect.center += self.direction *self.speed *dt
        
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()

class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites):
        super().__init__(groups)
        self.player = player
        
        #image
        self.frames, self.frame_index = frames, 0
        self.iamges = self.frames[self.frame_index]
        self.animation_speed = 6
        
        #rect
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-20,-40)
        self.collsion_sprites =collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 400
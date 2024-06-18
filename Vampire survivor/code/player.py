from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('images/player/down/0.png').convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        
        #move
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x= int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
    
    def collision(self, direction):
        pass
    
    def update(self, dt):
        self.input()
        self.move(dt)
        self.collision
        
        
#04:10
from settings import *
from player import Player
from random import randint
from sprites import *
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Sur")
        self.clock = pygame.time.Clock()
        self.running = True
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collison_sprites = pygame.sprite.Group()
        
        self.setup()
        
        #sprites
        self.player = Player((400,300),self.all_sprites,self.collison_sprites)
        
    
    def setup(self):
        map = load_pygame(join('data','maps','world.tmx'))
        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE ,y * TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisonSprite((obj.x, obj.y), obj.image,(self.all_sprites,self.collison_sprites))
        
        for collision in map.get_layer_by_name('Collisions'):
            CollisonSprite((collision.x, collision.y), pygame.Surface((collision.width, collision.height)),self.collison_sprites)
       
    def run(self):
        while self.running:
            
            dt = self.clock.tick() / 1000
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #update
            
            self.all_sprites.update(dt)
            
            #draw
            self.display_surface.fill((0,0,0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
            
        pygame.quit()
                

if __name__ == '__main__':
    game = Game()
    game.run()
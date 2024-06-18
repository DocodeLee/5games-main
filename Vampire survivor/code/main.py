from settings import *
from player import Player
from random import randint
from sprites import CollisonSprite

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
        
        #sprites
        self.player = Player((400,300),self.all_sprites,self.collison_sprites)
        for i in range(6):
            x, y = randint(0,WINDOW_WIDTH) , randint(0, WINDOW_HEIGHT)
            w, h = randint(50,100), randint(100,200)
            CollisonSprite((x,y), (w,h), self.collison_sprites)
            
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
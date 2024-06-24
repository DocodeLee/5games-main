from settings import *

class Player:
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.surface = SIZE
        self.image = pygame.draw.rect(self.surface)
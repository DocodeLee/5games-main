import pygame
import random
#General setup

pygame.init()
window_width = 1280
window_height = 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Space shooter")



# importing an image
player_surf = pygame.image.load('images/player.png').convert_alpha()
x = 100
star_surf = pygame.image.load('images/star.png').convert_alpha()

star_pos = [(random.randint(0, window_width),random.randint(0, window_height)) for i in range(40)]
    # for _ in range(20):
    #     x = random.randint(0, window_width)
    #     y = random.randint(0, window_height)
    #     star_pos.append((x,y))

while True:
    #event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw the game
    #fill the window color
    display_surface.fill('gray')
    for each_pos in star_pos:
        #random position
        display_surface.blit(star_surf,each_pos)
    x += 0.2
    display_surface.blit(player_surf,(x,150))
    pygame.display.update()
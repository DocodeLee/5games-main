import pygame
import random
#General setup

pygame.init()
window_width = 1280
window_height = 720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Space shooter")
clock = pygame.time.Clock()


# importing an image
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center=(window_width / 2, window_height / 2))
player_direction = pygame.math.Vector2()
player_speed = 4

#importing star
star_surf = pygame.image.load('images/star.png').convert_alpha()
star_pos = [(random.randint(0, window_width),random.randint(0, window_height)) for i in range(40)]
    # for _ in range(20):
    #     x = random.randint(0, window_width)
    #     y = random.randint(0, window_height)
    #     star_pos.append((x,y))

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
    #example of getting input
        # if you put the input inside the for loop it just run one
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         print("Left")
        #     if event.key == pygame.K_RIGHT:
        #         print("Right")
        #     if event.key == pygame.K_UP:
        #         print("UP")
        #     if event.key == pygame.K_DOWN:
        #         print("Down")
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         print("Stop left")
        #     if event.key == pygame.K_RIGHT:
        #         print("Stop Right")
        #     if event.key == pygame.K_UP:
        #         print("Stop up")
        #     if event.key == pygame.K_DOWN:
        #         print("Stop Down")
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos
    # input
    keys = pygame.key.get_pressed()
 
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction
    if player_rect.right > window_width:
        player_rect.right = window_width
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > window_height:
        player_rect.bottom = window_height
        ######### Level 2
            # if keys[pygame.K_RIGHT]:
            #     player_direction.x = 1
            # else:
            #     player_direction.x = 0
            ########## i made
            # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #   player_direction.x = 1
            # if event.type == pygame.KEYUP:
                # if event.key == pygame.K_RIGHT:
                #     player_direction.x = 0
    
    #Laser
    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
        print("fire")
    #draw the game
    #fill the window color
    display_surface.fill('gray')
    for each_pos in star_pos:
        #random position
        display_surface.blit(star_surf,each_pos)
    
    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf,laser_rect)
    display_surface.blit(player_surf,player_rect)
    player_rect.center += player_direction * player_speed
    
    pygame.display.update()
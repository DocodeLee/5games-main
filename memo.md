## Display surface is the main surface that we draw on and there can only be one and it is always  visible

## surface is an image, it is only visible when attached to the display surface

## if you don't fill the frame would not be clear so you can see the last frame

## convert() or conver_alpha() high the speed
### convert_alpha is for image which has transparent

## FRects store data as float
## Rects store as integer
### pygame.FRect(pos,size)

## create from a surface
surface.get_rect(pos)
surface.get_frect(pos)


# Vector
## vectors  are excellent way to store direction
## delta time make the movement framerate independent

## rect.center += direction * speed * dt
### independent to the framrate


# Mouse input
## pygame.mouse.get_pos() : get the position
## pygame.mouse.get_pressed() : give the list with 3 items from left, middle to right

## pygame.mouse.get_rel() : get the relative speed of moving

# Key input
## keys = pygame.key.get_pressed()
## if keys[pygame.K_1]:
##   print(1)

# Sprites
## inbuild pygame class that always contains a surface and a rect
## pygame.sprite.Sprite

## blit is for each surface, for group draw will be better

# Working with time
## interval timer
## triggers every x seconds
## create event set a timer

## custom timer
## capture the time start of game

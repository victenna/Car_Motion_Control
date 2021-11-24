import pygame

width=1650
height=900
x0,y0=320,400
x,y=0,5
angle=0
screen = pygame.display.set_mode([width,height])

route=pygame.sprite.Sprite()
route.image=pygame.image.load('route_geometry.png').convert_alpha()
route.rect=route.image.get_rect(center=(850,450))

car=pygame.sprite.Sprite()
CAR=pygame.sprite.Sprite()
car.image=pygame.image.load('vehicle.png').convert_alpha()
car.image=pygame.transform.scale(car.image,(55,90))
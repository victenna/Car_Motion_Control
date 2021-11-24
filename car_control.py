import pygame,math
pygame.init()
screen = pygame.display.set_mode([1650,900])
route=pygame.sprite.Sprite()
route.image=pygame.image.load('route_geometry.png').convert_alpha()
route.rect=route.image.get_rect(center=(850,450))
car=pygame.sprite.Sprite()
CAR=pygame.sprite.Sprite()
car.image=pygame.image.load('vehicle.png').convert_alpha()
car.image=pygame.transform.scale(car.image,(55,90))
x0,y0,x,y,angle=320,400,0,5,0
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:exit()
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        angle=angle-2
        x,y=5*math.sin(3.14*angle/180),5*math.cos(3.14*angle/180)
    if button[pygame.K_RIGHT]:
        angle=angle+2
        x,y=5*math.sin(3.14*angle/180),5*math.cos(3.14*angle/180)
    if button[pygame.K_UP]:
        x0,y0=x0-x,y0-y
    if button[pygame.K_DOWN]:
        x0,y0=x0+x,y0+y
    CAR.image=pygame.transform.rotate\
        (car.image,angle)
    CAR.rect=CAR.image.get_rect(center=(x0,y0))
    screen.fill('green')
    screen.blit(route.image,route.rect)
    screen.blit(CAR.image,CAR.rect)
    result=pygame.sprite.collide_mask(route,CAR)
    if result:
        if button[pygame.K_UP]:
            x0,y0=x0+x,y0+y
        if button[pygame.K_DOWN]:
            x0,y0=x0-x,y0-y
    pygame.display.update()

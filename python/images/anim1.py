import pygame
w=650
h=500
display=pygame.display.set_mode((w,h))
running =True
class Animation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("L1.png")
        self.image.set_colorkey()
        self.rect=self.image.get_rect()
        self.rect.x=w/2
        self.rect.y=h/2
        self.vx=0
        self.vy=0
    def update(self):
        self.vx=0
        self.vy=0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.vx= -5
        elif key[pygame.K_RIGHT]:
            self.vx= 5
        if key[pygame.K_UP]:
            self.vy =-5
        elif key[pygame.K_DOWN]:
            self.vy = 5
        self.rect.x+=self.vx
        self.rect.y+=self.vy
sprites=pygame.sprite.Group()
player=Animation()
sprites.add(player)
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False
            pygame.quit()
            quit()
    sprites.update()
    display.fill((255,151,140))
    sprites.draw(display)
    pygame.display.flip()
import pygame
pygame.init()
w=500
h=500
win=pygame.display.set_mode((w,h))
def load_image(name):
    image= pygame.image.load(name)
    return image
class Animation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
        self.image_left=[]
        self.image_left.append(load_image('C:/Users/juges/Desktop/python/images/L1.png'))
        self.image_left.append(load_image('L2.png'))
        self.image_left.append(load_image('L3.png'))
        self.image_left.append(load_image('L4.png'))
        self.image_left.append(load_image('L5.png'))
        self.image_left.append(load_image('L6.png'))
        self.image_left.append(load_image('L7.png'))
        self.image_left.append(load_image('L8.png'))
        self.image_left.append(load_image('L9.png'))
        self.index=0
        self.image=self.image_left[self.index]
        self.image_right=[pygame.transform.flip(i,True,False) for i in self.image_left]
        self.rect=pygame.Rect(5,5,64,64)
        self.rect.x=w/2
        self.rect.y=h/2
        self.vx=0
        self.vy=0
    def update(self):
        key=pygame.key.get_pressed()
        self.vx=0
        self.vy=0
        
        if key[pygame.K_UP]:
            self.vy += -2
        elif key[pygame.K_DOWN]:
            self.vy += 2
        if key[pygame.K_LEFT]:
            self.vx += -2
            self.index += 1
            if self.index >= len(self.image_left):
            
                self.index = 0
            self.image= self.image_left[self.index]
        
           
        elif key[pygame.K_RIGHT]:
            self.vx += 2
            self.index += 1
            if self.index >= len(self.image_right):
            
                self.index = 0
            self.image= self.image_right[self.index]
            
        self.rect.x+=self.vx
        self.rect.y+=self.vy 
g=pygame.sprite.Group(Animation())
run=True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run=False
            pygame.quit()
            quit()
    g.update()
    
    win.fill((252,20,25))
    g.draw(win)
    
    pygame.display.flip()
        
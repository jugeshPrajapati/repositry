import pygame
from mainSetting import *


pygame.init()
pygame.mixer.init()
v=pygame.math.Vector2
def load_image(name):
    image= pygame.image.load(name)
    return image
class Animation(pygame.sprite.Sprite):
    
    def __init__(self,game):
        
      #  pygame.sprite._layer=PLAYER_LAYER
        self.groups=game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.jumping=False
        self.image_left=[]
        self.image_left.append(load_image(FRAME_PATH+'L1.png'))
        self.image_left.append(load_image(FRAME_PATH+'L2.png'))
        self.image_left.append(load_image(FRAME_PATH+'L3.png'))
        self.image_left.append(load_image(FRAME_PATH+'L4.png'))
        self.image_left.append(load_image(FRAME_PATH+'L5.png'))
        self.image_left.append(load_image(FRAME_PATH+'L6.png'))
        self.image_left.append(load_image(FRAME_PATH+'L7.png'))
        self.image_left.append(load_image(FRAME_PATH+'L8.png'))
        self.image_left.append(load_image(FRAME_PATH+'L9.png'))
        self.index=0
        self.image=self.image_left[self.index]
        self.image_right=[pygame.transform.flip(i,True,False) for i in self.image_left]
        #self.rect=pygame.Rect(5,5,30,30)
       
        self.rect=self.image.get_rect()
        self.rect.center=(width/2,height)
        self.pos=v(width/2,height/2)
        self.vel=v(0,0)
        self.acc=v(0,0)
    def jumpCut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
    def jump1(self,player,platgorm):
        
        self.rect.y += 2
        hits =pygame.sprite.spritecollide(player,platgorm,False)
        self.rect.y -= 2
        if hits and not self.jumping:
            
            self.jumping =True
            self.vel.y = -PLAYER_JUMP_SPEED
            
    def moonJump(self):
        self.vel.y = -MOON_JUMP_SPEED
    def update(self):
        self.acc=v(0,GRAVITY)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.index += 1
            if self.index >= len(self.image_left):
            
                self.index = 0
            self.image= self.image_left[self.index]
        
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.index += 1
            if self.index >= len(self.image_right):
            
                self.index = 0
            self.image= self.image_right[self.index]
        
        
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos.x += self.vel.x + 0.5*self.acc.x
        self.pos.y += self.vel.y + 0.5*self.acc.y
      
        
        
        if self.pos.x >width:
            self.pos.x=0
        if self.pos.x < 0:
            self.pos.x=width
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.midbottom =self.pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,x,y,w):
        self.groups=game.all_sprites,game.mobs,game.platform
        pygame.sprite._layer=ENEMY_LAYER
        pygame.sprite.Sprite.__init__(self,self.groups)
       
        self.image_left=[]
        self.image_left.append(load_image(FRAME_PATH+'L1E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L2E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L3E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L4E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L5E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L6E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L7E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L8E.png'))
        self.image_left.append(load_image(FRAME_PATH+'L9E.png'))
        self.index=0
        self.image=self.image_left[self.index]
        
        self.image_right=[pygame.transform.flip(i,True,False) for i in self.image_left]
        self.image=self.image_right[self.index]
        self.rect=self.image.get_rect()
        
       # self.rect=self.image.get_rect()
       
        self.w=w
        self.x=x
        self.y=y
       # self.rect.midbottom=(self.x,self.y-30)
        self.rect.x=self.x
        self.rect.y=self.y-50
        self.vx=2
        #self.pos=v(self.x,self.y)
        
    def update(self):
        
        
      
        
        if self.vx > 0:
            if self.rect.x < self.x+self.w-self.image.get_width():
            
                self.vx=2
              
                self.index += 1
                if self.index >= len(self.image_right):
                
                    self.index = 0
                  
                self.image= self.image_right[self.index]
                self.rect.x += self.vx 
               
                
            else:
                self.vx=self.vx* -1
           
        else:
            if self.rect.x > self.x :
                
                self.vx = -2
              
            
                self.index += 1
                if self.index >= len(self.image_left):
                
                    self.index = 0
                    
                self.image= self.image_left[self.index]
                self.rect.x += self.vx 
            else:
            
                self.vx= 2
       
            self.mask=pygame.mask.from_surface(self.image)
            
           
     
       
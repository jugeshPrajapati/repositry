import pygame as py
from mainSetting import *
from images.anim5 import *
from mainSprites import  *

from random import randrange,choice
import mainMusic
from os import path
class Game():
    def __init__(self):
        py.init()
        py.mixer.init()
        self.screen=py.display.set_mode((width,height))
        self.info=py.display.Info()
        print(self.info)
        self.bg=py.image.load(path.join('C:/Users/juges/Desktop/python/images','sky.jpg')).convert()
        self.bg1=py.image.load(path.join('C:/Users/juges/Desktop/python/images','brandon-morgan-3qucB7U2l7I-unsplash.jpg')).convert()
        self.bg2=py.image.load(path.join('C:/Users/juges/Desktop/python/images','night_sky.jpg')).convert()
        self.bg3=py.image.load(path.join('C:/Users/juges/Desktop/python/images','night_sky_7.jpg')).convert()
        self.bg4=py.image.load(path.join('C:/Users/juges/Desktop/python/images','david-moum-nbqlWhOVu6k-unsplash.jpg')).convert()
        self.bg_list=choice([self.bg1,self.bg4,self.bg,self.bg2,self.bg3])
        py.display.set_caption("more fun")
        self.clock =py.time.Clock()
        
        self.running =True
        self.font_name = py.font.match_font('italic')
        self.score =0
        self.sink=False
        self.load_data()
        self.newy=0
     
    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir,HS_FILE),'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        
    def new(self):
        self.all_sprites= py.sprite.LayeredUpdates()
        self.platform=py.sprite.Group()
       
        self.mobs=py.sprite.Group()
      
        self.player=Animation(self)
        
        self.all_sprites.add(self.player)
       
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platform.add(p)
        
       
        mainMusic.runP()
        self.run()
        
        
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
   
    def update(self):
        self.all_sprites.update()
        self.mobs.update()
        self.hi =py.sprite.spritecollide(self.player, self.mobs, False,py.sprite.collide_mask)
        if self.hi:
            self.playing = False
         
       
        if self.player.vel.y > 0 :

            self.hits =py.sprite.spritecollide(self.player, self.platform, False)
            if self.hits:
               
                self.lowest = self.hits[0]
                for hit in self.hits:
                    
                    if hit.rect.bottom > self.lowest.rect.bottom:
                        self.lowest=hit
        
                if self.player.pos.y < self.lowest.rect.centery and not self.hi:
                    if self.player.pos.x < self.lowest.rect.right+10 and\
                    self.player.pos.x >self.lowest.rect.left-10:
                        self.player.pos.y= self.lowest.rect.top
                        self.player.vel.y=0
                        self.player.acc.y=0
                        self.player.jumping=False
                        
                else:
                    o=pygame.mixer.Sound('C:/Users/juges/Desktop/python/sounds/jumpsound.wav')
                    o.play()
                    self.player.vel.y=0
                    
                    self.player.moonJump()
                    self.sink=True
               
                   
        if self.player.rect.top <= height/4:
            self.player.pos.y += max(abs(self.player.vel.y),2)
            for plat in self.platform :
                plat.rect.y += max(abs(self.player.vel.y),2)
                #global self.newy
                self.newy=plat.rect.y
                
                if plat.rect.top >= height:
                    self.score += 5
                    plat.kill()
        if self.player.rect.bottom > height:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y,10)
                
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platform) == 0:
            self.playing = False
        while len(self.platform) < 9 :
            self.w=randrange(50,100)
            self.x=randrange(0,width-self.w,self.w)
            self.y=randrange(-80,-30,25)
            p=Platform(self.x,self.y,self.w,20)
            self.all_sprites.add(p)
            self.platform.add(p)
            #self.all_sprites.add(p)
            if self.w > 90:
                
                self.enemy=Enemy(self,self.x,self.y,self.w)
           
                
                
            
                
            
            
 
    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                if self.playing:
                    self.playing=False
                self.running =False
            if event.type == py.KEYDOWN:
                
                if event.key == py.K_UP:
                    #self.jump()
                    o=pygame.mixer.Sound('C:/Users/juges/Desktop/python/sounds/Explosion+1.wav')
                    o.play()
                    self.player.jump1(self.player,self.platform)
            if event.type == py.KEYUP:
                if event.key == py.K_UP:
                    self.player.jumpCut()
            mainMusic.whi(event)
  
    def draw(self):
        #py.display.update()
    
        self.screen.blit(self.bg_list,(0,0))
        self.screen.blit(py.transform.scale(self.bg_list,(width,height)),(0,0))
        self.mobs.draw(self.screen)
        self.all_sprites.draw(self.screen)
       # self.mobs.draw(self.screen)
        
        
       
       # self.screen.blit(self.player.image,self.player.rect)
       
        self.draw_text(str(self.score),22,WHITE,width/2,15)
        #mainMusic.whi()
        if self.sink:
            self.draw_text("moon jump",22,GREEN,150,30)
           
            self.sink =False
        py.display.flip()
       
    def show_start_screen(self):
        mainMusic.bgmusic()
        
        self.screen.fill(EXTRA)
        self.draw_text("jump",48,WHITE,width/2,height/4)
        self.draw_text("arrow to move left and right,up to jump:",22,WHITE,width/2,height/2)
        self.draw_text("press a key  to play:",22,WHITE,width/2,height * 3/4)
        self.draw_text("high score"+str(self.highscore),22,WHITE,width/2,15)
        py.display.flip()
        self.wait_for_key()
    def show_go_screen(self):
        
        self.screen.fill(BLACK)
        py.mixer.music.fadeout(1000)
        mainMusic.bgmus()   
        self.draw_text("GAME OVER",48,WHITE,width/2,height / 4)
        self.draw_text("score:"+str(self.score),22,WHITE,width/2,height/2)
        self.draw_text("press key for play:",22,WHITE,width/2,height*3/4)
        
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("new score" ,22,WHITE,width/2,height/5)
            with open(path.join(self.dir,HS_FILE),'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("high score"+str(self.highscore),22,WHITE,width/2,height/3)
            
                
        py.display.flip()
        self.wait_for_key()
    def draw_text(self,text,size,color,x,y):
        font = py.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)
        
    def wait_for_key(self):
        waiting =True
        while waiting:
            
            self.clock.tick(FPS)
            for event in py.event.get():
                if event.type == py.QUIT:
                    waiting = False
                    self.running =False
                if event.type == py.KEYUP:
                    self.score=0
                    waiting = False


g= Game()
g.show_start_screen()
#m=music_load(MUSIC_PATH)
while g.running:

    g.new()
    g.show_go_screen() 
  
py.quit()


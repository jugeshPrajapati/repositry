'''
Created on 03-Aug-2019

@author: juges
'''
import pygame as py
from random import choice
from mainSetting import *


class Platform(py.sprite.Sprite):
    def __init__(self,x,y,w,h):
        py.sprite._layer=PLATFORM_LAYER
        py.sprite.Sprite.__init__(self)
        
        self.image = py.Surface(( w,h))
        self.image.fill(choice([EXTRA,ORANGE,LITE_YELLOW,LITE_ORANGE,DARK_SKY,LITE_SKY]))
        #self.image.set_colorkey()
        self.rect =self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


        
        
            
        
        
        

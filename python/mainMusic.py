import os
from mainSetting import *
import pygame
pygame.init()
pygame.mixer.init()


MUSIC_ENDED = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_ENDED)
pygame.display.set_mode((width,height))
songs=[]
song_index=0
def load_music(path):
    
    global songs
    for filename in os.listdir(path):
        if filename.endswith('.xoht'):
            songs.append(os.path.join(path, filename))
    return songs


def runP():
    pygame.mixer.init()
    songs = load_music(path='C:/Users/juges/Desktop/python/sounds')

    global song_index  # The current song to load
    pygame.mixer.music.load(songs[song_index])
    pygame.mixer.music.play()
    
    song_index += 1
def whi(event):
          
    if event.type == MUSIC_ENDED:
        global song_index,songs
        song_index = (song_index + 1) % len(songs)  # Go to the next song (or first if at last).
        pygame.mixer.music.load(songs[song_index])
        pygame.mixer.music.play()
        
    pygame.display.update()
def bgmusic():
    pygame.mixer.music.load('C:/Users/juges/Desktop/python/sounds/music.mp3')
    pygame.mixer.music.play()
def bgmus():
    pygame.mixer.music.load('C:/Users/juges/Desktop/python/sounds/coolbeansbgmusic.mp3')
    pygame.mixer.music.play()




import pygame, sys, time, random
from pygame.locals import *
from time import *
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import os
import _thread
import threading
import Fala_volt

d = cmudict.dict()
 
def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
 

dimen_x = 1300
dimen_y = 900
pos_olhoESQ = (dimen_x/4,dimen_y/4)
pos_olhoDIR = ((dimen_x/4)*3,(dimen_y/4))
meio = (dimen_x/2,dimen_y/2)


pygame.init()
windowSurface = pygame.display.set_mode((dimen_x, dimen_y), 0, 32)
pygame.mouse.set_visible(False)
#give me the best depth with a 640 x 480 windowed display

pygame.display.set_caption("VOLT")

pi = 3.14
BLACK = (0, 0, 0)
COR_FUNDO = (2, 105, 182)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
 
info = pygame.display.Info()
sw = info.current_w
sh = info.current_h
y = 0
phrase = "Hi there. How are you doing"
windowSurface.fill(COR_FUNDO)

#OLHO ESQUERDO

pygame.draw.line(windowSurface,WHITE,pos_olhoESQ,(pos_olhoESQ[0]+200,pos_olhoESQ[1]),25)
pygame.draw.circle(windowSurface, WHITE , (int(pos_olhoESQ[0]+100),int(pos_olhoESQ[1])+150), 100, 0)
#OLHO DIREITO

pygame.draw.line(windowSurface,WHITE,pos_olhoDIR,(pos_olhoDIR[0]-200,pos_olhoDIR[1]),25)
pygame.draw.circle(windowSurface, WHITE , (int(pos_olhoDIR[0]-100),int(pos_olhoDIR[1])+150), 100, 0)

# BOCA ABERTA
boca = pygame.image.load('imagens/BocaAberta.png')
boca = pygame.transform.scale(boca, (600, 300))

windowSurface.blit(boca, (pos_olhoESQ[0]+100,(pos_olhoESQ[1]*3)-50))



#[325, 675, 975, 675]
# pygame.draw.circle(windowSurface, YELLOW , (250,200), 80, 0)
# pygame.draw.circle(windowSurface, BLACK,(280,170), 10, 0)
# pygame.draw.circle(windowSurface, BLACK,(220,170), 10, 0)
# pygame.draw.ellipse(windowSurface,BLACK,(225,230,50,10),0)
myfont = pygame.font.SysFont("ComicSans", 35)
pygame.display.update()


sleep(5)
paragraph = "Fala isso ai macaco um dois tres quatro"
#_thread.start_new_thread(saySomething,(paragraph,"pt",))
workingSentence = ""
sleep(0.26)


for phrase in paragraph.split("?"):
	for sentence in phrase.split("."):
	    for word in sentence.split():
	        windowSurface.fill(COR_FUNDO)
	        pygame.draw.circle(windowSurface, YELLOW , (250,200), 80, 0)
	        pygame.draw.circle(windowSurface, BLACK,(280,170), 10, 0)
	        pygame.draw.circle(windowSurface, BLACK,(220,170), 10, 0)
 
	        pygame.draw.ellipse(windowSurface,BLACK,(225,220,50,30),0)
	        myfont = pygame.font.SysFont("ComicSans", 17)
	        workingSentence += word + " "
	        label = myfont.render(workingSentence, 1, BLACK)
	        windowSurface.blit(label, (5, 5))
	        pygame.display.update()
	        sleep(0.165)
 
	        windowSurface.fill(COR_FUNDO)
	        pygame.draw.circle(windowSurface, YELLOW , (250,200), 80, 0)
	        pygame.draw.circle(windowSurface, BLACK,(280,170), 10, 0)
	        pygame.draw.circle(windowSurface, BLACK,(220,170), 10, 0)
 
	        pygame.draw.ellipse(windowSurface,BLACK,(225,230,50,10),0)
	        myfont = pygame.font.SysFont("ComicSans", 17)
	        label = myfont.render(workingSentence, 1, BLACK)
	        windowSurface.blit(label, (5, 5))
	        pygame.display.update()
	        Fala_volt.Voz_alta(word)

	    windowSurface.fill(COR_FUNDO)
	    pygame.draw.circle(windowSurface, YELLOW , (250,200), 80, 0)
	    pygame.draw.circle(windowSurface, BLACK,(280,170), 10, 0)
	    pygame.draw.circle(windowSurface, BLACK,(220,170), 10, 0)
 
	    pygame.draw.ellipse(windowSurface,BLACK,(225,230,50,10),0)
	    myfont = pygame.font.SysFont("ComicSans", 17)
	    label = myfont.render(workingSentence, 1, BLACK)
	    windowSurface.blit(label, (5, 5))
	    pygame.display.update()
	    sleep(0.8)
 
sleep(1)

import pygame as pg
from math import sqrt
import math
from random import randrange,seed
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere

pg.init()
f = pg.display.set_mode(size=(WIND, WIND))
pg.display.set_caption("")
fpsClock = pg.time.Clock()
font = pg.font.SysFont('consolas', 15) #police//roxane
quis=0
b = True
def draw(x,y):
    pg.draw.rect(f,(255,255,255),pg.Rect((x*WIND,WIND/2-y*WIND/2),(10,10)))
coef=2
L=[0 for i in range(int(WIND/10))]
lin=len(L)
userset=False
def src(L,ind):
    if ind<0:
        return math.cos(quis)
    elif ind>lin-1:
        return 0
    else:
        return L[ind]
try:
    while b:
        # Actualiser:
        pg.display.update()

        # Appliquer les images de fond sur la fenetre
        s = pg.Surface((WIND, WIND))  # piqué sur stackoverflow pour avoir un fond avec un alpha
        s.set_alpha()
        s.fill((0, 0, 0))
        f.blit(s, (0, 0))

        text = font.render(str(round(coef,2)), True, (255,255,255))
        textRect = text.get_rect()

        p = pg.key.get_pressed()  # SI la touche est appuyée
    

        for i in range(lin):
            L[i]=(src(L,i-1)*coef+src(L,i+1))/(1+coef)
        for ind,elem in enumerate(L):
            draw(ind/lin,elem)
        del ind,elem
        quis+=1/32
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
                print(" Fin du jeu  babe")
            elif event.type == pg.KEYUP:
                """if event.dict['key']==pg.K_SPACE:
                    
                if event.dict['key']==pg.K_a:"""
                    
            elif event.type==pg.MOUSEBUTTONUP:
                if event.button==1: #click gauche
                    userset=False
                    
                    

                """if event.button==3: #click droit
                   """
                if event.button==4: #vers le haut
                    coef+=0.01
                elif event.button==5: #vers le bas
                    coef-=0.01
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1: #click gauche
                    userset=True
        
        if userset:
            quis=pg.mouse.get_pos()[1]/75
            decal=0
            for i in dir():
                g=font.render(i+" = "+str(eval(i)),1,(255,255,255))
                decal+=g.get_rect().height
                f.blit(g,(0,decal))
        f.blit(text, (0,0))


        fpsClock.tick(FPS)
except :
    pg.quit()
    raise
finally:
    pg.quit()

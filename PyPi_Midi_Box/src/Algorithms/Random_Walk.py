#Credits go to http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
#http://pygame.org/project/1755/3062
#Edits made continue to be made

import pygame
from pygame.locals import *
from math import *
import random
if True:
    print('a')
elif True:
    print('b')
def getstring(iterations):
    s = ['A']
    n=0
    while n<iterations:
        rInt = random.randint(0,3)
        if rInt == 0:
            s.append('A')
        elif rInt == 1:
            s.append('-')
            s.append('-')
            s.append('A')
        elif rInt == '2':
            s.append('-')
            s.append('A')
            n = n+1
            
        elif rInt == '3':
            s.append('-')
            s.append('-')
            s.append('-')
            s.append('A')
        n=n+1
    return s

def main(dim):
    pygame.init()
    screen = pygame.display.set_mode((dim[0], dim[1]),pygame.FULLSCREEN)

    #F -> draw forward
    #+ -> turn right 25 degrees
    #- -> turn left 25 degrees
    #[ -> save position + angle
    #] -> restored position + angle
    
    t=pygame.time.get_ticks()

    iterations = 100000
    s = getstring(iterations)
    print(pygame.time.get_ticks()-t)
    
    t = pygame.time.get_ticks()
    pos = dim[0]/2 ,dim[1]/2
    unit =  5
    angleG = 0
    da = -45
    angle=angleG
    print(s)
    for letter in s:
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
        elif letter == '-':
            angle -= da
         
    print(pygame.time.get_ticks()-t)


    
    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == '__main__':
    main((1920,1080))
#https://en.wikipedia.org/wiki/L-system#Examples_of_L-systems

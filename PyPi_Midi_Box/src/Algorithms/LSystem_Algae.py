#Credits go to http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
#http://pygame.org/project/1755/3062
#Edits made continue to be made

import pygame
from pygame.locals import *
from math import *
if True:
    print('a')
elif True:
    print('b')
def getstring(iterations):
    s = ['A']

    for i in range(1):
        #X -> F-[[X]+X]+F[+FX]-X
        #F-FF
        A_make = ['B','-','A','-','B']
        B_make = ['A','+','B','+','A']        
        j = 0
        n=0
        while n<iterations:

            if s[j] == 'A':
                s.pop(j)
                for item in A_make[::-1]: s.insert(j,item); j=j+1
            elif s[j] == 'B':
                s.pop(j)
                for item in B_make[::-1]: s.insert(j,item);j=j+1
            else:
                j = j+1
            if j>=len(s):
                j=0
            n=n+1
            print(n, ' ', iterations)
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
    pos = dim[0]/dim[0]+5 ,dim[1]/dim[1]+5
    unit = dim[0]/iterations + 2
    angleG = 0
    da = -60
    angle=angleG
    for letter in s:
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
            

        elif letter == '+':
            angle += da
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

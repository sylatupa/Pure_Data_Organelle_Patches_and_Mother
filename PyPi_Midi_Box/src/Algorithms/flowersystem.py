#Credits go to http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
#http://pygame.org/project/1755/3062
#Edits made continue to be made

import pygame
from pygame.locals import *
from math import *

def getstring(iterations):
    s = ['X']

    for i in range(iterations):
        #X -> F-[[X]+X]+F[+FX]-X
        #F-FF
        X_make = ['F', '-', '[', '[', 'X', ']', '+', 'X', ']', '+', 'F', '[', '+', 'F', 'X', ']', '-', 'X']
        F_make = ['F','F']
        j = 0
        while j<len(s):
            if s[j] == 'X':
                s.pop(j)#replace X with our X_make list
                for item in X_make[::-1]: s.insert(j,item)
                j+=17#bump j up to skip over added items
            elif s[j] == 'F':
                s.pop(j)
                for item in F_make[::-1]: s.insert(j,item)
                j+=1
            j+=1
    return s

def main(dim):
    pygame.init()
    screen = pygame.display.set_mode((dim[0], dim[1]))

    #F -> draw forward
    #+ -> turn right 25 degrees
    #- -> turn left 25 degrees
    #[ -> save position + angle
    #] -> restored position + angle
    
    t=pygame.time.get_ticks()
    s = getstring(7)
    print(pygame.time.get_ticks()-t)
    
    t = pygame.time.get_ticks()
    pos = dim[0]/2. -200.,dim[1]
    unit = 2.5
    angle = -70
    da = 20
    saved_angles = []
    saved_poses = []
    for letter in s:
        if letter == 'F':
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
        elif letter == '[':
            saved_poses.append(pos)
            saved_angles.append(angle)
        elif letter == ']':
            pos = saved_poses.pop()
            angle = saved_angles.pop()
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
    main((1000,780))


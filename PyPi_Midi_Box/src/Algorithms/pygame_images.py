import socket
import pygame
import time

host = ""
port = 81    
pygame.init()
screen = pygame.display.set_mode((640,480))
image = pygame.surface.Surface((640, 480))
i=0
j=0
while 1:
    image.fill((i,j,0))
    i+=10
    j+=5
    if i >= 255: i = 0
    if j >= 255: j = 0
    data = pygame.image.tostring(image,"RGB")
    screen.blit(image,(0,0))
    pygame.display.update()
    time.sleep(0.5)

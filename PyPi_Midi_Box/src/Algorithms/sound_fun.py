import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

pygame.mixer.init()
thrust = pygame.mixer.Sound("./Laser Cannon.wav")
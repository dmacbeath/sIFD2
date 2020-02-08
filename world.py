import pygame
import os
from settings import *


def world_map():

    img = pygame.image.load(os.path.join('images', 'wall_1.png')).convert()
    img.convert_alpha()
    img.set_colorkey(black)
    img = pygame.transform.scale(img, (16*2, 16*2))


    return img


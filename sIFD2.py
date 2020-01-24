import pygame
from pygame.locals import *
import sys
import os

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    '''
    spawn player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        self.images = []

        for i in range(0, 3):
            img = pygame.image.load(os.path.join('images', 'spr_' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            # transform.scale(img, (scale up x, scale up y)
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)


           # self.frame = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        # player movement
        self.move_x += x
        self.move_y += y

    def update(self):
        # update player position
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y
        # movement animation here ...

        if self.move_x == 0:
            self.frame = 0
            self.image = self.images[self.frame]

        if self.move_x > 0:
           self.frame = 1
           self.image = self.images[self.frame]

        if self.move_x < 0:
            self.frame = 2
            self.image = self.images[self.frame]


'''
Setup
'''

world_x = 960
world_y = 720
fps = 60
clock = pygame.time.Clock()
pygame.init()


world = pygame.display.set_mode([world_x, world_y])
#backdrop = pygame.image.load(os.path.join('images', 'green.png')).convert()
#backdropbox = world.get_rect()

ALPHA = (255, 255, 255)
BLACK = (23, 23, 23)
# Player setup
player = Player()
player.rect.x = world_x/2
player.rect.y = world_y/2
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 5


main = True
'''
Main Loop
'''

while main:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)


    #world.blit(backdrop, backdropbox)
    world.fill(BLACK)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
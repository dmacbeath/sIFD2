import pygame
from pygame.locals import *
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        self.images_idle = []
        self.facing = 0
        # empty list for right animations
        self.images_run = []
        # img scaling factor
        scale = 5

        for i in range(0, 6):
            img = pygame.image.load(os.path.join('images', 'knight_idle_anim_f' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(black)
            # transform.scale(img, (scale up x, scale up y)
            img = pygame.transform.scale(img, (16*scale, 16*scale))
            self.images_idle.append(img)

        # running sprites
        for i in range(0, 6):
            img = pygame.image.load(os.path.join('images', 'knight_run_anim_f' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(black)
            img = pygame.transform.scale(img, (16*scale, 16*scale))
            self.images_run.append(img)

        self.frame = 0
        self.image = self.images_idle[self.frame]
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
            self.frame += 1
            if self.frame >= len(self.images_idle):
                self.frame = 0
            if self.facing == 0:
                self.image = self.images_idle[self.frame]
            # checks last x movement and flips idle ani if needed
            elif self.facing == 'right':
                self.image = self.images_idle[self.frame]
            elif self.facing == 'left':
                self.image = pygame.transform.flip(self.images_idle[self.frame], True, False)

        if self.move_y < 0:
            self.frame += 1
            if self.frame >= len(self.images_run):
                self.frame = 0
            if self.facing == 0:
                self.image = self.images_run[self.frame]
            elif self.facing == 'right':
                self.image = self.images_run[self.frame]
            elif self.facing == 'left':
                self.image = pygame.transform.flip(self.images_run[self.frame], True, False)

        if self.move_y > 0:
            self.frame += 1
            if self.frame >= len(self.images_run):
                self.frame = 0
            if self.facing == 0:
                self.image = self.images_run[self.frame]
            elif self.facing == 'right':
                self.image = self.images_run[self.frame]
            elif self.facing == 'left':
                self.image = pygame.transform.flip(self.images_run[self.frame], True, False)

        if self.move_x > 0:
            self.frame += 1
            if self.frame >= len(self.images_run):
                self.frame = 0
            self.image = self.images_run[self.frame]
            self.facing = 'right'

        if self.move_x < 0:
            self.frame += 1
            if self.frame >= len(self.images_run):
                self.frame = 0
            self.image = pygame.transform.flip(self.images_run[self.frame], True, False)
            self.facing = 'left'


# Setup
scale = 50
world_x = 16*scale
world_y = 16*scale
fps = 30
clock = pygame.time.Clock()
pygame.init()


world = pygame.display.set_mode([world_x, world_y])
#backdrop = pygame.image.load(os.path.join('images', 'green.png')).convert()
#backdropbox = world.get_rect()

ALPHA = (255, 255, 255)
black = (0, 0, 0)
BLACK = (23, 23, 23)
# Player setup
player = Player()
player.rect.x = world_x/2
player.rect.y = world_y/2
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 5


main = True

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


    # world.blit(backdrop, backdropbox)
    world.fill(BLACK)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)

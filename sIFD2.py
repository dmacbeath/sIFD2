import pygame
import sys
import characters
from settings import *
import world
import os

# Setup
pygame.init()

# set screen size
screen = pygame.display.set_mode([screen_width, screen_height])

# fps
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 18)

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color('green'))
    return fps_text


# background
def grid():
    for x in range(0, screen_width, TILESIZE):
        pygame.draw.line(screen, LIGHTGREY, (x, 0), (x, screen_height))
    for y in range(0, screen_height, TILESIZE):
        pygame.draw.line(screen, LIGHTGREY, (0, y), (screen_width, y))

# draw walls
def bgd():
    screen.fill(BLACK)
    grid()
    screen.blit(update_fps(), (16*3, 16*3))

#def fps_view():
#    pygame.display.update()



# Turn walls into rect objects
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

walls = []
#def wall_map():
x = y = 0
for row in level:
    y += 16 * 2
    x = 0
    for col in row:
        x += 16 * 2
        if col == 'w':
            #screen.blit(world.world_map(), (x-16*2, y-16*2))
            Wall((x-16*2, y-16*2))

#pygame.display.update()



#wall_map()

# Player setup
player = characters.Player()
player.rect.x = screen_width/2
player.rect.y = screen_height/2
player_list = pygame.sprite.LayeredDirty(player)
player_list.clear(screen, bgd())

steps = 5

main = True

while main:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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


    # create player, put in bgd(), draw player on screen
    player.update()
    bgd()

    for wall in walls:
        # blit background and walls on map
        screen.blit(world.world_map(), wall)
        player.checkCollision(wall)


    rects = player_list.draw(screen)

    pygame.display.update(rects)

    clock.tick(fps)

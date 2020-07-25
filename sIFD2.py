import pygame
import sys
from sprites import *
from settings import *
from tilemap import *
import os
import random

# HUD functions

def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align='nw'):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == 'nw':
            text_rect.topleft = (x, y)
        if align == 'ne':
            text_rect.topright = (x, y)
        if align == 'sw':
            text_rect.bottomleft = (x, y)
        if align == 'se':
            text_rect.bottomright = (x, y)
        if align == 'n':
            text_rect.midtop = (x, y)
        if align == 's':
            text_rect.midbottom = (x, y)
        if align == 'e':
            text_rect.midright = (x, y)
        if align == 'w':
            text_rect.midleft = (x, y)
        if align == 'center':
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        self.player_idle_r_img_0 = pygame.image.load(os.path.join('images', PLAYER_IMG[0])).convert_alpha()
        self.player_idle_r_img_1 = pygame.image.load(os.path.join('images', PLAYER_IMG[1])).convert_alpha()
        self.player_idle_r_img_2 = pygame.image.load(os.path.join('images', PLAYER_IMG[2])).convert_alpha()
        self.player_idle_r_img_3 = pygame.image.load(os.path.join('images', PLAYER_IMG[3])).convert_alpha()
        self.player_idle_r_img_4 = pygame.image.load(os.path.join('images', PLAYER_IMG[4])).convert_alpha()
        self.player_idle_r_img_5 = pygame.image.load(os.path.join('images', PLAYER_IMG[5])).convert_alpha()
        self.player_idle_r_img_0 = pygame.transform.scale(self.player_idle_r_img_0, (TILESIZE, TILESIZE))
        self.player_idle_r_img_1 = pygame.transform.scale(self.player_idle_r_img_1, (TILESIZE, TILESIZE))
        self.player_idle_r_img_2 = pygame.transform.scale(self.player_idle_r_img_2, (TILESIZE, TILESIZE))
        self.player_idle_r_img_3 = pygame.transform.scale(self.player_idle_r_img_3, (TILESIZE, TILESIZE))
        self.player_idle_r_img_4 = pygame.transform.scale(self.player_idle_r_img_4, (TILESIZE, TILESIZE))
        self.player_idle_r_img_5 = pygame.transform.scale(self.player_idle_r_img_5, (TILESIZE, TILESIZE))
        self.player_idle_l_img_0 = pygame.transform.flip(self.player_idle_r_img_0, True, False)
        self.player_idle_l_img_1 = pygame.transform.flip(self.player_idle_r_img_1, True, False)
        self.player_idle_l_img_2 = pygame.transform.flip(self.player_idle_r_img_2, True, False)
        self.player_idle_l_img_3 = pygame.transform.flip(self.player_idle_r_img_3, True, False)
        self.player_idle_l_img_4 = pygame.transform.flip(self.player_idle_r_img_4, True, False)
        self.player_idle_l_img_5 = pygame.transform.flip(self.player_idle_r_img_5, True, False)
        self.player_run_r_img_0 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[0])).convert_alpha()
        self.player_run_r_img_1 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[1])).convert_alpha()
        self.player_run_r_img_2 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[2])).convert_alpha()
        self.player_run_r_img_3 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[3])).convert_alpha()
        self.player_run_r_img_4 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[4])).convert_alpha()
        self.player_run_r_img_5 = pygame.image.load(os.path.join('images', PLAYER_RUN_IMG[5])).convert_alpha()
        self.player_run_r_img_0 = pygame.transform.scale(self.player_run_r_img_0, (TILESIZE, TILESIZE))
        self.player_run_r_img_1 = pygame.transform.scale(self.player_run_r_img_1, (TILESIZE, TILESIZE))
        self.player_run_r_img_2 = pygame.transform.scale(self.player_run_r_img_2, (TILESIZE, TILESIZE))
        self.player_run_r_img_3 = pygame.transform.scale(self.player_run_r_img_3, (TILESIZE, TILESIZE))
        self.player_run_r_img_4 = pygame.transform.scale(self.player_run_r_img_4, (TILESIZE, TILESIZE))
        self.player_run_r_img_5 = pygame.transform.scale(self.player_run_r_img_5, (TILESIZE, TILESIZE))
        self.player_run_l_img_0 = pygame.transform.flip(self.player_run_r_img_0, True, False)
        self.player_run_l_img_1 = pygame.transform.flip(self.player_run_r_img_1, True, False)
        self.player_run_l_img_2 = pygame.transform.flip(self.player_run_r_img_2, True, False)
        self.player_run_l_img_3 = pygame.transform.flip(self.player_run_r_img_3, True, False)
        self.player_run_l_img_4 = pygame.transform.flip(self.player_run_r_img_4, True, False)
        self.player_run_l_img_5 = pygame.transform.flip(self.player_run_r_img_5, True, False)
        self.mob_img = pygame.image.load(os.path.join('images', MOB_IMG)).convert_alpha()
        self.bullet_img = pygame.image.load(os.path.join('images', BULLET_IMG)).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join('images', WALL_IMG)).convert_alpha()
        self.treasure_img = pygame.image.load(os.path.join('images', TREASURE_IMG)).convert_alpha()
        self.blood_img = pygame.image.load(os.path.join('images', BLOOD_IMG)).convert_alpha()
        self.item_img = pygame.image.load(os.path.join('images', HEALTH_POTION_IMG)).convert_alpha()
        self.sword_img = pygame.image.load(os.path.join('images', SWORD_IMG)).convert_alpha()
        self.sword_img = pygame.transform.scale(self.sword_img, (int(TILESIZE / 2), TILESIZE))
        self.font = os.path.join('images', 'BitPotionExt.ttf')
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

    def new(self, level):
        self.map = Map('map.txt')
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        # Must spawn player first as Mob needs the player entity for its search function
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'p':
                    self.player = Player(self, col, row)
        mob_spawn_list = []
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '-':
                    mob_spawn_list.append([col, row])
                if tile == 't':
                    Treasure(self, col, row)
                if tile == 'h':
                    Item(self, col, row)
                if tile == 's':
                    self.sword = Sword(self, col, row)
        # spawn number of mobs equal to level at random possible spawn locations
        spawn_coords = random.sample(mob_spawn_list, level**2)
        for i in range(len(spawn_coords)):
            Mob(self, spawn_coords[i][0], spawn_coords[i][1])
        self.camera = Camera(self.map.width, self.map.height)
        self.paused = False


    def run(self, level):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.draw()
            if not self.paused:
                self.update()
        if len(self.mobs) == 0:
            self.show_level_screen()
        if self.player.health <= 0:
            self.show_go_screen(level)
            level = 0

        return level

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # sprite interactions defined here
        self.all_sprites.update()
        self.camera.update(self.player)
        keys = pygame.key.get_pressed()
        # game over if no mobs left
        if len(self.mobs) == 0:
            self.playing = False
        # Collision detection with sprites done here
        # player hits items
        hits = pygame.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.player.add_health(HEALTH_POTION_AMOUNT)
        # player hits sword
        hits = pygame.sprite.spritecollide(self.player, self.swords, False)
        for hit in hits:
            # E key kills sword in world
            if keys[pygame.K_e]:
                hit.kill()
        # mobs hit player
        hits = pygame.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
            if hits:
                self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pygame.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    # def draw_grid(self):
    #     for x in range(0, WIDTH, TILESIZE):
    #         pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
    #     for y in range(0, HEIGHT, TILESIZE):
    #         pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #pygame.display.set_caption(TITLE)
        pygame.display.set_caption('{:.2f}'.format(self.clock.get_fps()))
        self.screen.fill(BLACK)
        #self.draw_grid()

        # HUD functions
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_text('Mobs: {}'.format(len(self.mobs)), self.font, 50, RED, WIDTH-10, 10, align='ne')
        # view hit box
        # pygame.draw.rect(self.screen, RED, self.camera.apply(self.player), 2)
        # pygame.draw.rect(self.screen, RED, self.player.hit_rect, 2)
        # pygame.draw.rect(self.screen, RED, self.camera.apply(self.sword), 2)
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH )
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text('Paused', self.font, 200, RED, WIDTH / 2, HEIGHT / 32 + 24 , align='center')
            self.draw_text('w   up', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 5*24, align='nw')
            self.draw_text('s   down', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 8*24, align='nw')
            self.draw_text('a   left', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 11*24, align='nw')
            self.draw_text('d   right', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 14*24, align='nw')
            self.draw_text('arrow keys   shoot', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 17*24, align='nw')
            self.draw_text('escape   quit', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 20*24, align='nw')
            self.draw_text('p   pause', self.font, 100, RED, WIDTH / 2 - 3*64, HEIGHT / 32 + 23*24, align='nw')
        # if player interacts with sword, display text.
        hits = pygame.sprite.spritecollide(self.player, self.swords, False)
        for hit in hits:
            if hits:
                self.draw_text('press E to pick up', self.font, 50, WHITE, WIDTH / 2, HEIGHT / 32 + 24*5, align='center')

        pygame.display.flip()

    def update_fps(self):
        fps = str(int(clock.get_fps()))
        font = pygame.font.SysFont('Arial', 18)
        fps_text = font.render(fps, 1, pygame.Color('green'))
        return fps_text

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_p:
                    self.paused = not self.paused


    # Menu Screens
    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text('sIFD2', self.font, 200, RED, WIDTH / 2, HEIGHT / 2, align='center')
        self.draw_text('Press SPACE to start', self.font, 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align='center')
        pygame.display.flip()
        self.wait_for_key()

    def show_level_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(('Wave ' + str(level) + ' Survived'), self.font, 200, RED, WIDTH / 2, HEIGHT / 2, align='center')
        self.draw_text('Press SPACE to go to next level', self.font, 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align='center')
        pygame.display.flip()
        self.wait_for_key()


    def show_go_screen(self, level):
        self.screen.fill(BLACK)
        self.draw_text('Game over', self.font, 200, RED, WIDTH / 2, HEIGHT / 2 - 100, align='center')
        self.draw_text(('You reached level ' + str(level)), self.font, 100, RED, WIDTH / 2, HEIGHT * 3 / 4 - 100, align='center')
        self.draw_text('Press SPACE to restart', self.font, 75, WHITE, WIDTH / 2, HEIGHT * 4 / 4 - 100, align='center')
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        waiting = False

g = Game()
g.show_start_screen()
level = 1
while True:
    g.new(level)
    #g.run(level)
    level = 1 + g.run(level)
    #g.show_go_screen(level)

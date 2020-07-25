import pygame
import os
from random import uniform, choice, randint
from settings import *
from tilemap import collide_hit_rect
import pytweening as tween
vec = pygame.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_idle_r_img_0
        self.image_idle_r = [game.player_idle_r_img_1, game.player_idle_r_img_2, game.player_idle_r_img_3, game.player_idle_r_img_4, game.player_idle_r_img_5]
        self.image_idle_l = [game.player_idle_l_img_1, game.player_idle_l_img_2, game.player_idle_l_img_3, game.player_idle_l_img_4, game.player_idle_l_img_5]
        self.image_run_r = [game.player_run_r_img_0, game.player_run_r_img_1, game.player_run_r_img_2, game.player_run_r_img_3, game.player_run_r_img_4, game.player_run_r_img_5]
        self.image_run_l = [game.player_run_l_img_0, game.player_run_l_img_1, game.player_run_l_img_2, game.player_run_l_img_3, game.player_run_l_img_4, game.player_run_l_img_5]
        self.frame = 0
        self.facing = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.last_shot = 0
        self.rot = 0
        self.health = PLAYER_HEALTH
        self.elasped = 0

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel.x = - PLAYER_SPEED
        if keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pygame.K_w]:
            self.vel.y = - PLAYER_SPEED
            self.rot = 90
        if keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            self.rot = 270
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
            # shooting directions
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                if keys[pygame.K_RIGHT]:
                    self.rot = 0
                if keys[pygame.K_LEFT]:
                    self.rot = 180
                if keys[pygame.K_UP]:
                    self.rot = 90
                if keys[pygame.K_DOWN]:
                    self.rot = 270
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)
                # knockback setting for player, makes animation flip horizontally due to amatuerish logic
                # self.vel = vec(-KNOCKBACK, 0).rotate(-self.rot)

    def update(self):
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        # animation speed
        if pygame.time.get_ticks() - self.elasped > animation_interval:
            self.elasped = pygame.time.get_ticks()
            self.animate()

    def animate(self):
        if self.vel.x == 0:
            self.frame += 1
            if self.frame >= len(self.image_idle_r):
                self.frame = 0
            self.image = self.image_idle_r[self.frame]
            if self.facing == 'right':
                self.image = self.image_idle_r[self.frame]
            elif self.facing == 'left':
                self.image = self.image_idle_l[self.frame]

        if self.vel.x > 0:
            self.frame += 1
            if self.frame >= len(self.image_run_r):
                self.frame = 0
            self.image = self.image_run_r[self.frame]
            self.facing = 'right'

        if self.vel.x < 0:
            self.frame += 1
            if self.frame >= len(self.image_run_l):
                self.frame = 0
            self.image = self.image_run_l[self.frame]
            self.facing = 'left'

        if self.vel.y > 0:
            self.frame += 1
            if self.frame >= len(self.image_run_r):
                self.frame = 0
            if self.facing == 0:
                self.image = self.image_run_r[self.frame]
            elif self.facing == 'right':
                self.image = self.image_run_r[self.frame]
            elif self.facing == 'left':
                self.image = self.image_run_l[self.frame]

        if self.vel.y < 0:
            self.frame += 1
            if self.frame >= len(self.image_run_r):
                self.frame = 0
            if self.facing == 0:
                self.image = self.image_run_r[self.frame]
            elif self.facing == 'right':
                self.image = self.image_run_r[self.frame]
            elif self.facing == 'left':
                self.image = self.image_run_l[self.frame]

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        self._layer = MOB_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img.copy()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = MOB_HEALTH
        self.speed = choice(MOB_SPEED)
        self.target = game.player

    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < MOB_AVOID_RADIUS:
                    self.acc += dist.normalize()

    def update(self):
        target_dist = self.target.pos - self.pos
        #if target_dist.length_squared() < MOB_DETECT_RADIUS**2:
        self.rot = target_dist.angle_to(vec(1, 0))
        #self.image = pygame.transform.rotate(self.game.mob_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(1, 0).rotate(-self.rot)
        self.avoid_mobs()
        self.acc.scale_to_length(self.speed)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:
            self.kill()
            Effects(self.game, self.pos)

    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / MOB_HEALTH)
        self.health_bar = pygame.Rect(0, 0, width, 7)
        if self.health < MOB_HEALTH:
            pygame.draw.rect(self.image, col, self.health_bar)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets
        self._layer = BULLET_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-BULLET_SPREAD, BULLET_SPREAD)
        self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        self._layer = WALL_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Treasure(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        self._layer = WALL_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.treasure_img
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Effects(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites
        self._layer = WALL_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        size = randint(20, 50)
        self.image = pygame.transform.scale(game.blood_img, (size, size))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > BLOOD_DURATION:
            self.kill()


class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.items
        self._layer = WALL_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_img
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        # self.x = x
        # self.y = y
        self.rect.center = (x, y)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vec(x, y) * TILESIZE
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        # bobbing motion
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1

class Sword(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.swords
        self._layer = WALL_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.sword_img
        self.rect = self.image.get_rect()
        # self.x = x
        # self.y = y
        self.rect.center = (x, y)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vec(x, y) * TILESIZE
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        # bobbing motion
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1

 ## animation dragons

# empty list for right animations
# self.images_run = []

# self.frame = 0
# self.images_idle = []
# self.facing = 0
# for i in range(0, 6):
#     img = pygame.image.load(os.path.join('images', 'knight_idle_anim_f' + str(i) + '.png')).convert()
#     img.convert_alpha()
#     img.set_colorkey(black)
#     # transform.scale(img, (scale up x, scale up y)
#     img = pygame.transform.scale(img, (16*scale, 16*scale))
#     self.images_idle.append(img)
#
# # running sprites
# for i in range(0, 6):
#     img = pygame.image.load(os.path.join('images', 'knight_run_anim_f' + str(i) + '.png')).convert()
#     img.convert_alpha()
#     img.set_colorkey(black)
#     img = pygame.transform.scale(img, (16*scale, 16*scale))
#     self.images_run.append(img)

# self.frame = 0
# self.image = self.images_idle[self.frame]
# self.rect = self.image.get_rect()






        # movement animation here ...
        # self.dirty = 1
        # if self.move_x == 0:
        #     self.frame += 1
        #     if self.frame >= len(self.images_idle):
        #         self.frame = 0
        #     if self.facing == 0:
        #         self.image = self.images_idle[self.frame]
        #     # checks last x movement and flips idle ani if needed
        #     elif self.facing == 'right':
        #         self.image = self.images_idle[self.frame]
        #     elif self.facing == 'left':
        #         self.image = pygame.transform.flip(self.images_idle[self.frame], True, False)
        #
        # if self.move_y < 0:
        #     self.frame += 1
        #     if self.frame >= len(self.images_run):
        #         self.frame = 0
        #     if self.facing == 0:
        #         self.image = self.images_run[self.frame]
        #     elif self.facing == 'right':
        #         self.image = self.images_run[self.frame]
        #     elif self.facing == 'left':
        #         self.image = pygame.transform.flip(self.images_run[self.frame], True, False)
        #
        # if self.move_y > 0:
        #     self.frame += 1
        #     if self.frame >= len(self.images_run):
        #         self.frame = 0
        #     if self.facing == 0:
        #         self.image = self.images_run[self.frame]
        #     elif self.facing == 'right':
        #         self.image = self.images_run[self.frame]
        #     elif self.facing == 'left':
        #         self.image = pygame.transform.flip(self.images_run[self.frame], True, False)
        #
        # if self.move_x > 0:
        #     self.frame += 1
        #     if self.frame >= len(self.images_run):
        #         self.frame = 0
        #     self.image = self.images_run[self.frame]
        #     self.facing = 'right'
        #
        # if self.move_x < 0:
        #     self.frame += 1
        #     if self.frame >= len(self.images_run):
        #         self.frame = 0
        #     self.image = pygame.transform.flip(self.images_run[self.frame], True, False)
        #     self.facing = 'left'

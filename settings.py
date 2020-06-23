import pygame
vec = pygame.math.Vector2

TITLE = 'sIFD2'

WIDTH = 1024
HEIGHT = 768 # 64*12, 32*24
TILESIZE = 64
# 32 tiles across, 24 tiles down

fps = 60
animation_interval = 30

ALPHA = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (23, 23, 23)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

WALL_IMG = 'wall_top.png'

# Player settings
PLAYER_HEALTH = 500
PLAYER_SPEED = 500
PLAYER_IMG = ['knight_idle_anim_f0.png', 'knight_idle_anim_f1.png', 'knight_idle_anim_f2.png', 'knight_idle_anim_f3.png', 'knight_idle_anim_f4.png', 'knight_idle_anim_f5.png']
PLAYER_RUN_IMG = ['knight_run_anim_f0.png', 'knight_run_anim_f1.png', 'knight_run_anim_f2.png', 'knight_run_anim_f3.png', 'knight_run_anim_f4.png', 'knight_run_anim_f5.png']
PLAYER_HIT_RECT = pygame.Rect(0, 0, 12*4, 12*4)
BARREL_OFFSET = vec(30, 10)

# Projectile settings
BULLET_IMG = 'fireball.png'
BULLET_SPEED = 1000
BULLET_LIFETIME = 1000
BULLET_RATE = 100
KICKBACK = 200
BULLET_SPREAD = 5
BULLET_DAMAGE = 10

# Mob settings
MOB_IMG = 'mob.png'
MOB_SPEED = [200, 150, 125, 175]
MOB_HIT_RECT = pygame.Rect(0, 0, 12*4, 15*4)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 10
MOB_AVOID_RADIUS = 50
MOB_DETECT_RADIUS = 400

# Treasure
TREASURE_IMG = 'treasure.png'

# Effects
BLOOD_IMG = 'blood.png'
BLOOD_DURATION = 2000

# Items
HEALTH_POTION_IMG = 'Food.png'
HEALTH_POTION_AMOUNT = 250
BOB_RANGE = 30
BOB_SPEED = 0.4

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECT_LAYER = 4

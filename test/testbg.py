import os, sys
import pygame
from pygame.locals import *
from Box2D import *

from physics import BallBody, RobotBody
from ui import BallSprite, RobotSprite, Camera
import conf


pygame.init()

size = (700,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Capture the Flag')
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()
bg = pygame.image.load(os.path.join('images','field.png'))

robot_size = (22,22)
ball_size = (12,12)

rs = RobotSprite('30', robot_size, (200,200))
bs = BallSprite('Ball', ball_size, (444,444))

robot_sprites = pygame.sprite.RenderPlain(rs)
ball_sprites = pygame.sprite.RenderPlain(bs)

world = b2World(gravity=(0,0))

rb = RobotBody(world, '30', conf.g2b_pos((200,200)))
bb = BallBody(world, 'Ball', conf.g2b_pos((444,444)))

fps = 60
dt = 1.0/fps
vel_iters = 10
pos_iters = 10

while True:
    clock.tick(fps)
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            pygame.quit()
            sys.exit(0)

    rb.set_linear_impulse(0.05,0.05)
    # rb.set_angular_impulse(0.05,0.05,dt)
    world.Step(dt, vel_iters, pos_iters)

    rs.set_pos(conf.b2g_pos(rb.get_pos()))
    rs.rotate(conf.b2g_angle(rb.get_angle()))
    bs.set_pos(conf.b2g_pos(bb.get_pos()))

    screen.blit(bg,(0,0))
    robot_sprites.update()
    robot_sprites.draw(screen)
    ball_sprites.update()
    ball_sprites.draw(screen)
    pygame.display.flip()

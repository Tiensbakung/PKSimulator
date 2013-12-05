#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Entry point for simulator. Intended for behaviour with no
team communication.
'''

from datetime import timedelta
import itertools
import logging
import sys
import time

import pygame
from pygame.locals import *
import Box2D

import conf
from pk_architecture import pk_set_debug_options
import ui

field_width = 700
field_height = 600
screen_size = (field_width+500, field_height)
robot_info_list = (
    ('31', (52.0, -43.0), 0, '31', 'defender', 'blue'),
    ('32', (45, -43), 0, '32', 'collector', 'red'),
)
ball_info_list = (
    ('ball', (12, -12)),
    ('ball', (45, -40)),
    ('ball', (30, -30))
)


def main():
    pk_set_debug_options(warning=False,
                         trace=False,
                         debug=True,
                         info=False,
                         verbous=False)
    logging.basicConfig(level=logging.WARN)
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    gw = ui.GameWindow(screen)
    allsprites = pygame.sprite.RenderUpdates()
    clock = pygame.time.Clock()

    world = Box2D.b2World(gravity=(0,0))
    lwall, rwall, twall, bwall = conf.create_playground(world)
    rbl = []                    # robot body list
    rsl = []                    # robot sprite list
    rrl = []                    # robot role list
    bbl = []                    # ball body list
    bsl = []                    # ball sprite list

    for ID,pos,heading,leader,role,team in robot_info_list:
        body, sprite, role = conf.create_robot(ID, pos, heading,
                                               world, leader, role, team)
        rbl.append(body)
        rsl.append(sprite)
        rrl.append(role)

    for name,pos in ball_info_list:
        body, sprite = conf.create_ball(name, pos, world)
        bbl.append(body)
        bsl.append(sprite)

    allsprites.add(rsl)
    allsprites.add(bsl)
    gw.add_spritegroup(allsprites)
    fps = 60
    dt = 1.0 / 60
    vel_iters = 10
    pos_iters = 10
    t0 = time.time()
    counter = 0

    while True:
        clock.tick(fps)
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        wb_r_data = conf.build_wb_robot_data(rbl)
        wb_o_data = conf.build_wb_object_data(bbl)
        for i, body, role in itertools.izip(range(len(rbl)), rbl, rrl):
            if not counter:
                vi_r_data = conf.build_vi_robot_data(body, role,
                                                     itertools.izip(rbl, rrl))
                vi_o_data = conf.build_vi_object_data(body, role, bbl)
                in_grabber = conf.object_in_grabber(body, role, bbl)
                print vi_r_data
                print vi_o_data
                role.feed_workbench_data(wb_r_data, wb_o_data)
                role.feed_vision_data(vi_r_data, vi_o_data, in_grabber)
                role.run()
            l, r = conf.get_speed(role.speed())
            li = body.set_linear_impulse(l, r, dt)
            ai = body.set_angular_impulse(l, r, dt)
            text = '{}: {} [{}]'.format(role.ID, role.role, role.state)
            gw.add_dynamictext(text, (705, 120 + 20*i))
        counter = (counter + 1) % 11

        world.Step(dt, vel_iters, pos_iters)
        world.ClearForces()

        score_red = 0
        score_blue = 0
        for body, sprite in itertools.izip(rbl, rsl):
            sprite.set_pos(conf.b2g_pos(body.get_pos()))
            sprite.rotate(conf.b2g_angle(body.get_angle()))

        for body, sprite in itertools.izip(bbl, bsl):
            sprite.set_pos(conf.b2g_pos(body.get_pos()))
            sprite.rotate(conf.b2g_angle(body.get_angle()))
            score_red += sprite.score_red
            score_blue += sprite.score_blue

        running_time = timedelta(seconds=int(time.time()-t0))
        gw.add_dynamictext('Time: {}'.format(running_time), (705,20))
        gw.add_dynamictext('Team Red: {}'.format(score_red), (705,50))
        gw.add_dynamictext('Team Blue: {}'.format(score_blue), (705,70))
        gw.update()


if __name__ == '__main__':
    main()

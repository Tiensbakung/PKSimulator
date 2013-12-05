#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

import ui

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    gw = ui.GameWindow(screen)
    clock = pygame.time.Clock()

    rs = ui.RobotSprite('30', (24,24), (200,200))
    bs = ui.BallSprite('Ball', (12,12), (400,400))
    allsprites = pygame.sprite.RenderUpdates((rs,bs))
    gw.add_spritegroup(allsprites)

    fps = 60

    gw.add_statictext('Catch the Flag', (710,20))
    counter = 0

    while True:
        clock.tick(fps)
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        counter += 1
        gw.add_dynamictext('Frames: {}'.format(counter), (710,60))
        gw.update()


if __name__ == '__main__':
    main()
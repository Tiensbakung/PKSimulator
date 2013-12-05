#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import pygame

from basesprite import BaseSprite


class RobotSprite(BaseSprite):

    def __init__(self, ID, color, size, position, heading=0):
        BaseSprite.__init__(self, size, position, heading)
        self.ID = ID
        p = os.path.join('images', 'Robot.png')
        img = Image.open(p)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('Arial_Bold.ttf', 14)
        draw.text((7,1), ID, color, font)
        self.image_origin = pygame.image.frombuffer(img.tostring(),
                                                    img.size, img.mode)
        self.image_origin = self.image_origin.convert_alpha()
        self.image = pygame.transform.scale(self.image_origin, size)
        self.image = pygame.transform.rotate(self.image, heading)
        self.rect = self.image.get_rect()
        self.size = size

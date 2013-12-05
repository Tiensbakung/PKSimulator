#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pygame

class GameWindow:

    def __init__(self,
                 screen,
                 caption='Catch the Flag',
                 bg_file='field.png'):
        self.screen = screen
        self.bg = pygame.image.load(os.path.join('images', bg_file))
        self.font = pygame.font.Font(None, 24)
        self.sprite_groups = []
        self.static_texts = {}
        self.dynamic_texts = {}

    def add_spritegroup(self, sg):
        self.sprite_groups.append(sg)

    def add_dynamictext(self, text, pos, color=(255,255,255)):
        surface = self.font.render(text, True, color)
        self.dynamic_texts[text] = pos, surface, color

    def add_statictext(self, text, pos, color=(255,255,255)):
        surface = self.font.render(text, True, color)
        self.static_texts[text] = pos, surface, color

    def del_statictext(self, text):
        try:
            del self.static_texts[text]
        except KeyError:
            pass

    def update(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0,0))
        for v in self.static_texts.itervalues():
            pos, surface = v[0], v[1]
            self.screen.blit(surface, pos)
        for v in self.dynamic_texts.itervalues():
            pos, surface = v[0], v[1]
            self.screen.blit(surface, pos)
        self.dynamic_texts.clear()

        for group in self.sprite_groups:
            group.update()
            group.draw(self.screen)
        pygame.display.flip()
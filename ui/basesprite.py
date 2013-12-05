import pygame
import os
class BaseSprite(pygame.sprite.Sprite):

    def __init__(self, size, position, heading=0, filename=None):
        pygame.sprite.Sprite.__init__(self)
        if filename:
            p = os.path.join('images',filename)
            self.image_origin = pygame.image.load(p).convert_alpha()
            self.image = pygame.transform.scale(self.image_origin, size)
            self.image = pygame.transform.rotate(self.image, heading)
            self.rect = self.image.get_rect()
            self.size = size
        self.pos = position
        self.angle = heading

    def rotate(self, angle):
        if self.angle != angle:
            self.angle = angle
            self.image = pygame.transform.scale(self.image_origin,self.size)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect()

    def resize(self, size):
        if self.size != size:
            self.size = size
            self.image = pygame.transform.scale(self.image_origin,self.size)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect()

    def set_pos(self, position):
        self.pos = position

    def update(self):
        self.rect.center = self.pos

import pygame, sys, os
import math
from pygame.locals import *

class OutOfCamera(Exception):
    def __init__(self, message, Errors):
        Exception.__init__(self, Errors)
        self.Errors = Errors

class Camera:

    def __init__(self,origin, size, ratio=100, zoom_factor=1):
        self.origin = origin
        self.size = size
        self.ratio = ratio
        self.zoom_factor = zoom_factor

    def get_x(self, x):
        if math.fabs(x-self.origin[0]) > self.size[0]:
            raise OutOfCamera('Object is out of Camera')
        return (x-self.origin[0])*self.zoom_factor*self.ratio

    def get_y(self, y):
        if math.fabs(y-self.origin[1]) > self.size[1]:
            raise OutOfCamera('Object is out of Camera')
        return (y-self.origin[1])*self.zoom_factor*self.ratio

    def get_pos(self, pos):
        return (self.get_x(pos[0]),self.get_y(pos[1]))

    def get_angle(self, angle):
        return math.degrees(angle)%360

    def zoom_in(self, delta):
        self.zoom_factor += delta

    def zoom_out(self, delta):
        self.zoom_factor -= delta

    def zoom_normal(self):
        self.zoom_factor = 1

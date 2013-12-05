#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

bg_ratio = 10.0                 # 1 meter in Box2D = 100 pixels in pygame
bw_ratio = 100.0                # Box2D (1 meter) = workbench (100 mm)
rb_ratio = 10.0                 # 1 meter in reality = 10 meter in simulation


# Box2D to pygame
def b2g_angle(angle):
    return math.degrees(angle) % 360

def b2g_pos(pos):
    return b2g_x(pos[0]), b2g_y(pos[1])

def b2g_x(x):
    return (x - 0.185*rb_ratio) * bg_ratio + 32

def b2g_y(y):
    return (-y - 0.430*rb_ratio) * bg_ratio + 32


# Box2D to Vision
def b2v_angle(angle):
    return (math.degrees(angle) + 180) % 360

def b2v_pos(pos):
    return b2v_x(pos[0]), b2v_y(pos[1])

def b2v_x(x):
    return x / rb_ratio

def b2v_y(y):
    return -y / rb_ratio


# Box2D to Workbench
def b2w_angle(angle):
    return (math.degrees(angle) + 180) % 360

def b2w_pos(pos):
    return b2w_x(pos[0]), b2w_y(pos[1])

def b2w_x(x):
    return x * bw_ratio

def b2w_y(y):
    return -y * bw_ratio


# pygame to Box2D
def g2b_angle(angle):
    return math.radians(angle % 360)

def g2b_pos(pos):
    return g2b_x(pos[0]), g2b_y(pos[1])

def g2b_x(x):
    return (x-32)/bg_ratio - 0.185*rb_ratio

def g2b_y(y):
    return -(y-32)/bg_ratio - 0.430*rb_ratio

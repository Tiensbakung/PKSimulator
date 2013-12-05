#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Box2D import *

import physics
import conf

dt = 1.0 / 60
vel_iters = 10
pos_iters = 10
world = b2World(gravity=(0,0))
body = physics.RobotBody(world, '1', (0.0774193447035, 0))
print body.get_pos(), conf.b2g_angle(body.get_angle())
for i in range(3):
    body.set_linear_impulse(-2, -2)
    body.set_angular_impulse(-2, -2, dt)
    world.Step(dt, vel_iters, pos_iters)
    print body.get_pos(), conf.b2g_angle(body.get_angle())

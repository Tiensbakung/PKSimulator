#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Box2D import *

import physics
import behaviour
import conf

robot_info_list = (
    ('1', (1.3,1.3), 0, 'collector', 'blue'),
    ('2', (1.8,1.8), 0, 'collector', 'blue'),
    ('3', (2.1,2.1), 0, 'collector', 'blue'),
    ('4', (2.5,2.5), 0, 'collector', 'red'),
    ('5', (2.8,2.8), 0, 'collector', 'red'),
    ('6', (3.2,3.2), 0, 'collector', 'red')
)
ball_info_list = (
    ('Ball', (3,3)),
    ('Ball', (4.0,4.0))
)

world = b2World()
rbl = []                    # robot body list
rrl = []                    # robot role list
bbl = []                    # ball body list
bsl = []                    # ball sprite list

for ID,pos,heading,role,team in robot_info_list:
    body = physics.RobotBody(world, ID, pos)
    size = int(body.width*conf.bg_ratio), int(body.height*conf.bg_ratio)
    role = behaviour.RobotRole(ID, role, team)
    rbl.append(body)
    rrl.append(role)

for name,pos in ball_info_list:
    body = physics.BallBody(world, name, pos)
    bbl.append(body)

print conf.build_wb_robot_data(rbl)
print conf.build_wb_object_data(bbl)

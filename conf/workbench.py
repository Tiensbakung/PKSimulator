#!/usr/bin/env python
# -*- coding: utf-8 -*-
import coord


def build_wb_object_data(object_list):
    L = []
    for object in object_list:
        pos = coord.b2w_pos(object.get_pos())
        L.append((object.name.capitalize(), pos[0], pos[1]))
    return L


def build_wb_robot_data(robot_list):
    D = {}
    for robot in robot_list:
        pos = coord.b2w_pos(robot.get_pos())
        heading = coord.b2w_angle(robot.get_angle())
        D[robot.ID] = pos[0], pos[1], heading
    return D

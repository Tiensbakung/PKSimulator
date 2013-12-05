#!/usr/bin/env python
# -*- coding: utf-8 -*-
import coord
import vision_simulated as vis
import math

DIST_THRESHOLD = 75.06 # 7.506 cm
ANGLE_THRESHOLD = math.radians(2.2906) # in degrees

def build_vi_object_data(body, role, object_list):
    message = []
    body_pos = coord.b2v_pos(body.get_pos())
    body_angle =  coord.b2v_angle(body.get_angle()) # degrees
    for obj in object_list: # loop through all the objects on the play ground
        objects = {}
        obj_pos = coord.b2v_pos(obj.get_pos())
        mass, angle = vis.distance2mass(body_pos, body_angle, obj_pos)
        if mass and angle: # if the object is recognized by the vision
            dist = vis.mass2distance(mass)
            objects['object_type'] = obj.name
            objects['distance'] = dist
            objects['angle'] = angle
            message.append(objects)
    return message

def build_vi_robot_data(body, role, robot_list):
    message = []
    body_pos = coord.b2v_pos(body.get_pos())
    body_angle = coord.b2v_angle(body.get_angle())
    for b, r in robot_list: # loop through all the robots on the play ground
        objects = {}
        b_pos = coord.b2v_pos(b.get_pos())
        eheight, angle = vis.distance2eheight(body_pos, body_angle, b_pos)
        if eheight and angle: # if the robot is recognized by the vision
            dist = vis.eheight2distance(eheight)
            objects['object_type'] = r.team + '_robot'
            objects['distance'] = dist
            objects['angle'] = angle
            message.append(objects)
    return message

def object_in_grabber(body, role, object_list):
    body_pos = coord.b2v_pos(body.get_pos())
    body_angle =  coord.b2v_angle(body.get_angle()) # degrees
    for obj in object_list:
        obj_pos = coord.b2v_pos(obj.get_pos())
        mass, angle = vis.distance2mass(body_pos, body_angle, obj_pos)
        if mass and angle:
            dist = vis.mass2distance(mass)
            if dist <= DIST_THRESHOLD and abs(angle) <= ANGLE_THRESHOLD:
                return True
    return False
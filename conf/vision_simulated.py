#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

MAX_VIEW_RANGE = 1 #(in meters) Maximum distance a robot vision can detect an object
MAX_VIEW_ANGLE = 60 #(in degrees) Maximum viewing angle form the center to each side.

def angle_range(heading, theta):
    diff = abs(heading - theta)
    if diff >= 180:
        diff = diff - 360
    if heading > theta:
        return -diff
    else:
        return diff

def angle2pix_distance(angle):
    """Convert to Pixel Distance
    Input : real angle to object (in radians)
    returns : pixel distance corresponds to the angle
    """
    dist = (angle - 0.004074246) / 0.005993035
    return round(dist)

def distance(pos1, pos2):
    """Distance between two objects
    Input : Positions of two objects (x1, y1), (x2, y2).

    returns : Euclidean distance sqrt((x2 - x1)**2 + (y2 - y1)**2)
    """
    dist = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
    if dist < MAX_VIEW_RANGE:    # distance restricted to 1000 mm (1m)
        return dist * 1000
    else:
        return None

def distance2angle(robot_pos, heading, object_pos):
    """Angle Model
    Input : viewing robot position, angle of deviation
    from the real world (heading), object position.

    returns : angle according to the local coordinates (in radians).
    """
    dist = distance(robot_pos, object_pos)
    if dist:
        theta = get_theta(robot_pos, object_pos)  # slope in degree
        a_diff = angle_range(heading, theta)
        if abs(a_diff) <= MAX_VIEW_ANGLE: # if the object within the viewing angle range
            xdist = angle2pix_distance(abs(a_diff))
            angle = math.radians(0.005993035 * xdist + 0.004074246)
            if a_diff < 0:
                return -angle
            else:
                return angle
    return None

def distance2eheight(robot_one_pos, heading, robot_two_pos):
    """Robot Distance Model
    Input : viewing robot position, angle of deviation from the real world
    heading, robot position. (Max value 1029 mm)

    returns : eheight (in pixels) of the lightguide that corresponds to the
    distance.
    """
    bc_lamda = -1.5
    dist = distance(robot_one_pos, robot_two_pos)
    angle = distance2angle(robot_one_pos, heading, robot_two_pos)
    if dist and angle:
        bc_dist = ((dist/10) ** bc_lamda - 1) / bc_lamda
        eheight = -4203.51031215 * bc_dist + 2800.13064751
        return round(eheight), angle
    else:
        return None, None

def distance2mass(robot_pos, heading, object_pos):
    """Ball Distance Model
    Input : viewing robot position, angle of deviation from the real world
    heading, position of ball. (Max value 892 mm)

    returns : mass (in pixels) of the ball.
    """
    bc_lamda = -1.686687
    dist = distance(robot_pos, object_pos)
    angle = distance2angle(robot_pos, heading, object_pos)
    if dist and angle:
        bc_dist = (dist ** bc_lamda - 1) / bc_lamda
        mass = (bc_dist - 5.92872e-01) / (-4.966366e-08)
        return round(mass), angle
    return None, None

def eheight2distance(eheight):
    """ Estimate distance to object by measuring eheight for robots."""
    bc_dist = (eheight - 2800.13064751) / (-4203.51031215)
    bc_lambda = -1.5
    dist = (bc_dist * bc_lambda + 1) ** (1 / bc_lambda)
    return dist * 10

def get_theta(robot_pos, object_pos):
    ang = math.degrees(math.atan2(object_pos[1] - robot_pos[1], 
                                  object_pos[0] - robot_pos[0]))
    return ang % 360

def mass2distance(mass):
    """ Estimate distance to object by measuring mass for balls."""
    bc_dist = 5.92872e-01 - 4.966366e-08 * mass
    bc_lambda = -1.686687
    dist = (bc_dist * bc_lambda + 1) ** (1 / bc_lambda)
    return dist

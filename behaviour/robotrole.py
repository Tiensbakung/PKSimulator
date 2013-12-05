#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

_path = os.path.split(os.getcwd())[0]
main_path = os.path.join(_path, 'iborg_main')
behaviour_path = os.path.join(_path, 'iborg_brain', 'behaviour')

sys.path.insert(1, behaviour_path)
sys.path.insert(2, main_path)
sys.path.insert(3, _path)

from iborg_robot_util import RobotInit, VisionInit

from senseact_base import SenseActProvider
from roleassigner import RoleAssigner
from worldmodel import WorldModel

class RobotRole:

    def __init__(self, ID, leader_id, role='collector', team='blue'):
        self.ID = ID
        self.rinit = RobotInit().get_restore_dict()
        self.rinit['init_id'] = ID
        self.vinit = VisionInit()
        self.role = role
        self.sap = SenseActProvider()
        self.state = ''
        self.wm = WorldModel(robot_init=self.rinit, vision_init=self.vinit)
        self.wm.leader_id = leader_id
        self.set_team(team)
        self.ra = RoleAssigner(senseact_provider=self.sap,
                               world_model=self.wm,
                               init_role=role)

    def _tweak(self):
        if self.team == 'red':
            self.wm.OwnBin1 = self.wm.BinRed1
            self.wm.OwnBin2 = self.wm.BinRed2
            self.wm.OpponentBin1 = self.wm.BinBlue1
            self.wm.own_bin_middle = self.wm.bin_middle_red
            self.wm.opponent_bin_middle = self.wm.bin_middle_blue
            self.wm.OwnHalfField = self.wm.half_field_red_1
            self.wm.OwnColor = 'red_robot'
            self.wm.GP = self.wm.bin_red
        elif self.team == 'blue':
            self.wm.OwnBin1 = self.wm.BinBlue1
            self.wm.OwnBin2 = self.wm.BinBlue2
            self.wm.OpponentBin1 = self.wm.BinRed1
            self.wm.own_bin_middle = self.wm.bin_middle_blue
            self.wm.opponent_bin_middle = self.wm.bin_middle_red
            self.wm.OwnHalfField = self.wm.half_field_blue_1
            self.wm.OwnColor = 'blue_robot'
            self.wm.GP = self.wm.bin_blue

    def assign_role(self, role):
        self.role = role
        self.ra.assign_role(role)

    def feed_workbench_data(self, robot_data, object_data):
        self.wm.robot_position = robot_data[self.ID]
        self.wm.workbench_robot_dict = robot_data
        self.wm.workbench_object_list = object_data

    def feed_vision_data(self, robot_data, object_data, object_in_grabber):
        self.wm.vision_robot_list = robot_data
        self.wm.vision_object_list = object_data
        self.wm.object_in_grabber = object_in_grabber

    def run(self, params={}):
        self.state, params = self.ra.active_role.run(params)
        return self.state, params

    def set_team(self, team):
        self.team = team
        self._tweak()

    def speed(self):
        return self.wm.speed

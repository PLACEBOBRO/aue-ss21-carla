#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob as glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time

actor_list = []

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False

world = client.get_world()
blueprint_library = world.get_blueprint_library()

vehicle_bp = random.choice(blueprint_library.filter('vehicle'))
transform = carla.Transform(carla.Location(x=-75, y=-110, z=0), carla.Rotation(yaw=-90))
vehicle = world.spawn_actor(vehicle_bp, transform)

vehicle.apply_control(carla.VehicleControl(throttle=0.5, steer=0.0))

while True:
    if vehicle.get_location().y <= -130 and vehicle.get_location().x < -70 :
        vehicle.apply_control(carla.VehicleControl(throttle=0.5, steer=0.55))
    if vehicle.get_location().x >= -70:
        vehicle.apply_control(carla.VehicleControl(throttle=0.5, steer=0.0))


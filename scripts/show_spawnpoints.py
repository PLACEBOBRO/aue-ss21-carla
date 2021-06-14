import glob
import os
import sys
import time
from pynput import keyboard

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
from carla import VehicleLightState as vls
import argparse
import logging
from numpy import random

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False

world = client.get_world()
blueprints = world.get_blueprint_library().filter('vehicle.*')

try:
    print("Drawing Spawnpoints on Map")
    map = world.get_map()
    waypoint_list = map.generate_waypoints(2.0)
    # Draw spawn points
    points = map.get_spawn_points()
    print(dir(points[0]))
    print(points[0].location)
    number = 0
    for waypoint in points:
        world.debug.draw_string(waypoint.location, str(number), draw_shadow=False,color=carla.Color(r=255, g=255, b=255), life_time=1000,persistent_lines=True)
        number += 1
finally:
    print('Done')


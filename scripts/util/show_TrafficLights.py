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

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False

world = client.get_world()
traffic_lights = world.get_actors().filter("traffic.traffic_light")

try:
    print("Drawing TrafficLights on Map")
    # Draw spawn points
    print(len(traffic_lights))
    print(dir(traffic_lights[0]))
    # print(world.get_actor(85).get_pole_index())
    for light in traffic_lights:
        world.debug.draw_string(light.get_location(), str(light.id), draw_shadow=False,color=carla.Color(r=255, g=0, b=0), life_time=100000,persistent_lines=True)

finally:
    print('Done')


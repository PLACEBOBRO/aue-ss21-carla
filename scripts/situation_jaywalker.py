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

vehicles_list = []
walkers_list = []
client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False
print("Press Function Keys for Spawning Vehicles!")
print("F1")

world = client.get_world()
blueprints = world.get_blueprint_library().filter('vehicle.*')


def onPress(key):
    try:

        # Spawns two cars more or less in the center
        if str(key) == 'Key.f1':
            # Spawn walker
            # Spawn_Point: Edited spawn_points[81] towards sidewalk
            spawn_point = carla.Transform(carla.Location(x=94.184067, y=-105.191704, z=8.305596), carla.Rotation(pitch=0.000000, yaw=-87.975883, roll=0.000000))
            ped_blueprints = world.get_blueprint_library().filter("walker.*")
            player = world.try_spawn_actor(random.choice(ped_blueprints),spawn_point)
            player_control = carla.WalkerControl()
            player_control.speed = 1
            pedestrian_heading=180
            player_rotation = carla.Rotation(0,pedestrian_heading,0)
            player_control.direction = player_rotation.get_forward_vector()
            player.apply_control(player_control)
            
    except Exception as e:
        print("Exception occured: " + str(e))


try:
    print("Starting init...")

    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(1.0)
    traffic_manager.set_random_device_seed(9)

    spawn_points = world.get_map().get_spawn_points()
    number_of_spawn_points = len(spawn_points)
    map = world.get_map()
    waypoint_list = map.generate_waypoints(2.0)
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    SetVehicleLightState = carla.command.SetVehicleLightState
    FutureActor = carla.command.FutureActor   
    keyboardListener = keyboard.Listener(on_press=onPress)
    keyboardListener.start()

    print("Startup finished")
    while True:
        world.wait_for_tick()
finally:
    print("ERROR EXCEPTED THE SCRIPT!")
    for actor in world.get_actors().filter("walker.*"):
        actor.destroy()
    print("Walker destroyed")


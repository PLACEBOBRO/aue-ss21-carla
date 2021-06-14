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
            # Set lane change false for every actor
            for actor in world.get_actors():
                traffic_manager.auto_lane_change(actor, False)

            car_bp = random.choice(blueprints.filter('vehicle.audi.etron'))
            car = world.try_spawn_actor(car_bp, spawn_points[99])
            print("Car spawned")

            # So car is not rolling away
            if car is not None:
                car.apply_control(carla.VehicleControl(brake=1.0))

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
    print('DESTROYING VEHICLES')
    for actor in world.get_actors().filter("vehicle.*"):
        actor.destroy()
    print('DONE DESTROYING VEHICLES')


import glob
import os
import sys
import time
from pynput import keyboard

# Gets the actor (see below) and turns the next traffic light yellow


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
print("Press F1 To change next Traffic Light to Yellow")
print("F1")

world = client.get_world()
blueprints = world.get_blueprint_library().filter('vehicle.*')


def onPress(key):
    try:
        # Changes next Traffic light to Yellow
        if str(key) == 'Key.f1':
            print("Hi")
            if my_actor == []:
                print("No actor present")
            else:
                actor = my_actor[0]
                while actor.is_at_traffic_light() == False:
                    time.sleep(0)
                if actor.is_at_traffic_light():
                    traffic_light = actor.get_traffic_light()
                print(traffic_light)
                if traffic_light.get_state() == carla.TrafficLightState.Green:
                    traffic_light.set_state(carla.TrafficLightState.Yellow)
                    print("Changed traffic light. Bye.")

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

    actors = world.get_actors()
    # Filter exact vehicle here
    my_actor = actors.filter('vehicle.*')
    print(my_actor)

    print("Startup finished")
    while True:
        world.wait_for_tick()
finally:
    print("ERROR EXCEPTED THE SCRIPT!")


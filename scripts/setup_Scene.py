import glob
import os
import sys
import time
from pynput import keyboard

# Way to spawn multiple Vehicles and Setup the World

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


def spawnVehicle(spawn_point,vehicle,rdn):
    batch = []
    print("SPAWNING A VEHICLE...")
    if rdn == True:
        # select random spawnpoint between 0 and 264
        spawn_point = random.randint(0,264)
    blueprint = random.choice(blueprints.filter(vehicle))
    if blueprint.has_attribute('driver_id'):
        driver_id = random.choice(blueprint.get_attribute('driver_id').recommended_values)
        blueprint.set_attribute('driver_id', driver_id)
    blueprint.set_attribute('role_name', 'autopilot')
    light_state = vls.NONE
    batch.append(SpawnActor(blueprint, spawn_points[spawn_point])
                 .then(SetAutopilot(FutureActor, True, traffic_manager.get_port()))
                 .then(SetVehicleLightState(FutureActor, light_state)))

    for response in client.apply_batch_sync(batch, synchronous_master):
        if response.error:
            print(response.error)
            logging.error(response.error)
        else:
            vehicles_list.append(response.actor_id)


def onPress(key):
    try:

        # Spawns two cars more or less in the center
        if str(key) == 'Key.f1':
            spawnVehicle(44,"vehicle.bh.crossbike",False)
            spawnVehicle(44,"vehicle.audi.etron",True)
            spawnVehicle(44,"vehicle.bmw.grandtourer",True)
            spawnVehicle(44,"vehicle.kawasaki.ninja",True)
            spawnVehicle(44,"vehicle.dodge_charger.police",True)
            spawnVehicle(44,"vehicle.audi.a2",True)
            spawnVehicle(44,"vehicle.citroen.c3",True)
            spawnVehicle(44,"vehicle.seat.leon",True)
            spawnVehicle(44,"vehicle.mini.cooperst",True)


    except Exception as e:
        print("Exception occured: " + str(e))


try:
    print("Starting init...")

    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(1.0)
    traffic_manager.set_random_device_seed(9)

    spawn_points = world.get_map().get_spawn_points()
    number_of_spawn_points = len(spawn_points)

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


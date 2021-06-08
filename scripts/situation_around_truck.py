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


def spawnCar(spawn_point):
    batch = []
    print("SPAWNING ONE CAR...")
    blueprint = random.choice(blueprints.filter("vehicle.bmw.grandtourer"))
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
            spawnCar(64)
            spawnCar(62)

            # Set lane change false for every actor
            for actor in world.get_actors():
                traffic_manager.auto_lane_change(actor, False)

            truck_bp = random.choice(blueprints.filter('vehicle.carlamotors.carlacola'))
            truck = world.try_spawn_actor(truck_bp, spawn_points[63])

            # So truck is not rolling away
            if truck is not None:
                truck.apply_control(carla.VehicleControl(brake=1.0))

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


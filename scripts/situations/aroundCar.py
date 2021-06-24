# Library function to start situation around Car

import carla
import time
from numpy import random

car_lst = None

def start(world,client,traffic_manager):
    global car_lst
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    if car_lst == None:
        print("lib:Starting Situation around Car")
        spawn_points = world.get_map().get_spawn_points()
        blueprints = world.get_blueprint_library().filter('vehicle.*')
        car_bp = random.choice(blueprints.filter('vehicle.audi.etron'))
        if car_bp.has_attribute('driver_id'):
            driver_id = random.choice(car_bp.get_attribute('driver_id').recommended_values)
            car_bp.set_attribute('driver_id', driver_id)
        car = SpawnActor(car_bp, spawn_points[114])
        car_lst = client.apply_batch_sync([car], False)
        car_act = world.get_actor(car_lst[0].actor_id)
    else:    
        batch = []
        print("Car starting to drive")
        batch.append(SetAutopilot(car_lst[0].actor_id, True, traffic_manager.get_port()))
        client.apply_batch_sync(batch)
        car_act = world.get_actor(car_lst[0].actor_id)
        car_lst=None
    return car_act


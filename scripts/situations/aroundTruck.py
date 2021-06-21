# Library function to start situation around Truck

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation around Truck")
    spawn_points = world.get_map().get_spawn_points()
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    
    truck_bp = random.choice(blueprints.filter('vehicle.carlamotors.carlacola'))
    truck = world.try_spawn_actor(truck_bp, spawn_points[63])
    if truck is not None:
        truck.apply_control(carla.VehicleControl(brake=1.0))
    return truck
    print("Spawned")


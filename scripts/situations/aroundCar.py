# Library function to start situation around Car

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation around Car")
    spawn_points = world.get_map().get_spawn_points()
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    car_bp = random.choice(blueprints.filter('vehicle.audi.etron'))
    car = world.try_spawn_actor(car_bp, spawn_points[99])
    if car is not None:
        car.apply_control(carla.VehicleControl(brake=1.0))
    return car
    print("Spawned")


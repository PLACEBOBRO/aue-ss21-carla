# Library function to start situation ???

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation ???")
    spawn_points = world.get_map().get_spawn_points()
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    #insert code here
    print("Spawned")
    # Remember to return spawned entities

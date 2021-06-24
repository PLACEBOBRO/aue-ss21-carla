# Library function to start situation Jaywalker

import carla
import time
from numpy import random
player = None
toSpawn = True


def start(world):
    print("lib:Starting Situation Jaywalker")
    global player
    global toSpawn
    # Spawn_Point: Edited spawn_points[89]
    if toSpawn:
        spawn_point = carla.Transform(carla.Location(x=189.0, y=52.0, z=0.275307), carla.Rotation(pitch=0.000000, yaw=179.852554, roll=0.000000))
        ped_blueprints = world.get_blueprint_library().filter("walker.*")
        player = world.try_spawn_actor(random.choice(ped_blueprints),spawn_point)
        print(player)
        print("Walker spawned")
        if player != None:
            toSpawn = False
    # Ped starts walking 
    else:
        player_control = carla.WalkerControl()
        player_control.speed = 1
        pedestrian_heading=90
        player_rotation = carla.Rotation(0,pedestrian_heading,0)
        player_control.direction = player_rotation.get_forward_vector()
        player.apply_control(player_control)
        toSpawn = True
    return player


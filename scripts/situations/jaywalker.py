# Library function to start situation Jaywalker

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation Jaywalker")
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
    print("Walker spawned")
    return player


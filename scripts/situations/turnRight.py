# Library function to start situation turnRight

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation turnRight")
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    #insert code here
    # Spawn_Point: Edited spawn_points[256] 
    spawn_point = carla.Transform(carla.Location(x=-95.793716, y=-8.109917, z=0.275307), carla.Rotation(pitch=0.000000, yaw=-179.705399, roll=0.000000))
    # Spawn_Point2: Edited spawn_points[28] 
    # spawn_point = carla.Transform(carla.Location(x=-94.5, y=118.906883, z=0.520476), carla.Rotation(pitch=0.000000, yaw=89.787704, roll=0.000000))
    ped_blueprints = world.get_blueprint_library().filter("walker.*")
    player = world.try_spawn_actor(random.choice(ped_blueprints),spawn_point)
    player_control = carla.WalkerControl()
    player_control.speed = 1
    pedestrian_heading=90
    player_rotation = carla.Rotation(0,pedestrian_heading,0)
    player_control.direction = player_rotation.get_forward_vector()
    player.apply_control(player_control)
    return player
    print("Spawned")

# Library function to start situation turnRight

import carla
import time
from numpy import random
fst = True

def start(world,lights):
    print("lib:Starting Situation turnRight")
    global fst
    points = []
    # Spawn_Point: Edited spawn_points[256] 
    points.append(carla.Transform(carla.Location(x=-94.593716, y=-8.109917, z=0.275307), carla.Rotation(pitch=0.000000, yaw=-179.705399, roll=0.000000)))
    # Spawn_Point2: Edited spawn_points[33]
    points.append(carla.Transform(carla.Location(x=-107.510582, y=143.0, z=0.275307), carla.Rotation(pitch=0.000000, yaw=-0.597992, roll=0.000000)))
    ped_blueprints = world.get_blueprint_library().filter("walker.*")
    for light in lights:
        light.freeze(True)
        light.set_state(carla.TrafficLightState.Green)
    if fst:
        pedestrian_heading=90
        spawn_point = points[0]
        print("Spawning first turn right")
        fst = False
    else:
        pedestrian_heading=0
        print("Spawning second turn right")
        spawn_point = points[1]
        fst = True
    player = world.try_spawn_actor(random.choice(ped_blueprints),spawn_point)
    time.sleep(10)        
    player_control = carla.WalkerControl()
    player_control.speed = 1
    player_rotation = carla.Rotation(0,pedestrian_heading,0)
    player_control.direction = player_rotation.get_forward_vector()
    player.apply_control(player_control)
    time.sleep(5)
    for light in lights:
        light.freeze(False)
    print("Spawned")
    return player

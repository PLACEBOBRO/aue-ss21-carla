# Library function to start situation passPedestrian

import carla
from numpy import random

def start(world):
    print("lib:Starting Situation passPedestrian")
    # turning off traffic lights
    lights = [68,69,77]
    for light in lights:
        world.get_actor(light).set_state(carla.TrafficLightState.Off)
    print("Traffic Light off")
    # spawn Walker
    # Spawn_Point: Edited spawn_points[129]
    spawn_point = carla.Transform(carla.Location(x=-8.798443, y=-185.813995, z=0.275307), carla.Rotation(pitch=0.000000, yaw=91.413536, roll=0.000000))
    ped_blueprints = world.get_blueprint_library().filter("walker.*")
    player = world.try_spawn_actor(random.choice(ped_blueprints),spawn_point)
    player_control = carla.WalkerControl()
    player_control.speed = 1
    pedestrian_heading=0
    player_rotation = carla.Rotation(0,pedestrian_heading,0)
    player_control.direction = player_rotation.get_forward_vector()
    player.apply_control(player_control)
    print("Walker spawned")
    return player
    
    



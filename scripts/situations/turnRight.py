# Library function to start situation turnRight

import carla
import time
from numpy import random
walker = []

def start(world,lights):
    print("lib:Starting Situation turnRight")
    global walker
    if walker == []:
        points = []
        # Spawn_Point: Edited spawn_points[256] 
        points.append(carla.Transform(carla.Location(x=-94.593716, y=-8.109917, z=0.275307), carla.Rotation(pitch=0.000000, yaw=-179.705399, roll=0.000000)))
        # Spawn_Point2: Edited spawn_points[33]
        points.append(carla.Transform(carla.Location(x=-107.510582, y=143.0, z=0.275307), carla.Rotation(pitch=0.000000, yaw=-0.597992, roll=0.000000)))
        ped_blueprints = world.get_blueprint_library().filter("walker.*")
        for light in lights:
            light.freeze(True)
            light.set_state(carla.TrafficLightState.Green)
        spawn_point1 = points[0]
        print("Spawning first turn right")
        print("Spawning second turn right")
        spawn_point2 = points[1]
        walker.append(world.try_spawn_actor(random.choice(ped_blueprints),spawn_point1))
        walker.append(world.try_spawn_actor(random.choice(ped_blueprints),spawn_point2))
    else:
        pedestrian1_heading=90
        pedestrian2_heading=0
        player1_control = carla.WalkerControl()
        player1_control.speed = 1
        player1_rotation = carla.Rotation(0,pedestrian1_heading,0)
        player1_control.direction = player1_rotation.get_forward_vector()
        player2_control = carla.WalkerControl()
        player2_control.speed = 1
        player2_rotation = carla.Rotation(0,pedestrian2_heading,0)
        player2_control.direction = player2_rotation.get_forward_vector()
        walker[0].apply_control(player1_control)
        walker[1].apply_control(player2_control)
        time.sleep(2)
        for light in lights:
            light.freeze(False)
        walker = []
    print("Spawned")
    return walker

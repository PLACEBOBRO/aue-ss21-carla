# Library function to start situation around Truck

import carla
import time
from numpy import random

truck_lst = None

def start(world,client,traffic_manager):
    global truck_lst
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    if truck_lst == None:
        print("lib:Starting Situation around Truck")
        spawn_points = world.get_map().get_spawn_points()
        blueprints = world.get_blueprint_library().filter('vehicle.*')
        truck_bp = random.choice(blueprints.filter('vehicle.carlamotors.carlacola'))
        if truck_bp.has_attribute('driver_id'):
            driver_id = random.choice(truck_bp.get_attribute('driver_id').recommended_values)
            truck_bp.set_attribute('driver_id', driver_id)
        truck = SpawnActor(truck_bp, spawn_points[63])
        truck_lst = client.apply_batch_sync([truck], False)
        truck_act = world.get_actor(truck_lst[0].actor_id)
        if truck_act is not None:
            truck_act.apply_control(carla.VehicleControl(brake=1.0))
    else:
        batch = []
        print("Truck starting to drive")
        batch.append(SetAutopilot(truck_lst[0].actor_id, True, traffic_manager.get_port()))
        client.apply_batch_sync(batch)
        truck_act = world.get_actor(truck_lst[0].actor_id)
        truck_lst = None

    return truck_act


# Library function to start situation passBiker

import carla
from carla import VehicleLightState as vls


from numpy import random

def start(world,client,traffic_manager):
    print("lib:Starting Situation passBiker")
    batch = []
    tm_port = traffic_manager.get_port()
    spawn_points = world.get_map().get_spawn_points()
    SetVehicleLightState = carla.command.SetVehicleLightState
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    FutureActor = carla.command.FutureActor
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    bike_bp = random.choice(blueprints.filter("vehicle.bh.crossbike"))
    if bike_bp.has_attribute('driver_id'):
        driver_id = random.choice(bike_bp.get_attribute('driver_id').recommended_values)
        bike_bp.set_attribute('driver_id', driver_id)
    bike_bp.set_attribute('role_name', 'autopilot')
    light_state = vls.NONE
    batch.append(SpawnActor(bike_bp, spawn_points[176])
                 .then(SetAutopilot(FutureActor, True, traffic_manager.get_port()))
                 .then(SetVehicleLightState(FutureActor, light_state)))
    bike = client.apply_batch_sync(batch, False)
    bike_act = world.get_actor(bike[0].actor_id)
    print("Spawned")
    return bike_act

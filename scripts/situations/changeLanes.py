# Library function to start situation changeLanes
# TODO: MAybe find a way to make vehicle slow down? Manual Control?

import carla
from carla import VehicleLightState as vls


from numpy import random

def start(world,client,traffic_manager):
    print("lib:Starting Situation changeLanes")
    batch = []
    tm_port = traffic_manager.get_port()
    spawn_points = world.get_map().get_spawn_points()
    SetVehicleLightState = carla.command.SetVehicleLightState
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    FutureActor = carla.command.FutureActor
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    car_bp = random.choice(blueprints.filter("vehicle.bmw.grandtourer"))
    if car_bp.has_attribute('driver_id'):
        driver_id = random.choice(car_bp.get_attribute('driver_id').recommended_values)
        car_bp.set_attribute('driver_id', driver_id)
    car_bp.set_attribute('role_name', 'autopilot')
    light_state = vls.NONE
    batch.append(SpawnActor(car_bp, spawn_points[170])
                 .then(SetAutopilot(FutureActor, True, traffic_manager.get_port()))
                 .then(SetVehicleLightState(FutureActor, light_state)))
    car = client.apply_batch_sync(batch, False)
    car_act = world.get_actor(car[0].actor_id)
    print("Spawned")
    return car_act

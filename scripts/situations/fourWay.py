# Library function to start situation 4Way Stop

import carla
from numpy import random
car_lst = None

def start(world,lights,client,traffic_manager):
    global car_lst
    SpawnActor = carla.command.SpawnActor
    SetAutopilot = carla.command.SetAutopilot
    print("lib:Starting Situation 4Way Stop")
    spawn_points = world.get_map().get_spawn_points()
    blueprints = world.get_blueprint_library().filter('vehicle.*')
    points = [48,129]
    if car_lst == None:
        group = lights.get_group_traffic_lights()
        for light in group:
            light.set_state(carla.TrafficLightState.Off)
            light.freeze(True)
        print("Traffic Light off")
        car1_bp = random.choice(blueprints.filter('vehicle.nissan.patrol'))
        car2_bp = random.choice(blueprints.filter('vehicle.tesla.model3'))
        if car1_bp.has_attribute('driver_id'):
            driver_id = random.choice(car_bp.get_attribute('driver_id').recommended_values)
            car_bp.set_attribute('driver_id', driver_id)
        if car2_bp.has_attribute('driver_id'):
            driver_id = random.choice(car_bp.get_attribute('driver_id').recommended_values)
            car_bp.set_attribute('driver_id', driver_id)
        car1 = SpawnActor(car1_bp, spawn_points[48])
        car2 = SpawnActor(car2_bp, spawn_points[129])
        car_lst = client.apply_batch_sync([car1,car2], False)
        car_act = [world.get_actor(car_lst[0].actor_id),world.get_actor(car_lst[1].actor_id)]
    else:
        batch = []
        print("Car starting to drive")
        batch.append(SetAutopilot(car_lst[0].actor_id, True, traffic_manager.get_port()))
        batch.append(SetAutopilot(car_lst[1].actor_id, True, traffic_manager.get_port()))
        client.apply_batch_sync(batch)
        car_act = []
        car_lst=None     
    print("Spawned")
    return car_act

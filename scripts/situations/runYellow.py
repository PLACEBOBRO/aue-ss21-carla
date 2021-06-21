# Library function to start situation runYellow

import carla

def start(world,light):
    print("lib:Starting Situation runYellow")
    # print(light)
    if light.get_state() == carla.TrafficLightState.Green:
        light.set_state(carla.TrafficLightState.Yellow)
        print("Traffic Light Changed")
    else:
        print("Light was red/yellow")
    # No return here

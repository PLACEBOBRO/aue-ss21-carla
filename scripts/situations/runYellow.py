# Library function to start situation runYellow

import carla

def start(world,light):
    print("lib:Starting Situation runYellow")
    # print(light)
    if light.is_frozen() == True:
        light.freeze(False)
        light.set_state(carla.TrafficLightState.Yellow)
        print("Traffic Light Changed")
    else:
        light.freeze(True)
        light.set_state(carla.TrafficLightState.Green)
        print("Light frozen")
    # No return here

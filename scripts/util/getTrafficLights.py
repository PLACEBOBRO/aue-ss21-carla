# Library function to get traffic lights
# Location Traffic Light Situation F9: Location(x=249.399994, y=46.070000, z=0.200000)
# Location Traffic Light Situation F10:
import carla
from numpy import random


def start(world):
    print("Getting Traffic Lights")
    F9 = None
    F10 = None
    traffic_lights = world.get_actors().filter("traffic.traffic_light")
    for light in traffic_lights:
        # print(light)
        # print(str(light.get_location()))
        if str(light.get_location()) == "Location(x=249.399994, y=46.070000, z=0.200000)":
            F9 = light
        if str(light.get_location()) == "Location(x=95.532082, y=-214.192078, z=0.014180)":
            F10 = light
    print(F9)
    print(F10)
    print("Finished Traffic Lights")
    return [F9,F10]

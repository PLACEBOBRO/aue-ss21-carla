# Library function to get traffic lights
# Location Traffic Light Situation (F9): Location(x=249.399994, y=46.070000, z=0.200000) (Backup Location)
# Location Traffic Light Situation F9: Location(x=-18.010000, y=123.139999, z=0.200000)
# Location Traffic Light Situation F10: Location(x=20.463360, y=-187.895172, z=0.148411)
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
        if str(light.get_location()) == "Location(x=-18.010000, y=123.139999, z=0.200000)":
            F9 = light
        if str(light.get_location()) == "Location(x=20.463360, y=-187.895172, z=0.148411)":
            F10 = light
    print(F9)
    print(F10)
    print("Finished Traffic Lights")
    return [F9,F10]

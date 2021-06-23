# Library function to get traffic lights
# Location Traffic Light Situation F4.1: Location(x=-94.057716, y=28.359629, z=0.109092)
# Location Traffic Light Situation F4.2: Location(x=-66.787178, y=142.753357, z=0.147905)
# Location Traffic Light Situation (F9): Location(x=249.399994, y=46.070000, z=0.200000) (Backup Location)
# Location Traffic Light Situation F9: Location(x=-18.010000, y=123.139999, z=0.200000)
# Location Traffic Light Situation F10: Location(x=20.463360, y=-187.895172, z=0.148411)
import carla
from numpy import random


def start(world):
    print("Getting Traffic Lights")
    F9 = None
    F10 = None
    F41 = None
    F42 = None
    traffic_lights = world.get_actors().filter("traffic.traffic_light")
    for light in traffic_lights:
        # print(light)
        # print(str(light.get_location()))
        if str(light.get_location()) == "Location(x=-18.010000, y=123.139999, z=0.200000)":
            F9 = light
        if str(light.get_location()) == "Location(x=20.463360, y=-187.895172, z=0.148411)":
            F10 = light
        if str(light.get_location()) == "Location(x=-94.057716, y=28.359629, z=0.109092)":
            F41 = light
        if str(light.get_location()) == "Location(x=-66.787178, y=142.753357, z=0.147905)":
            F42 = light
    lights = [F9,F10,F41,F42]
    print(lights)
    print("Finished Traffic Lights")
    return lights

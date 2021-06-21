# Master Script to connect to Carla and spawn Situations
# TODO: Maybe add Shift+F?? to kill situational entities?
# TODO: Find a place with only crosswalk for Situation "Pass pedestrian"
# TODO: Situation Blinking Red & 4Way Stop the same?

import glob
import os
import sys
import time
from pynput import keyboard

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False
world = client.get_world()

# import situations

from situations import jaywalker
from situations import aroundCar
from situations import aroundTruck
from situations import turnRight
from situations import passBiker
from situations import changeLanes
from situations import blinkingRed
from situations import runYellow


entities = []
print("Press Key for Spawning Situations")
print("F1: 4 Way Stop")
print("F2: Jaywalker")
print("F3: around Truck")
print("F4: turnRight")
print("F5: around Car")
print("F6: passBiker")
print("F7: blinking Red")
print("F8: changeLanes")
print("F9: runYellow")
print("F10: pass Pedestrian")
print("F12: kill spawned entities")

def onPress(key):
    global entities
    try:
        if str(key) == 'Key.f1':
            print("Starting Situation: 4Way Stop")
            # TODO: Edit and import Situation
        if str(key) == 'Key.f2':
            entities.append(jaywalker.start(world))
        if str(key) == 'Key.f3':
            entities.append(aroundTruck.start(world))
        if str(key) == 'Key.f4':
            entities.append(turnRight.start(world))
        if str(key) == 'Key.f5':
            entities.append(aroundCar.start(world))
        if str(key) == 'Key.f6':
            entities.append(passBiker.start(world,client,traffic_manager))
        if str(key) == 'Key.f7':
            entities.append(blinkingRed.start(world,client,traffic_manager))
        if str(key) == 'Key.f8':
            entities.append(changeLanes.start(world,client,traffic_manager))
        if str(key) == 'Key.f9':
            runYellow.start(world)
        if str(key) == 'Key.f10':
            print("Starting Situation: pass Pedestrian")
            # TODO: Edit and import Situation, find a place with ONLY crosswalk
        if str(key) == 'Key.f12':
            print("Killing last spawned entities")
            for actor in entities:
                actor.destroy()
            entities = []
    except Exception as e:
        print("Exception occured: " + str(e))

try:
    print("Initializing")
    # init traffic manager
    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(1.0)
    #needed?
    traffic_manager.set_global_distance_to_leading_vehicle(1.0)
    traffic_manager.set_random_device_seed(9)
    # -
    keyboardListener = keyboard.Listener(on_press=onPress)
    keyboardListener.start()

    print("Done")
    while True:
        world.wait_for_tick()
finally:
    print("ERROR EXCEPTED THE SCRIPT!")
    print('DESTROYING SPAWNED ACTORS')
    #TODO: add walkers to be removed
    for actor in world.get_actors().filter("vehicle.*"):
        actor.destroy()
    for walker in world.get_actors().filter("walker.*"):
        walker.destroy()
    print('DONE DESTROYING ACTORS')












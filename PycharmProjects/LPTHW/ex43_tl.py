from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured, SubClass it and implement enter(). "
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = ["Such a luser. "]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        action = raw_input("> ")
        if action == "shoot!":
            return 'death'
        elif action == "dodge!":
            return 'death'
        elif action == "tell a joke":
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'            

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print code
        guess = raw_input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            return 'the_bridge'
        else:
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "In the Bridge."
        action = raw_input("> ")
        if action == "throw the bomb":
            return 'death'

        elif action == "slowly place the bomb":
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "EscapePod"
        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            return 'death'
        else:
            print "You won!"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        # pass
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        # pass
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        # pass
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# for i in dir(a_game):
#     print i
# for i in dir(a_map):
#     print i

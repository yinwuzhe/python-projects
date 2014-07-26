from sys import exit
from random import randint

class Scene(object):

    def enter(self):
	exit(1)

class TheCorridor(Scene):


    def enter(self):
	print """
		This is the Corrider,all you can see is a vast of white,
		the white wall, the white floor, there is , no windows,
		all there have is endless,
		Ah, there is a closed door, mybe  a way...
		Ah, there is a elevator,another choice!
		Or you can choose to hang on here to the death!
	"""
	action=raw_input(">");
	
	if action=="open the door":
	    print """
			******You opened the door which is not locked,
			and You enter into it!!! to find...
	    """	
	    return 'GasRoom'

	elif action=="enter the elevator":
	    print """
			I(elevator) am always waiting for guests like you,
			 in the corridor,AHAHHAHAHHA!!!
			You smells delicious!
		 """
	    return 'Elevator'
	else:
	    print "DOSE NOT COMPUTE"
	    return 'TheCorridor'

class GasRoom(Scene):
   
    def enter(self):
	print """
		OH, baby ,you come!
			ERRRRzzzzzzzzzzz
		Nice, the door is closed!
		Never been out,the poison gas will make 
		You forgot your mom in few minutes...
		AHAHAHAAAAAAAAAAAAOOOOOO

		beside the door there is a pad to open the door 
		maybe you can try...
	   """
	code= "%d%d" %(randint(0,9),randint(0,9))
	guess = raw_input("[keypad]> ");
	guesses=1
	while guess!=code and guesses<5:
	    print "BZZZZZZPPPPPPPPPPPPPP"
	    guesses+=1
	    guess= raw_input("[keypad]> ")

	if guess==code:
	    print """
		Oh,lucky boy!
		You opened the door and 
		saved your self
		"""
	    return 'TheCorrider'
	else:
	    print"""
		Sadly, the lock buzzes one last time,
		You have spent your time.
		Your mom will miss you always...
		AHHHHHHH Sadly story.....
		"""
	    return 'Death'

class Elevator(Scene):

    def enter(self):
	print """
		hello, this is the elevator!!!!
		We have beautiful music here,
		Don't cry, Oh, you think too much,
		anyway, you should try to select which floor to go...
	"""
	floor = raw_input("[floor #]> ")
	if int(floor) == 3:
	    print "there is a door to the laserRoom"
	    return 'LaserRoom'
	elif int(floor)==5:
	    print "this is the Roof "
	    return "TheRoof"
	else:
	    print "there is no room out,just the wall, you fool!"
	    return 'Elevator'


class Death(Scene):
	quips = [
	"You died. You are such a loser.",
	"Your mother will never see you again...but miss you always..",
	"You kinda of suck at this.",
	"I have a small puppy that's better at this."
	]
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class TheRoof(Scene):

    def enter(self):
	print "you are now in the roof, the goust is chasing you"
	action = raw_input("> ")
	if action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'finished'
        else:
            print "the ghosts catched your lag!"
            return 'Death'

class LaserRoom(Scene):
	
    def enter(self):
	print """
		You do a dive roll into the Weapon Armory, crouch and scan the room,
		for more Ghosts that might be hiding.  It's dead quiet, too quiet.
		You stand up and run to the far side of the room and find the,
		neutron bomb in its container.  There's a keypad lock on the box,
		and you need the code to get the bomb out.  If you get the code,
		wrong 10 times then the lock closes forever and you can't,
		get the bomb.  The code is 3 digits.
		"""
	code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "let's share the secret ", code
        guesses = 1
        guess = raw_input("[keypad]> ")
        while guess != code and guesses < 10:
            guesses += 1
            print "BZZZZEDDD!"
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'Elevator'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'Death'



class BloodRoom(Scene):
	pass

class Map(object):

    scenes = {
	"TheCorridor":TheCorridor(),
	'GasRoom':GasRoom(),
	'Elevator':Elevator(),
	'TheRoof':TheRoof(),
	'LaserRoom':LaserRoom(),
	'BloodRoom':BloodRoom(),
	'Death':Death()
   }

    def __init__(self, start_scene):
	self.start_scene=start_scene

    def next_scene(self,scene_name):
	return Map.scenes.get(scene_name)

    def opening_scene(self):
	return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self,smap):
	self.smap=smap
    
    def play(self):
	current_scene= self.smap.opening_scene()
	
	while True:
	    next_scene =current_scene.enter()
	    current_scene=self.smap.next_scene(next_scene)
  

mymap=Map('TheCorridor')
game=Engine(mymap)
game.play()

class Room(object):
    def __init__(self, name, description):
	self.name = name
	self.description = description
	self.paths = {}

    def go(self, direction):
	return self.paths.get(direction, None)

    def add_paths(self, paths):
	self.paths.update(paths)

TheCorridor = Room("TheCorridor",
"""
		This is the Corrider,all you can see is a vast of white,
		the white wall, the white floor, there is , no windows,
		all there have is endless,
		Ah, there is a closed door, mybe  a way...
		Ah, there is a elevator,another choice!
		Or you can choose to hang on here to the death!
	""")

GasRoom = Room('GasRoom',
"""
		OH, baby ,you come!
			ERRRRzzzzzzzzzzz
		Nice, the door is closed!
		Never been out,the poison gas will make 
		You forgot your mom in few minutes...
		AHAHAHAAAAAAAAAAAAOOOOOO

		beside the door there is a pad to open the door 
		maybe you can try...
	   """)

Elevator = Room('Elevator',
"""
		hello, this is the elevator!!!!
		We have beautiful music here,
		Don't cry, Oh, you think too much,
		anyway, you should try to select which floor to go...
	""")

Death = Room('Death',
"I have a small puppy that's better at this.")

TheRoof = Room('TheRoof',
"you are now in the roof, the goust is chasing you")

LaserRoom = Room('LaserRoom',
"""
		You do a dive roll into the Weapon Armory, crouch and scan the room,
		for more Ghosts that might be hiding.  It's dead quiet, too quiet.
		You stand up and run to the far side of the room and find the,
		neutron bomb in its container.  There's a keypad lock on the box,
		and you need the code to get the bomb out.  If you get the code,
		wrong 10 times then the lock closes forever and you can't,
		get the bomb.  The code is 3 digits.
		""")
finished =Room('Success',"You are the winner, congradulations!")

LaserRoom.add_paths({
	"123":Elevator,
	'*':Death
})
TheRoof.add_paths({
	"slowly place the bomb":finished,
	"*":Death
})
Elevator.add_paths({
	"3":LaserRoom,
	'5':TheRoof,
	'*':Elevator
})
GasRoom.add_paths({
	'0123':TheCorridor,
	'*':Death
})
TheCorridor.add_paths({
	'open the door':GasRoom,
	'enter the elevator':Elevator,
	'*':TheCorridor
})
START = TheCorridor




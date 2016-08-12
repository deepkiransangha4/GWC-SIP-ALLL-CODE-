start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)
done = False

while not done:
	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()
	if user_input == "left":
		print("You decide to go left and you run into a troll! Fight or run?") 
		done = True
		user_input = input()
		if user_input == "fight":
			print ("The troll hits you on the head and you turn into a dragon. Fly or attack?")
			done = True
			user_input = input()
			if user_input == "fly":
				print ("You suck at flying and fly into a castle.")
				done = True
			elif user_input == "attack":
				print ("You accidentally breathe fire onto an unprotected set of a gajillion fireworks and hurt yourself.")
				done = True
			done = True
		elif user_input == "run":
			while user_input != "invisible" or "throw rocks":
				print ("The troll starts chasing you. Do you go invisible or throw rocks at it as you're running?")
				user_input = input()
				if user_input == "invisible":
					print ("You run into Harry Potter. He's mad that you're invisible because that's his thing. Potter points his wand at you and says 'Avada Kedavra.' Sorry.")
				elif user_input == "throw rocks":
					print ("You accidentally throw a rock at a sleeping dragon. The dragon chases you. Sorry.")
					done = True
			done = True
	elif user_input == "right":
			print("You choose to go right and you walk up to a river. Swim across?")
			done = True
			user_input = input()
			if user_input == "yes":
				while user_input != "hippogriff" or "Hedwig":
					print ("The current is too strong. Do you summon a hippogriff to help you or Hedwig to get you your magic broom?")
					done = True
					user_input = input()
					if user_input == "hippogriff":
						print("You're not Harry Potter, so the hippogriff hates you. It swings you off of its back.. oops.")
						done = True
					elif user_input == "Hedwig":
						print ("Hedwig recognizes you from that one time you ate the piece of worm that she wanted. First of all, how could you? Second of all, what the heck dude who eats worms??? Hedwig is pissed, and brings you a huge gummy worm rather than a broom.")
						done = True
			elif user_input == "no":
					print ("You sit down next to the river. Do you take a nap? Yeah or nooo?")
					user_input == input()
					if user_input == "yeah":
						print ("Homie, that was nooooot a good idea. A troll comes by to take his revenge (we won't tell you what he does.. let's leave that a surprise) because he just doesn't like you.")
						done = True
					elif user_input == "nooo":
						print ("Good job! You're viligant. OH WHOA LOOK THERE! A DRAGON! ... Hello?")
						done = True
		

	

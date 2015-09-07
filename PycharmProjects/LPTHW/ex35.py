#!/usr/bin/env python

import string
import keyword
import sys

#Get all keyword for python
#keyword.kwlist
#['and', 'as', 'assert', 'break', ...]
keyWords = keyword.kwlist

#Get all character for identifier
#string.letters ==> 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#string.digits  ==> '0123456789'
charForId = string.letters + "_"
numForId = string.digits

idInput = raw_input("Input your words,please!")

if idInput in keyWords:
    print "%s is keyword fot Python!" % idInput
else:
    lenNum = len(idInput)
    if(1 == lenNum):
        if(idInput in charForId and idInput != "_"):
            print "%s is legal identifier for Python!" % idInput
        else:
            #It's just "_"
            print "%s isn't legal identifier for Python!" % idInput

    else:
        if(idInput[0:1] in charForId):
            legalstring = charForId + numForId
            for item in idInput[1:]:
                if (item not in legalstring):
                    print "%s isn't legal identifier for Python!" % idInput
                    sys.exit(1)
            print "%s is legal identifier for Python!2" % idInput
        else:
            print "%s isn't legal identifier for Python!3" % idInput





##################################################
# from sys import exit

# def gold_room():
# 	print "This room is full of gold. How much do you take?"

# 	next = raw_input("> ")
# 	if "0" in next or "1" in next:
# 		how_much = int(next)
# 	else:
# 		dead("Man, learn to type a number.")

# 	if how_much < 50:
# 		print "Nice, you're not greedy, we win!"
# 		exit(0)
# 	else:
# 		dead("You greedy bastard!")

# def bear_room():
# 	print "This is a bear here."
# 	print "The bear has a bunch of honey."
# 	print "The fat bear is in front of anohter door."
# 	print "How are you going to move the bear?"
# 	bear_moved = False

# 	while True:
# 		next = raw_input("> ")

# 		if next == "take honey":
# 			dead("The bear looks at you then slaps your face off.")
# 		elif next == "taunt bear" and not bear_moved:
# 			print "The bear has moved from the door. You can go through it now."
# 			bear_moved = True
# 		elif next == "taunt bear" and bear_moved:
# 			dead("The bear gets pissed off and chews your leg off.")
# 		elif next == "open door" and bear_moved:
# 			gold_room()
# 		else:
# 			print "I got no idea what that means."

# def cthulhu_room():
# 	print "Here you see the great evil Cthulhu."
# 	print "He, it, whatever stares at you and you go insane."
# 	print "Do you flee for your life or eat your head?"

# 	next = raw_input("> ")

# 	if "flee" in next:
# 		start()
# 	elif "head" in next:
# 		dead("Well that was tasty!")
# 	else:
# 		cthulhu_room()

# def dead(why):
# 	print why, "Good job!"
# 	exit(0)

# def start():
# 	print "You are in a dark room."
# 	print "There is a door to your right and left."
# 	print "Which one do you take?"

# 	next = raw_input("> ")

# 	if next == "left":
# 		bear_room()
# 	if next == "right":
# 		cthulhu_room()
# 	else:
# 		dead("You stumble around the room until you starve.")

# start()
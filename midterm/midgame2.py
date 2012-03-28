import random
kills = 0
totalkills = 0
flask = 0
maxhealth = 100
health = 100
rem = 0
attack_min = 0
attack_max = 0
red_moss = 0
totalred = 0
green_moss = 0
totalgreen = 0
bosshealth = 200
bossdamage = 1
def med():
	if flask == "1":
		maxhealth - health == rem
		rem + health == health
def stat():
	print "****************"
	print "|totalkills:%s " %totalkills
	print "|health:%s     " %health
	print "|attack_min:%s " %attack_min
	print "|attack_max:%s " %attack_max
	print "|totalred:%s   " %totalred
	print "|totalgreen:%s " %totalgreen
	print "****************"
	
def cell_start():
	global attack_min
	global attack_max
	print " You have awaken in a small cell"
	print " You see the keys to you cell are on the floor"
	print " You use a piece of a broken bench and get the keys"
	print " You open the door"
	print " What do you do"
	print "1) Leave"
	print "2) Explore"
	print "3) Stay"
	
	next4 = raw_input(">")
	if next4 == "1":
		start()
	if next4 == "2":
		print "You taken one last look around and decide to take the piece of the broken bench with you"
		attack_min = attack_min + 1 
		attack_max = attack_max + 3 
		start()
	if next4 =="3":
		print "You decide to sleep one more night, you never wake up"
		exit()
def start():		
	print "You arrive in a long and narrow hallway. With a dim light coming from the center. You can see six doors."
	print "What do you do?"
	print "1)Go through the 1st door on the left"
	print "2)Go through the 1st door on the right"
	print "3)Go through the big door in the center"
	print "4)Go through the 2nd door on the left"
	print "5)Go throught the 2nd door on the right"
	print "6)Go back to your cell"
	
	next = raw_input("> ")
	if next == "1":
		rat_room()
	elif next == "2":
		cat_room()
	elif next == "3":
		boss_room()
	elif next == "4":
		dealer_room()
	elif next == "5":
		moss_room()
	elif next == "6":
		cell()
	elif next == "stats":
		stat()
		start()
	else:
		print "You stumble around the room until you starve."
	
def rat_room():
	global health
	global kills
	global totalkills
	global attack_min
	global attack_max
	print "You open the door only to find that it is a room full of rats"
	print "What do you do?"
	print "1)Explore the rat room."
	print "2)Kill all the rats"
	print "3)Leave"
	
	next2 = raw_input(">")
	if next2 == "1":
		print "You look around and find nothing of interest, just rats."
		rat_room()
	if next2 == "2":
		print "You start your hunt and kill every rat you see."
		kills = random.randint(0+ attack_min,20+attack_max)
		health = health - round(kills*.5) 
		totalkills = kills + totalkills
		print "You killed %s rats." %kills
		print "You still have %s health" %health
		start()
	if next2 == "3":
		print "you left"	
		start()

def cat_room():
	global attack_min
	global attack_max
	print """You enter a room you see a man laying down against the wall holding a cat in a cage."""
	print "1) Talk to the man"
	print "2) Kill the man"
	print "3) Explore the room"
	next3 = raw_input(">")
	if next3 == "1":
		print """You are the first person I have seen in a very long time. You look so healthy so...you might have a chance. Yes, yes there is still hope for me...us to get out of this god forsaken place. Its is simple really all you have to do is bring me rats. Yes rats. This place is full of them. Bring me a good amount and I will feed them to my cat. But be warned the more you hunt these rats the more dangerous they become."""
		start()	
	if next3 == "2":
		print "You approach the man and twist his neck. He dies instantly. As the cage falls it opens and unleashes a furry little menace that is out for you blood but it runs away into the darkness.You pick up an amulet and put it on"
		attack_min = attack_min + 5 
		attack_max = attack_max + 8
		start()
	if next3 == "3":
		print " A room the size of a closet a man seems to have taken refeuge in here but from what"
		cat_room()

def dealer_room():
	print "You enter a room with a table and two chairs a young women comes from the shadow."
	print "1) Sit down and talk to the women"
	print "2) Kill the women"
	print "3) Explore the room"
	next5 = raw_input(">")
	if next5 == "1":
		print """I been waiting for some one to come. No body ever vist me anymore.I know why you are here, an enchantment from a ghost will prove very usefull in your endervor. All that i ask is that you bring me some moss.Now go."""
		start()
	if next5 == "2":
		print "You fool I am already dead, now feel the wrath of the undead."
		print "You feel your life being suck away from your body slowly dying painfully"
		exit()
	if next5 == "3":
		print "You look around the room and you see a golden flask, as you go and pick it up the women says"
		print " Only a few can handle something like that come back later many some moss can change my mind"
		dealer_room()
def moss_room():
	global red_moss
	global totalred
	global green_moss
	global totalgreen
	print "You enter a room that is all wet and slimy"
	print"1) Look for moss."
	print"2) Explore the room"
	print"3) Leave"

	next6 = raw_input(">")
	if next6 == "1":
		green_moss = random.randint(1,3)
		red_moss = random.randint(1,5)
		print "You found %s green moss" %green_moss
		print "You found %s red moss" %red_moss
		totalgreen = green_moss+totalgreen
		totalred = red_moss+totalred
		start()
	if next6 == "2":
		print " In a room full if slime you found nothing worth wild.Just some moss."
	if next6 == "3":
		print "you left"
		start()

def boss_room():
	global maxhealth
	global health
	global attack_min
	global attack_max
	global bosshealth 
	global bossdamage 
	print "You open the door and walk inside to see a room that is warm and cozy. Not dark like the other but well lit with torches and candles"
	print "You also see the one that has kept you here an old slim man"
	print "So you think you can escape my castle good luck"
	print "What do you do?"
	print "1) Kill the boss."
	nextfinal = raw_input(">")
	if nextfinal == "1":
		while bosshealth <= 0:
			bossdamage = bossdamage + random.randInt(0,5)
			health = bossdamage - health
			bosshealth = bosshealth - random.randint(0+ attack_min,20+attack_max)
			if health <= 0:
				print "Now you are here forever"
				exit()
	print "it cant be"
		
cell_start()
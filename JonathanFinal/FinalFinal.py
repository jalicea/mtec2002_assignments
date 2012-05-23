bif="dungeonresized.jpg"
fbif = "rage.jpg"
sbif ="cross.jpg"
tbif ="hallway.jpg"
ffbif="face.jpg"
mif="mouse.png"
cs ="sound.mp3"
ls = [bif,fbif,sbif,tbif,ffbif]
import pygame
from pygame.locals import *

pygame.init()
sound = pygame.mixer.Sound(cs)
sound.play()

screen_size = (640, 400)
screen = pygame.display.set_mode(screen_size)
background=pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

pygame.display.set_caption("THE FINAL")

clock = pygame.time.Clock()

running = True

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
index =0

while running == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
			print "left click"
			try:
		 		index = index +1
		 	except: index = 0
		elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
			print "centerclick"
			sound.play()
		elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
			print "rightclick"
			try: 
				index = index -1
			except: index = 3
	
	try:
		background=pygame.image.load(ls[index]).convert()
	except: 
		index = 0
	screen.blit(background, (0,0))
	x,y = pygame.mouse.get_pos()
	x -= mouse_c.get_width()/2
	y -= mouse_c.get_height()/2
	screen.blit(mouse_c, (x,y))
	pygame.display.update()
	clock.tick(60)
	pygame.display.flip()
	
pygame.quit()
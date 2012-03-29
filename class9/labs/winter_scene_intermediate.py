"""
winter_scene.py
===
Using the drawing and animation techniques we learned create an animation of snow falling.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Incorporate the code from multiple_objects.py to create the snow:
	a. However, in the setup, rather than use 0 for the initial y value, use a random value
	b. In the main loop, when iterating over the circles, check if the y value is greater than the window width (see screen_wrap.py)
	c. If the y value is greater... then bring the circle back up to the top
3. (INTERMEDIATE) Incorporate random lateral motion.  Try adding a unique velocity for x and y for each circle by expanding your two element list!  You can also use a dictionary if it makes more sense than a list with indexes.

"""
import pygame

FRAME_RATE = 100
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "My Game"

background_color = (001, 001, 001)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

while running == True:

	# stop the main loop when window is closed 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill(background_color)

	# draw everything here!  this line draws a circle in the middle of the screen
	
	pygame.draw.circle(screen, (200, 200, 200), (WINDOW_WIDTH / 5, WINDOW_HEIGHT / 1), 100)
	pygame.draw.circle(screen, (200, 1, 200), (WINDOW_WIDTH / 2.25, WINDOW_HEIGHT / 2.25), 25)
	pygame.draw.circle(screen, (200, 1, 200), (WINDOW_WIDTH / 1.75, WINDOW_HEIGHT / 2.25), 25)
 
	clock.tick(FRAME_RATE)
	pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
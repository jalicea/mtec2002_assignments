"""
simple_animation.py
===
In this exercise, we'll animate a circle so that it moves from the top of the screen to the bottom of the screen...

1. We'll store the circle's coordinates and velocity in the variables x, y and velocity.  
2. Since our game loops continuously, if we redraw the circle at a different position after each iteration of the loop, it will look like it's moving.  
3. To do this, we'll draw the circle using the values of x and y as the coordinates.  
4. At each iteration, we'll also increment that position with the value that we have in the velocity variable.

To write this code:
1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Create three variables above the for loop.  Name them x, y and velocity_y.  Set them to the following values: 
	x: window_dimensions[0] / 2
	y: 0
	velocity_y: 1
3. Draw a circle using the x and y values above
	a. The code for the circle should go after the line that fills the background color in the while loop.  
	b. Use the x and y values to set the coordinates of the circle.
	c. Use the docs if you need help with calling the function: http://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
4. Increment your y value by adding velocity_y.
"""

import pygame

FRAME_RATE = 100
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "My Game"
x = WINDOW_WIDTH/2
y = 0
velocity_y = 1

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
	
	pygame.draw.circle(screen, (200, 200, 200), (x,y), 10)
	y =+ velocity_y 
	clock.tick(FRAME_RATE)
	pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
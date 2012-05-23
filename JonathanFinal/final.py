import pygame

FRAME_RATE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "My Game"

background_color = (255, 255, 255)
running = True
pygame.init()
pygame.image.load
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
	pygame.draw.circle(screen, (0, 0, 200), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 10)
 
	clock.tick(FRAME_RATE)
	pygame.display.flip()

# exit when we're done with the loop
pygame.quit()

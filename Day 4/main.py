from setup import *
from jumper import Jumper

is_running = True

dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(dimensions)

# Set the window title to Jumper
pygame.display.set_caption("Jumper")

# This is what will handle game logic and drawing
game = Jumper()

previous_time = pygame.time.get_ticks()

# Main game loop
while is_running:
	# Find the change in time (delta_time) since the previous frame
	current_time = pygame.time.get_ticks()
	delta_time = current_time - previous_time
	previous_time = current_time

	# Draw white background
	screen.fill((255, 255, 255))

	# Update game logic and draw
	game.update(delta_time)
	game.draw(screen)  

	# Loop over all pending events and clear them
	for event in pygame.event.get():
		# If there is a quit event, the user wants to exit
		# This will make the close (red X) button work
		if event.type == pygame.QUIT:
			is_running = False

	# Update the display with the latest frame...
	# This is used so that everything is displayed to the user in one step, after all instructions 
	# are completed. Pygame does not immediately display drawn objects, as otherwise the user would
	# see them flicker out (as the screen is filled) and in (as the object is drawn). This update
	# will replace the previous frame.
	pygame.display.update()

pygame.quit()
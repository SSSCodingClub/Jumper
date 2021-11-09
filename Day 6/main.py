from setup import *
from colors import COLOR_WHITE
from jumper import Jumper
from splash import Splash

is_running = True

dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(dimensions)

# Set the window title to Jumper
pygame.display.set_caption("Jumper")

current_scene = Splash()

previous_time = pygame.time.get_ticks()

# Main game loop
while is_running:
	# Find the change in time (delta_time) since the previous frame
	current_time = pygame.time.get_ticks()
	delta_time = current_time - previous_time
	previous_time = current_time

	# Draw white background
	screen.fill(COLOR_WHITE)

	# Update logic and draw
	# Store the status of the current scene (return value of update)
	status = current_scene.update(delta_time)
	current_scene.draw(screen)  

	# If current scene requests to exit, end the game loop
	if status == COMMAND_EXIT:
		is_running = False
	# If the current scene requests to start (or restart) the game, set the current scene to a new
	# instance of Jumper
	elif status == COMMAND_START:
		current_scene = Jumper()

	# Update the display with the latest frame...
	# This is used so that everything is displayed to the user in one step, after all instructions 
	# are completed. Pygame does not immediately display drawn objects, as otherwise the user would
	# see them flicker out (as the screen is filled) and in (as the object is drawn). This update
	# will replace the previous frame.
	pygame.display.update()

pygame.quit()
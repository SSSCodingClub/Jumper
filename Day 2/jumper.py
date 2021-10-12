from setup import *
from player import Player
from platform import Platform

# Class which handles the main game logic and drawing
class Jumper:

	# Called on game initialization
	def __init__(self):
		# Create a player at the top left corner
		self.player = Player(0, 0) 

		# Create a list of platforms
		# For now, this list contains just one platform in the center of the screen
		self.platforms = [Platform(SCREEN_WIDTH/2 - Platform.width/2, 
								   SCREEN_HEIGHT/2 - Platform.height/2)]

	# Updates the game logic every frame
	def update(self, delta_time):
		self.player.resolve_platform_collisions(delta_time, self.platforms)
		self.player.update(delta_time)

	# Draws all game objects every frame
	def draw(self, screen):
		for platform in self.platforms:
			platform.draw(screen)
		self.player.draw(screen)

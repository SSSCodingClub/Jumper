from setup import *
from player import Player

# Class which handles the main game logic and drawing
class Jumper:

	# Called on game initialization
	def __init__(self):
		# Create a player at the top left corner
		self.player = Player(0, 0) 

	# Updates the game logic every frame
	def update(self):
		self.player.update()

	# Draws all game objects every frame
	def draw(self, screen):
		self.player.draw(screen)

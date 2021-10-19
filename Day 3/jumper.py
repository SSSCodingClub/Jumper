from setup import *
from player import Player
from platform import Platform

# Class which handles the main game logic and drawing
class Jumper:

	camera_speed = 0.1

	# Called on game initialization
	def __init__(self):
		# Camera only moves up, so we only need a y position
		self.camera_y = 0

		# Create a player at a top-center position
		self.player = Player(SCREEN_WIDTH/2 - Player.width/2, 0) 

		# Create a list of platforms
		# For now, this list will end up containing 100 test platforms
		self.platforms = []

		for i in range(100):
			self.platforms.append(Platform(SCREEN_WIDTH/2 - Platform.width/2, 
								  SCREEN_HEIGHT/2 - Platform.height/2 - i*100))

	# Moves the camera every frame
	def update_camera_position(self, delta_time):
		# Move the camera down
		self.camera_y -= self.camera_speed * delta_time
		# If the player jumps higher than the camera y position, set the camera y to match the
		# position of the player
		if self.player.position.y < self.camera_y:
			self.camera_y = self.player.position.y

	# Updates the game logic every frame
	def update(self, delta_time):
		self.player.resolve_platform_collisions(delta_time, self.platforms)
		self.player.update(delta_time)

		self.update_camera_position(delta_time)

		# Continuously check for key presses
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_RIGHT]:
			self.player.move_right()
		if pressed[pygame.K_LEFT]:
			self.player.move_left()

	# Draws all game objects every frame
	def draw(self, screen):
		for platform in self.platforms:
			platform.draw(screen, self.camera_y)
		self.player.draw(screen, self.camera_y)

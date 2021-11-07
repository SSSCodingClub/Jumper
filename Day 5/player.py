from setup import *
from colors import COLOR_BLACK

class Player:

	width, height = 25, 50
	color = COLOR_BLACK
	jump_power = 0.8
	gravity = 0.0015
	movement_acceleration = 0.0025
	horizontal_resistance = 0.005

	# Called on player creation
	def __init__(self, x, y):
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.acceleration = pygame.Vector2(0, self.gravity)
	
	# Launches the player up
	def jump(self):
		self.velocity.y = -self.jump_power

	# Sets the horizontal acceleration to accelerate left
	def move_left(self):
		self.acceleration.x -= self.movement_acceleration

	# Sets the horizontal acceleration to accelerate right
	def move_right(self):
		self.acceleration.x += self.movement_acceleration
	
	# Makes the player jump when they fall onto a platform
	def resolve_platform_collisions(self, delta_time, platforms):
		# How much error to account for when collision detection is performed
		epsilon = abs(self.velocity.y) * delta_time

		player_left = self.position.x
		player_right = self.position.x + self.width

		for platform in platforms:
			platform_left = platform.position.x 
			platform_right = platform.position.x + platform.width

			# If the player is overlapping horizontally with the platform
			if player_left < platform_right and player_right > platform_left:
				# If the player's bottom is aligned with the top of the platform with error epsilon
				if abs((self.position.y + self.height) - platform.position.y) < epsilon:
					# Only stop the player if it is falling
					if self.velocity.y > 0:
						self.jump()

	# When the player goes off the left or right of the screen, teleport them to the other side
	def screen_wrap(self):
		if self.position.x > SCREEN_WIDTH:
			self.position.x = -self.width
		if self.position.x < -self.width:
			self.position.x = SCREEN_WIDTH

	# Does player logic every frame
	def update(self, delta_time):
		self.position += self.velocity * delta_time
		self.velocity += self.acceleration * delta_time
		self.screen_wrap()

		# Slow down the player; this prevents the player from infinitely increasing their velocity
		# with their acceleration, as well as slows them down when they wish to stop moving
		self.velocity.x *= max(0, 1 - (delta_time * self.horizontal_resistance))

		# Reset x acceleration to zero at the end of every frame. move_left and move_right are
		# called every frame when their respective inputs are pressed, so as long as they are still
		# pressed, acceleration will be increased again. When the input is released, this
		# will handle setting the x acceleration to zero.
		self.acceleration.x = 0

	# Draws player every frame
	def draw(self, screen, camera_y):
		r = pygame.Rect(self.position.x, self.position.y - camera_y, self.width, self.height)
		pygame.draw.rect(screen, self.color, r)
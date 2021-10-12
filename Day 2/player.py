from setup import *

class Player:

	width, height = 25, 50
	color = (0, 0, 0)
	jump_power = 0.8
	gravity = 0.0015

	# Called on player creation
	def __init__(self, x, y):
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0.5, 0)
		self.acceleration = pygame.Vector2(0, self.gravity)
	
	# Launches the player up
	def jump(self):
		self.velocity.y = -self.jump_power
	
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

	# Draws player every frame
	def draw(self, screen):
		r = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
		pygame.draw.rect(screen, self.color, r)
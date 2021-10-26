from setup import *
from player import Player

class Platform:
	
	width, height = 200, 5
	color = (0, 0, 0)

	# Called on platform creation
	def __init__(self, x, y):
		self.position = pygame.Vector2(x, y)

	# Draws the platform every frame
	def draw(self, screen, camera_y):
		r = pygame.Rect(self.position.x, self.position.y - camera_y, self.width, self.height)
		pygame.draw.rect(screen, self.color, r)

class PlatformManager:

	# Spacing interval for platform slots; all platforms will be spaced at a multiple of this value
	platform_spread = 50

	min_slots_between_platforms = 1
	max_slots_between_platforms = 4

	# The slot of the initial platform the player should spawn on
	# It is in the middle of the screen
	starting_platform_slot = (SCREEN_HEIGHT / platform_spread) // 2 + 1

	# Called when the game starts
	def __init__(self):
		# Create a list of platforms that will be used in the game
		self.platforms = []

		# Keeps track of the next slot where a platform will spawn
		self.next_slot = 0

		# Create our initial platforms
		self.spawn_initial_platforms()

	# Spawns a platform at a given slot
	def spawn_platform_at_slot(self, slot, center = False):
		if center == False:
			# Generate a random horizontal position for the next platform
			# This position will range from 0, where the platform will be at the left side, to 
			# SCREEN_WIDTH - Platform.width, where the platform will be at the right side
			platform_position_x = random.random() * (SCREEN_WIDTH - Platform.width)
		else:
			platform_position_x = SCREEN_WIDTH / 2 - Platform.width / 2
		
		# Find the y correct y position of a slot at the specified slot
		platform_position_y = SCREEN_HEIGHT - (self.platform_spread * slot) - Platform.height

		# Create a new platform at the correct position and add it to our list of platforms
		new_platform = Platform(platform_position_x, platform_position_y)
		self.platforms.append(new_platform)
		
	def spawn_initial_platforms(self):
		has_starting_platform_spawned = False

		# How many platform slots fit on the screen initially
		max_initial_slots = SCREEN_HEIGHT // self.platform_spread

		# Keep updating the next slot until we've reached the maximum amount
		# that can fit on the screen
		while self.next_slot < max_initial_slots:
			# If the next slot is above or equal to the middle platform slot, also spawn the middle
			# platform if it hasn't already been spawned
			if self.next_slot >= self.starting_platform_slot and not has_starting_platform_spawned:
				self.spawn_platform_at_slot(self.starting_platform_slot, center = True)
				has_starting_platform_spawned = True

			# Spawn the platform at the next slot if the next slot is not the starting platform
			if self.next_slot != self.starting_platform_slot:
				self.spawn_platform_at_slot(self.next_slot)

			# Calculate the next slot
			self.next_slot += random.randint(self.min_slots_between_platforms, 
											 self.max_slots_between_platforms)       

	def spawn_new_platforms(self, camera_y):
		# While the next platform to spawn is on screen
		while camera_y <= SCREEN_HEIGHT - (self.platform_spread * self.next_slot):
			# Spawn a platform at the slot and calculate the slot where the next platform will spawn
			self.spawn_platform_at_slot(self.next_slot)
			self.next_slot += random.randint(self.min_slots_between_platforms, 
											 self.max_slots_between_platforms) 

	def delete_old_platforms(self, camera_y):
		# If there exists platforms to delete
		if self.platforms:

			# Get the first platform in the list
			# This will always be at the bottom most platform
			platform = self.platforms[0]

			# How far platforms can travel off screen
			# *	Platform height is added to ensure platforms are fully off screen before deletion
			# *	Player height is added so that players that don't completely fall off screen have
			# 	a chance to catch a platform that just went off screen
			offset = Platform.height + Player.height + camera_y

			# If the platform meets the criteria for deletion, delete it
			if platform.position.y > SCREEN_HEIGHT + offset:
				self.platforms.remove(self.platforms[0])

	def update(self, camera_y):
		self.delete_old_platforms(camera_y)
		self.spawn_new_platforms(camera_y)

	# Draws all platforms to the screen
	def draw(self, screen, camera_y):
		for platform in self.platforms:
			platform.draw(screen, camera_y)
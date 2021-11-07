from setup import *
from colors import *
from player import Player
from platform import Platform, PlatformManager

# Class which handles the main game logic and drawing
class Jumper:

	# (Primary, Accent)
	colors = (
		(COLOR_WHITE, COLOR_BLACK),
		(COLOR_LIGHT_PINK, COLOR_BLACK),
		(COLOR_LIGHT_BLUE, COLOR_BLACK),
		(COLOR_LIGHT_YELLOW, COLOR_BLACK),
		(COLOR_ORANGE, COLOR_WHITE),
		(COLOR_OFF_RED, COLOR_WHITE),
		(COLOR_PURPLE, COLOR_WHITE),
		(COLOR_DARK_BLUE, COLOR_WHITE),
		(COLOR_BLACK, COLOR_YELLOW),
		(COLOR_BLACK, COLOR_RED),
		(COLOR_WHITE, COLOR_RED))

	color_switch_interval = 250


	camera_acceleration = 0.0000025
	jump_power_increase_rate = 0.000005

	distance_per_score = 20

	# Called on game initialization
	def __init__(self):
		# Creates an instance of platform manager
		self.platform_manager = PlatformManager()

		self.color_index = 0
		self.color_palette = ColorPalette(self.colors[self.color_index][0], 
										  self.colors[self.color_index][1])

		# Camera only moves up, so we only need a y position
		self.camera_y = 0

		# The speed at which the camera will move up
		self.camera_speed = 0.1

		# Create our player at the position such that it will land on the platform in the middle of 
		# the screen
		starting_platform_position_y = (SCREEN_HEIGHT - 
										PlatformManager.platform_spread *
										PlatformManager.starting_platform_slot -
										Platform.height)

		self.player = Player(SCREEN_WIDTH / 2, starting_platform_position_y - Player.height)

		# Create the variable which will keep track of the user's score
		self.score = 0

	def update_colors(self, delta_time):
		self.color_palette.update(delta_time)

		if (self.color_index + 1) * self.color_switch_interval <= self.score:
			self.color_index += 1

			color_index_mod = self.color_index % len(self.colors)
			self.color_palette = ColorPalette(self.colors[color_index_mod][0],
											  self.colors[color_index_mod][1],
											  self.color_palette)
										
		Player.color = self.color_palette.get_accent_color()
		Platform.color = self.color_palette.get_accent_color()

	# Moves the camera every frame
	def update_camera_position(self, delta_time):
		# Move the camera down
		self.camera_y -= self.camera_speed * delta_time
		# If the player jumps higher than the camera y position, set the camera y to match the
		# position of the player
		if self.player.position.y < self.camera_y:
			self.camera_y = self.player.position.y

	# Increase game difficulty over time
	def update_difficulty(self, delta_time):
		self.camera_speed += delta_time * self.camera_acceleration
		self.player.jump_power += delta_time * self.jump_power_increase_rate

	# Update the score based on the highest y position the player has reached
	def update_score(self):
		self.score = max(self.score, int(-self.player.position.y / self.distance_per_score))

	# Updates the game logic every frame
	def update(self, delta_time):
		self.player.resolve_platform_collisions(delta_time, self.platform_manager.platforms)
		self.player.update(delta_time)

		self.update_difficulty(delta_time)
		self.update_score()

		self.update_camera_position(delta_time)
		self.update_colors(delta_time)

		# Continuously check for key presses
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_RIGHT]:
			self.player.move_right()
		if pressed[pygame.K_LEFT]:
			self.player.move_left()
		
		# Perform platform creation and deletion as necessary
		self.platform_manager.update(self.camera_y)	

	# Draws all game objects every frame
	def draw(self, screen):

		screen.fill(self.color_palette.get_primary_color())
		self.draw_score(screen)
		self.player.draw(screen, self.camera_y)
		self.platform_manager.draw(screen, self.camera_y)
		

	# Draw the score to the screen
	def draw_score(self, screen):
		# Use the largest font
		text_font = FONT_BIGGER
		text_color = self.color_palette.get_text_color()
		# Get the middle of the screen
		position_x, position_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
		# Create a surface with the score drawn on it
		text_surface = text_font.render(str(self.score), True, text_color)
		# Calculate where the top left of the surface should be put
		top_left = (position_x - text_surface.get_width() / 2,
					position_y - text_surface.get_height() / 2)
		# Make the score text translucent
		text_surface.set_alpha(int(255 * 0.25))
		# Draw the text surface onto the screen
		screen.blit(text_surface, top_left)

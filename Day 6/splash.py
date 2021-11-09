from setup import *
from math import sin

class Splash:

	def __init__(self):
		self.time = 0

	def update(self, delta_time):
		self.time += delta_time

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return COMMAND_EXIT
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					return COMMAND_START

	def draw(self, screen):

		# Jumper
		text_font = FONT_BIG
		text_color = (0, 0, 0)
		position_x, position_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.35
		text_surface = text_font.render("Jumper!", True, text_color)

		top_left = (position_x - text_surface.get_width()/2, position_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)

		# Press Space...
		text_font = FONT_SMALL
		text_color = (100, 100, 100)
		position_x, position_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.65
		text_surface = text_font.render("Press space to play", True, text_color)

		text_scale = sin(self.time/500)/6 + 5/6
		text_scale_width = int(text_surface.get_width() * text_scale)
		text_scale_height = int(text_surface.get_height() * text_scale)
		text_surface = pygame.transform.scale(text_surface, (text_scale_width, text_scale_height))

		top_left = (position_x - text_surface.get_width()/2, position_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)
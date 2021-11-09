from setup import *
from colors import *
from math import sin

class GameOverDisplay:

	def __init__(self, new_score, best_score):
		self.time = 0
		self.new_score = new_score
		self.best_score = best_score

	def update(self, delta_time):
		self.time += delta_time

	def draw(self, screen):
		popup_slide_offset = max(0, (10 - self.time*0.01)) ** 3
		popup_color = COLOR_BLACK
		popup_width, popup_height = 400, 500
		popup_x = SCREEN_WIDTH/2 - popup_width/2
		popup_y = SCREEN_HEIGHT/2 - popup_height/2 + popup_slide_offset
		r = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
		pygame.draw.rect(screen, popup_color, r)

		# Game over...
		text_font = FONT_NORMAL
		text_color = COLOR_RED
		text_x, text_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.25 + popup_slide_offset
		text_surface = text_font.render("Game over", True, text_color)

		text_scale = sin(self.time/500)/6 + 5/6
		text_scale_width = int(text_surface.get_width() * text_scale)
		text_scale_height = int(text_surface.get_height() * text_scale)
		text_surface = pygame.transform.scale(text_surface, (text_scale_width, text_scale_height))

		top_left = (text_x - text_surface.get_width()/2, text_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)

		# Your Score text...
		text_font = FONT_TINY
		text_color = COLOR_WHITE
		text_x, text_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.4 + popup_slide_offset
		text_surface = text_font.render(f"Your score: {self.new_score}", True, text_color)

		top_left = (text_x - text_surface.get_width()/2, text_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)

		# Best Score text... (reuse values from previous)
		text_x, text_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.5 + popup_slide_offset
		text_surface = text_font.render(f"Best score: {self.best_score}", True, text_color)

		top_left = (text_x - text_surface.get_width()/2, text_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)

		# Press space to play again text... (reuse values from previous)
		text_x, text_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.7 + popup_slide_offset
		text_surface = text_font.render("Press space to play again", True, text_color)

		top_left = (text_x - text_surface.get_width()/2, text_y - text_surface.get_height()/2)
		screen.blit(text_surface, top_left)
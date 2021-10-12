from setup import *

class Platform:
	
	width, height = 200, 5
	color = (0, 0, 0)

	# Called on platform creation
	def __init__(self, x, y):
		self.position = pygame.Vector2(x, y)

	# Draws the platform every frame
	def draw(self, screen):
		r = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
		pygame.draw.rect(screen, self.color, r)
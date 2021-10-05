from setup import *

class Player:

	width, height = 25, 50
	color = (0, 0, 0)
	gravity = 0.0015

	# Called on player creation
	def __init__(self, x, y):
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0.5, 0)
		self.acceleration = pygame.Vector2(0, self.gravity)
	
	# Does player logic every frame
	def update(self):
		self.position += self.velocity
		self.velocity += self.acceleration

	# Draws player every frame
	def draw(self, screen):
		r = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
		pygame.draw.rect(screen, self.color, r)
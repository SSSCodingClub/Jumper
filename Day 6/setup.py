import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640

FONT_FILE = "font.otf"

FONT_BIGGER = pygame.font.Font(FONT_FILE, 160)
FONT_BIG    = pygame.font.Font(FONT_FILE, 130)
FONT_NORMAL = pygame.font.Font(FONT_FILE, 75)
FONT_SMALL  = pygame.font.Font(FONT_FILE, 60)
FONT_TINY   = pygame.font.Font(FONT_FILE, 30)

COMMAND_EXIT = 0
COMMAND_START = 1
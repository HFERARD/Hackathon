import pygame
import pygame as pg
from pieces import get_piece
from locals import *


class Piece(pg.sprite.Sprite):
	def __init__(self, piece_matrix, colour: int):
		pg.sprite.Sprite.__init__(self)
		self.image = ...
		self.rect = self.image.get_rect()
		self.colour = ... # que joueur possède la pièce

	@staticmethod
	def image_from_matrix(piece_matrix, colour):
		height, width = (len(piece_matrix) - 2, len(piece_matrix[0]) - 2)
		pixel_height, pixel_width = (width * SQUARE_SIZE + (width - 1) * LINE_WIDTH,
									 height * SQUARE_SIZE + (height - 1) * LINE_WIDTH)

		surface = pygame.Surface((pixel_width, pixel_height))
		surface.fill(WHITEc)
		surface.set_colorkey(WHITEc)

		for i in range(height):
			for j in range(width):
				if piece_matrix[i+1][j+1] == 1:
					x = i * SQUARE_SIZE + (i - 1) * LINE_WIDTH
					y = j * SQUARE_SIZE + (j - 1) * LINE_WIDTH
					pygame.draw.rect(surface, PlAYER_COLOUR[colour], (x, y, SQUARE_SIZE, SQUARE_SIZE))




	@classmethod
	def from_piece(cls, piece_matrix):
		height, width = ..., ...


	def set_position(self, x, y):
		self.rect.topleft = (x, y)

	def draw(self, surface : pg.Surface):
		surface.blit(self.image, self.rect)
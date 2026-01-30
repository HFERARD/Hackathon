import pygame as pg
from pieces import get_piece


class Piece(pg.sprite.Sprite):
	def __init__(self, colour: int):
		pg.sprite.Sprite.__init__(self)
		self.image = ...
		self.rect = self.image.get_rect()
		self.colour = ... # que joueur possède la pièce

	@classmethod
	def from_piece(cls, piece_matrix):
		height, width = ..., ...


	def set_position(self, x, y):
		self.rect.topleft = (x, y)


	def update(self):
		pass
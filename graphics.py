import pygame
import pygame as pg
from pieces import get_piece
from locals import *


class PiecesManagement:
	# Pour 4 joueurs à update pour moins
	def __init__(self):
		self.selected_piece : Piece | None = None

		self.pieces = {colour : pg.sprite.Group() for colour in PLAYERS}

		for colour in [RED] :
			for i in range(1, 22):
				self.pieces[colour].add(Piece.from_id(str(i), colour))

		x_, y_ = (10, 10)
		for piece in self.pieces[RED]:
			piece.set_default_position(x_, y_)
			x_ += piece.rect.width + 10


	def select_piece(self, x, y, colour):
		"""
		takes in mouse position and checks whether a piece can be selected
		"""
		for piece in self.pieces[colour]:
			if piece.rect.collidepoint(x, y):
				self.selected_piece = piece

	def unselect(self):
		self.selected_piece.reset_position()
		self.selected_piece = None


	def update(self, x, y):
		if self.selected_piece is not None:
			self.selected_piece.set_position(x, y)

	def draw(self, surface: pg.surface):
		if self.selected_piece is not None:
			surface.blit(self.selected_piece.image, self.selected_piece.rect)
		for group in self.pieces.values():
			for piece in group:
				piece.draw(surface)


class Piece(pg.sprite.Sprite):
	def __init__(self, piece_matrix, colour: int):
		pg.sprite.Sprite.__init__(self)
		self.image = self.image_from_matrix(piece_matrix, colour)
		self.rect = self.image.get_rect()
		self.colour = colour # du joueur qui possède la pièce
		self.piece_matrix = piece_matrix

		self.default_position = (0, 0)

	@staticmethod
	def image_from_matrix(piece_matrix, colour):
		"""
		Creates an image from a standard piece_matrix which can be drawn onto screen for animation

		:param piece_matrix:
		:param colour:
		:return: pygame.Surface
		"""
		height, width = (len(piece_matrix) - 2, len(piece_matrix[0]) - 2)
		pixel_width, pixel_height = (width * SQUARE_SIZE + (width - 1) * LINE_WIDTH,
									 height * SQUARE_SIZE + (height - 1) * LINE_WIDTH)

		surface = pygame.Surface((pixel_width, pixel_height))
		surface.fill(WHITEc)
		surface.set_colorkey(WHITEc)

		for i in range(height):
			for j in range(width):
				if piece_matrix[i+1][j+1] == 1:
					x = j * SQUARE_SIZE + (j - 1) * LINE_WIDTH
					y = i * SQUARE_SIZE + (i - 1) * LINE_WIDTH
					pygame.draw.rect(surface, PlAYER_COLOUR[colour], (x, y, SQUARE_SIZE, SQUARE_SIZE))

		return surface

	@classmethod
	def from_id(cls, id_, colour):
		"""
		:param id_:
		:param colour:
		:return:
		"""
		return cls(get_piece(id_), colour)


	def set_position(self, x, y):
		self.rect.topleft = (x, y)

	def reset_position(self):
		self.rect.topleft = self.default_position

	def set_default_position(self, x, y):
		self.default_position = (x, y)
		self.set_position(x, y)

	def draw(self, surface : pg.Surface):
		surface.blit(self.image, self.rect)
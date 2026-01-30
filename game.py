import pygame as pg
from sys import exit
from locals import *

SIZE = (1000, 600)

SQUARE_SIZE = 27
LINE_WIDTH = 2
N = 20


WHITEc = (255, 255, 255)
BLACKc = (0, 0, 0)
REDc = (255, 0, 0)
GREENc = (0, 255, 0)
BLUEc = (0, 0, 255)
YELLOWc = (255, 255, 0)
GREYc = (128, 128, 128)

# offset de 11 de chaque coté du tableau

class Board:
	def __init__(self):
		# Graphic setup --------------------------

		K = SQUARE_SIZE * N + (N + 1) * LINE_WIDTH
		self.surface = pg.Surface((K, K))
		self.surface.fill(WHITEc)
		self.rect = self.surface.get_rect()
		self.rect.center = (500, 300)

		self.draw_grid()


		# Positions setup --------------------------

		self.status = [[0 for i in range(N)] for j in range(N)] # status of the board at current state


	def draw_grid(self):
		for i in range(N + 1):
			K = self.surface.get_size()[0]
			pg.draw.line(self.surface, BLACKc,
						 (i * (SQUARE_SIZE + LINE_WIDTH), 0), (i * (SQUARE_SIZE + LINE_WIDTH), K), width=LINE_WIDTH)
			pg.draw.line(self.surface, BLACKc,
						 (0, i * (SQUARE_SIZE + LINE_WIDTH)), (K, i * (SQUARE_SIZE + LINE_WIDTH)), width=LINE_WIDTH)

	def add_piece(self, piece ):
		pass


	def draw(self, surface : pg.Surface):
		surface.blit(self.surface, self.rect)




class Game:
	def __init__(self):
		# Game system set up | pygame ----

		self.SCREEN = pg.display.set_mode(SIZE)
		self.CLOCK = pg.time.Clock()
		self.FPS = 60

		self.running = True

		pg.display.set_caption('Blokus | Game by MPVH')

		# Game variables -------------------

		self.table = Board()


	def run(self):
		"""
		Main game loop
		- No arguments
		- return None
		"""
		while self.running:
			self.SCREEN.fill(GREYc)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False

			self.table.draw(self.SCREEN)

			pg.display.update()
			self.CLOCK.tick(self.FPS)

		# Sortie de boucle : fin de jeu
		pg.quit()
		exit()

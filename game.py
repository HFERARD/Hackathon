import pygame as pg
from sys import exit

SIZE = (1000, 600)






class Game:
	def __init__(self):
		self.SCREEN = pg.display.set_mode(SIZE)
		self.CLOCK = pg.time.Clock()
		self.FPS = 60

		self.running = True

		pg.display.set_caption('Blokus | Game by MPVH')


	def run(self):
		"""
		Main game loop
		- No arguments
		- return None
		"""
		while self.running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False


			pg.display.update()
			self.CLOCK.tick(self.FPS)

		# Sortie de boucle : fin de jeu
		pg.quit()
		exit()

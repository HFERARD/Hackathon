import pygame as pg
from sys import exit
from locals import *
from graphics import PiecesManagement, Piece
#from pieces import get_piece

SIZE = (1000, 800)


"""
-1 : case non-jouable pour le joueur selectionné
0 : case vide 
1 : case remplie par le joueur
10 : case adjecent à un coin (au moins une par tour)

"""

# offset de 11 de chaque coté du tableau

class Board:
	def __init__(self):
		# Graphic setup --------------------------

		K = SQUARE_SIZE * N + (N + 1) * LINE_WIDTH
		self.surface = pg.Surface((K, K))
		self.surface.fill(WHITEc)
		self.rect = self.surface.get_rect()
		self.rect.center = (500, 400)

		self.dynamic_overlay = self.surface.copy()
		self.dynamic_overlay.set_colorkey(WHITEc)
		self.pieces_positions = self.surface.copy()
		self.pieces_positions.set_colorkey(WHITEc)

		self.draw_grid()


		# Positions setup --------------------------

		self.status = [[[0, 0, 0, 0] for i in range(N+2)] for j in range(N+2)] # status of the board at current state
		for i in range(0,N+2):
			self.status[i][0] = [-1, -1, -1, -1]
			self.status[i][N+1] = [-1, -1, -1, -1]
			self.status[0][i] = [-1, -1, -1, -1]
			self.status[N+1][i] = [-1, -1, -1, -1]
		self.status[1][1] = [10,10,10,10]
		self.status[1][N] = [10,10,10,10]
		self.status[N][1] = [10,10,10,10]
		self.status[N][N] = [10,10,10,10]
		# sur chaque case [joueur1, joueur2, joueur3, joueur4]

		#self.add_piece()

	@staticmethod
	def real_position(i):
		return SQUARE_SIZE * i + (i + 1) * LINE_WIDTH


	def draw_grid(self):
		for i in range(N + 1):
			K = self.surface.get_size()[0]
			pg.draw.line(self.surface, BLACKc,
						 (i * (SQUARE_SIZE + LINE_WIDTH), 0),
						 (i * (SQUARE_SIZE + LINE_WIDTH), K),
						 width=LINE_WIDTH)
			pg.draw.line(self.surface, BLACKc,
						 (0, i * (SQUARE_SIZE + LINE_WIDTH)),
						 (K, i * (SQUARE_SIZE + LINE_WIDTH)),
						 width=LINE_WIDTH)


	def valid_move(self, piece, topleft, colour):
		"""
		For a piece of colour :colour:, return if this move is valid:
			- Corner connection
			- No edges from same colour touch
		"""
		lignes = len(piece)
		colonnes = len(piece[0])
		corner = False # vérifie si deux coins se touchent càd si la pièce recouvre au moins un 10
		for j in range(colonnes):
			for i in range(lignes):
				x, y = (i + topleft[0], j + topleft[1])  # coordonnées
				if piece[i][j] == 1:
					if self.status[y][x][colour] == -1: # Case non-jouable
						return False
					if self.status[y][x][colour] == 10: # Case adjacente à un coin
						corner = True
		return corner


	def add_piece(self, piece, topleft, colour: int):
		"""
		:param piece: matrice de type
		:param topleft: position du carré (x, y)
		:param colour: couleur du joueur (constante int)
		:return: None

		Adds piece to the status matrix if move is valid and draws piece to board surface
		"""

		x, y = (topleft[0] - 1, topleft[1] - 1)
		if self.valid_move(piece, topleft, colour):
			for i, row in enumerate(piece):
				for j, stat in enumerate(row):
					# Add to status board
					self.status[i + y][j + x][colour] = piece[i][j]
					# Draw to surface
					if stat == 1:
						pg.draw.rect(self.pieces_positions, PlAYER_COLOUR[colour],
								(self.real_position(j + x), self.real_position(i + y),
								 SQUARE_SIZE, SQUARE_SIZE))

	def update(self):
		pass


	def draw(self, surface : pg.Surface):
		surface.blit(self.surface, self.rect)
		surface.blit(self.dynamic_overlay, self.rect)
		surface.blit(self.pieces_positions, self.rect)

	def dynamic_add(self, x, y, piece: Piece):
		i = (x - (self.rect.left + LINE_WIDTH)) // (SQUARE_SIZE + LINE_WIDTH)
		j = (y - (self.rect.top + LINE_WIDTH)) // (SQUARE_SIZE + LINE_WIDTH)

		print(i, j)
		self.add_piece(piece.piece_matrix, (i,j), piece.colour)




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

		self.pieces_management = PiecesManagement()

		self.clicked = True

		self.current_colour = RED


	def run(self):
		"""
		Main game loop
		- No arguments
		- return None
		"""
		while self.running:
			self.SCREEN.fill(GREYc)
			mx, my = pg.mouse.get_pos()

			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False

				if event.type == pg.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.clicked = True
						self.pieces_management.select_piece(mx, my, self.current_colour)
				if event.type == pg.MOUSEBUTTONUP:
					if event.button == 1:
						self.clicked = False
						if self.pieces_management.selected_piece is not None:
							if self.table.rect.collidepoint(mx, my):
								self.table.dynamic_add(mx, my, self.pieces_management.selected_piece)

							self.pieces_management.unselect()


			# Draw table
			self.table.draw(self.SCREEN)


			# Update and draw pieces before they appear on the board
			self.pieces_management.draw(self.SCREEN)
			if self.clicked:
				self.pieces_management.update(mx, my)


			pg.display.update()
			self.CLOCK.tick(self.FPS)

		# Sortie de boucle : fin de jeu
		pg.quit()
		exit()

pieces = [
    [
        [None,-1,0,-1,None],
        [-1,0,1,0,-1],
        [0,1,1,1,0],
        [-1,0,1,0,-1],
        [None,-1,0,-1,None]
    ],
    [
         [None,-1,0,-1],
         [-1, 0, 1,0],
         [0,  1, 1,0],
         [0,  1, 1,0],
         [-1, 0, 0,-1]
     ]
]

def rotation_sens_trigo(piece):
    """
    tourne une piece dans le sens trigo
    """
    ligne = len(piece)
    colonne = len(piece[0])
    new_piece = [[0 for i in range(ligne)] for j in range(colonne)]
    for i in range(ligne):
        for j in range(colonne):
            new_piece[colonne-1-j][i] = piece[i][j]
    return new_piece

def get_piece(piece, joueur):
    """
    renvoie le format écrit sur le tableau pour la pièce d'un joueur
    """
    ligne = len(piece)
    colonne = len(piece[0])
    new_piece = [[0 for j in range(colonne)] for i in range(ligne)]
    for i in range(ligne):
        for j in range(colonne):
            if piece[i][j] == None:
                new_piece[i][j] = 0
            elif piece[i][j] == 1:
                new_piece[i][j] = joueur
            elif piece[i][j] == 0:
                new_piece[i][j] = -joueur
            else:
                new_piece[i][j] = 10*joueur
    return new_piece

def affiche(piece):
    """
    affiche une piece dans le terminal
    """
    for ligne in piece:
        print(ligne)
    print()


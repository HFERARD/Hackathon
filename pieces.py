pieces = { 
    "1": 
          [[-1,0,-1], 
           [ 0,1, 0], 
           [-1,0,-1]], 
    "2": 
    [[-1,0,-1], 
        [ 0,1, 0],
        [ 0,1, 0],
        [-1,0,-1]],
     "3":
    [[-1, 0,-1], 
     [ 0, 1, 0], 
     [ 0, 1, 0],
     [ 0, 1, 0], 
     [-1, 0,-1]],
     "4":
    [[-1, 0,-1, None], 
     [ 0, 1, 0, None], 
     [ 0, 1, 1, 0], 
     [-1, 0, 0,-1]],
     "5":
     [
        [-1, 0,-1], 
        [ 0, 1, 0], 
        [ 0, 1, 0],
        [ 0, 1, 0],
        [ 0, 1, 0], 
        [-1, 0,-1]
     ],
     "6":
     [
        [None, -1, 0,-1], 
        [None,  0, 1, 0], 
        [  -1,  0, 1, 0],
        [   0,  1, 1, 0],
        [  -1,  0, 0,-1],
     ],
     "7":
     [
        [-1, 0,-1,None],
        [ 0, 1, 0,  -1],
        [ 0, 1, 1,   0],
        [ 0, 1, 0,  -1],
        [-1, 0,-1,None]
     ],
     "8":
     [
         [-1, 0, 0,-1],
         [ 0, 1, 1, 0],
         [ 0, 1, 1, 0],
         [-1, 0, 0,-1]
     ],
     "9":
     [
         [  -1, 0, 0,-1,None],
         [   0, 1, 1, 0,  -1],
         [  -1, 0, 1, 1,   0],
         [None,-1, 0, 0,  -1]
     ],
     "10":
     [
        [-1,0,-1], 
        [0,1,0], 
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0], 
        [-1,0,-1]
     ],
     "11":
     [
        [None, -1, 0,-1],
        [None,  0, 1, 0],
        [  -1,  0, 1, 0],
        [  -1,  0, 1, 0], 
        [   0,  1, 1, 0],
        [  -1,  0, 0,-1]
     ],
     "12":
     [
         [None, -1, 0, -1],
         [None,  0, 1,  0],
         [-1,    0, 1,  0],
         [ 0,    1, 1,  0],
         [ 0,    1, 0, -1],
         [-1,    0,-1,None]
     ],
     "13":
     [
         [None,-1,0,-1],
         [-1, 0, 1,  0],
         [0,  1, 1,  0],
         [0,  1, 1,  0],
         [-1, 0, 0, -1]
     ],
     "14":
     [
         [-1, 0, 0, -1],
         [0,  1,  1, 0],
         [-1, 0,  1, 0],
         [0,  1,  1, 0],
         [-1, 0,  0, -1]
     ],
     "15":
     [
         [-1,  0, -1, None],
         [ 0,  1,  0, -1],
         [ 0,  1,  1,  0],
         [ 0,  1,  0, -1],
         [ 0,  1,  0, None],
         [-1,  0, -1, None]
     ],
     "16":
    [
        [None, -1, 0, -1, None],
        [None,  0, 1, 0, None],
        [ -1,   0, 1, 0, -1],
        [  0,   1, 1, 1,  0],
        [ -1,   0, 0, 0, -1]
    ],
    "17":
    [
        [-1,  0, -1, None, None],
        [ 0,  1,  0, None, None],
        [ 0,  1,  0,    0,  -1],
        [ 0,  1,  1,    1,   0],
        [-1,  0,  0,    0,  -1]
    ],
    "18":
    [
        [  -1,    0,   0, -1, None],
        [   0,    1,   1,  0,  -1],
        [  -1,    0,   1,  1,   0],
        [None,   -1,   0,  1,   0],
        [None, None,  -1,  0,  -1]
    ],
    "19":
    [
        [  -1,  0, -1, None, None],
        [   0,  1,  0,    0,  -1],
        [  -1,  1,  1,    1,   0],
        [None,  0,  0,    1,   0],
        [None,  0, -1,    0,  -1]
    ],
    "20":
    [
        [  -1,  0,  -1,None, None],
        [   0,  1,   0,   0,   -1],
        [   0,  1,   1,   1,    0],
        [  -1,  0,   1,   0, None],
        [None, -1,   0,  -1, None]
    ],
    "21":
    [
        [None, -1, 0, -1, None],
        [  -1,  0, 1,  0,   -1],
        [   0,  1, 1,  1,    0],
        [  -1,  0, 1,  0,   -1],
        [None, -1, 0, -1, None]
    ]
} 

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

def symetrie_verticale(piece):
    """
    t'a capté mon reuf"
    """
    ligne = len(piece)
    colonne = len(piece[0])
    new_piece = [[0 for j in range(colonne)] for i in range(ligne)]
    for i in range(ligne):
        for j in range(colonne):
            new_piece[i][j] = piece[i][colonne-1-j]
    return new_piece
 


def get_piece(id):
    piece = pieces[id]
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
            elif piece[i][j] == 0:
                new_piece[i][j] = -1
            elif piece[i][j] == 1:
                new_piece[i][j] = 1
            else:
                new_piece[i][j] = 10
    return new_piece



def affiche(piece):
    """
    affiche une piece dans le terminal
    """
    for ligne in piece:
        print(ligne)
    print()

affiche(get_piece("6"))
affiche(symetrie_verticale(get_piece("6")))
pieces = [

    [[None,-1,0,-1,None],
    [-1,0,1,0,-1],
    [0,1,1,1,0],
    [-1,0,1,0,-1],
    [None,-1,0,-1,None]]

]

def rotation_sens_trigo(piece):
    ligne = len(piece)
    colonne = len(piece[0])
    new_piece = [[0 for i in range(ligne)] for j in range(colonne)]
    for i in range(ligne):
        for j in range(colonne):
            new_piece[colonne-1-j][i] = piece[i][j]
    return new_piece

print(pieces[0])
print(rotation_sens_trigo(pieces[0]))
NONE =   0b000000
PAWN =   0b000001
KING =   0b000010
KNIGHT = 0b000011
BISHOP = 0b000100
ROOK =   0b001000
QUEEN =  0b001100

BLACK =  0b010000
WHITE =  0b100000

piece_texture_map = {
    "p": "Black Pawn",
    "b": "Black Bishop",
    "n": "Black Knight",
    "r": "Black Rook",
    "q": "Black Queen",
    "k": "Black King",
    "P": "White Pawn",
    "B": "White Bishop",
    "N": "White Knight",
    "R": "White Rook",
    "Q": "White Queen",
    "K": "White King" 
}

piece_id_map = {
    "p": PAWN | BLACK,
    "b": BISHOP | BLACK,
    "n": KNIGHT | BLACK,
    "r": ROOK | BLACK,
    "q": QUEEN | BLACK,
    "k": KING | BLACK,
    "P": PAWN | WHITE,
    "B": BISHOP | WHITE,
    "N": KNIGHT | WHITE,
    "R": ROOK | WHITE,
    "Q": QUEEN | WHITE,
    "K": KING | WHITE
}

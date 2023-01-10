import re
import pieces


class Board:
    piece_positions: dict[tuple[int, int], int] = dict()
    en_passant: int = -1
    castleing: int = 0
    white_to_move: bool = True
    moves_since_last_action: int = 0
    next_round: int = 1

    def __init__(self, start_fen: str):
        [ranks, to_move, castleing, en_passant, moves, round] = start_fen.split()
        ranks = ranks.split("/")
        rank_indices = reversed(range(8))

        castleing_string = "KQkq"
        self.castleing = 0
        for c in castleing:
            if c in castleing_string:
                self.castleing += 2**castleing_string.index(c)

        self.white_to_move = to_move == "w"
        self.en_passant = -1 if en_passant == '-' else ord(en_passant[0]) - ord('a') + int(en_passant[1]) << 3
        self.moves_since_last_action = moves
        self.next_round = round
        
        for rank in ranks:
            rank_index = next(rank_indices)
            file_index = 0
            for char in rank:
                if re.match(r"\d", char):
                    file_index += int(char)
                    continue
                self.piece_positions[(file_index, rank_index)] = pieces.piece_id_map[char]
                file_index += 1
    
    def __str__(self):
        ranks = list()
        infos = list()
        id_piece_map = {v: k for k, v in pieces.piece_id_map.items()}

        for rank in reversed(range(8)):
            empty_counter = 0
            rank_str = ""
            for file in reversed(range(8)):
                pos = (file, rank)
                if pos in self.piece_positions:
                    if empty_counter != 0:
                        rank_str += str(empty_counter)
                    rank_str += id_piece_map[self.piece_positions[pos]]
                else:
                    empty_counter += 1
            if empty_counter != 0:
                rank_str += str(empty_counter)
            ranks.append(rank_str)
        infos.append("/".join(ranks))
        infos.append("w" if self.white_to_move else "b")

        castling_string = "KQkq"
        permitted_castles = ""

        for i in range(4):
            if self.castleing and 2**i == 2**i:
                permitted_castles += castling_string[i]
        
        infos.append(permitted_castles or "-")
        infos.append("-" if self.en_passant == -1 else chr(self.en_passant & 7) + str(self.en_passant >> 3))
        infos.append(str(self.moves_since_last_action))
        infos.append(str(self.next_round))

        return " ".join(infos)


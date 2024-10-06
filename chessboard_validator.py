squares = ["1a", "1b", "1c", "1d", "1e", "1f", "1g", "1h",
           "2a", "2b", "2c", "2d", "2e", "2f", "2g", "2h",
           "3a", "3b", "3c", "3d", "3e", "3f", "3g", "3h",
           "4a", "4b", "4c", "4d", "4e", "4f", "4g", "4h",
           "5a", "5b", "5c", "5d", "5e", "5f", "5g", "5h",
           "6a", "6b", "6c", "6d", "6e", "6f", "6g", "6h",
           "7a", "7b", "7c", "7d", "7e", "7f", "7g", "7h",
           "8a", "8b", "8c", "8d", "8e", "8f", "8g", "8h"]

piece_count = {"wking": 1, "bking": 1, "wqueen": 1, "bqueen": 1, "wrook": 2, "brook": 2, "wknight": 2, "bknight": 2,
               "wbishop": 2, "bbishop": 2, "wpawn": 8, "bpawn": 8}

def verify_board(board):
    invalid_square_error = False
    invalid_pieces = False
    invalid_number_of_pieces = False
    king_error = False
    double_occupancy_error = False
    board_count = {}
    square_occupants_count = {}
    for square in board:
        if square not in squares:
            invalid_square_error = True
            break
    for piece in board.values():
        if piece not in piece_count:
            invalid_pieces = True
        board_count.setdefault(piece, 0)
        board_count[piece] += 1
    # for s in board.keys():           this block of code doesn't work like I thought it would.  Python doesn't count keys of the same name separately.
    #     print(s)
    #     square_occupants_count.setdefault(s, 0)
    #     square_occupants_count[s] += 1
    #     print(len(board))
    # for s, c in square_occupants_count.items():
    #    if c > 1:
    #        double_occupancy_error = True
    if "wking" not in board.values() or "bking" not in board.values():
            king_error = True
    if not invalid_pieces:
        for piece, count in board_count.items():
            if count > piece_count[piece]:
                invalid_number_of_pieces = True
                break
    if king_error or invalid_number_of_pieces or invalid_pieces or invalid_square_error:
        if invalid_square_error:
            print("Game not valid. There are squares that do not exist.")
        if invalid_pieces:
            print("Game not valid. There are pieces that do not exist.")
        if king_error:
            print("Game not valid. One or more kings are missing.")
        if invalid_number_of_pieces:
            print("Game not valid. The number of pieces exceeds maximum limits.")
    else:
        print("Valid game.")

game1 = {"8a": "bking", "3b": "wking", "5h": "wqueen", "6b": "wknight"}

verify_board(game1)

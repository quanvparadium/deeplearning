from utils import print_board, move

player1_score = 0
player2_score = 0

def test_basic(index, rotation=True):
    board = [1000, 5, 5, 5, 5, 5, 1000, 5, 5, 5, 5, 5]

    print("BEFORE MOVE")
    print_board(board)

    print(f"AFTER MOVE: INDEX {index} ROTATION {'CLOCKWISE' if rotation else 'COUNTER-CLOCK'}")
    score = move(board, index, rotation)
    print_board(board)
    print("SCORE", score)    

def test_1(index, rotation=True):
    board = [1, 1, 3, 2, 3, 1, 1000, 1, 4, 1, 2, 1]
    print("BEFORE MOVE")
    print_board(board)

    print(f"AFTER MOVE: INDEX {index} ROTATION {'CLOCKWISE' if rotation else 'COUNTER-CLOCK'}")
    score = move(board, index, rotation)
    print_board(board)
    print("SCORE", score)

def test_2(index, rotation=True):
    board = [0, 4, 1, 3, 1, 5, 0, 5, 1, 5, 1, 5]
    print("BEFORE MOVE")
    print_board(board)

    print(f"AFTER MOVE: INDEX {index} ROTATION {'CLOCKWISE' if rotation else 'COUNTER-CLOCK'}")
    score = move(board, index, rotation)
    print_board(board)
    print("SCORE", score)    

if __name__ == "__main__":
    board = [10, 5, 5, 0, 5, 5, 10, 5, 5, 5, 5, 5]
    # print
    possible_move = [index+1 for index in range(5) if board[index + 1] != 0]
    print(possible_move)
    # print_board(board)

    # move(board, 3, False)
    # print_board(board)
    # print("PLAYER 1 - SCORE: ", player1_score)
    # print("PLAYER 2 - SCORE: ", player2_score)
    # test_1(11, False)
    # test_basic(3, True)
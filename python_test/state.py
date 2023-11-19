from utils import print_board, move
import copy

class State:
    def __init__(self, board, player, player1_score, player2_score):
        """
        Input
        ----------
            board: map(12);
            player: 1 or -1, represent for player
            player1_score: Score player 1
            player2_score: Score player 2

        """
        self.board = board
        self.player = player
        self.player1_score = player1_score
        self.player2_score = player2_score
    
    def get_possible_moves(self):
        if self.player == 1:
            possible_move = [(index+1, True) for index in range(5) if self.board[index + 1] != 0]
            possible_move += [(index+1, False) for index in range(5) if self.board[index + 1] != 0]
        elif self.player == -1:
            possible_move = [(index+7, True) for index in range(5) if self.board[index + 7] != 0]
            possible_move += [(index+7, False) for index in range(5) if self.board[index + 7] != 0]
        else:
            assert "ERROR PLAYER"
        return possible_move    
       
    def print_board(self):
        print_board(self.board)
    
    def print_score(self):
        print("SCORE PLAYER 1: ", self.player1_score)
        print("SCORE PLAYER 2: ", self.player2_score)
    
    def gap_score(self):
        return self.player1_score - self.player2_score

def get_state(state: State, index, is_clockwise):
    new_board = copy.deepcopy(state.board)
    score = move(new_board, index, is_clockwise)
    if state.player == 1:
        new_state = State(new_board, -1, state.player1_score + score, state.player2_score)
    else:
        new_state = State(new_board, 1, state.player1_score, state.player2_score + score)
    return new_state
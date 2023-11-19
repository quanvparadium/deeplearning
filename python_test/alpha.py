import numpy as np
import sys
import os
import random
import time
import copy
from state import State, get_state

MAX_DEPTH = 4

def minimax_move(state):

    visited_states = {}
    def _calculate_score(state: State):
        return state.gap_score()

    def _is_visited(state, depth):
        return state in visited_states \
            and visited_states[state][depth] is not None
    
    def _add_visited_state(state, depth, score, action):
        if state not in visited_states:
            visited_states[state] = [None]*(MAX_DEPTH+1)
        visited_states[state][depth] = (action, score)

    def _minimax(state: State, depth, alpha, beta):
        if (depth == 0):
            return (), _calculate_score(state)
        
        if _is_visited(state, depth):
            return visited_states[state][depth] 

        possible_moves = state.get_possible_moves()
        best_action = ()   

        if state.player == 1:
            # print("PLAYER 1")
            max_value = -10000    
            for (possible_move, direction) in possible_moves:
                # print(direction)
                next_move = (possible_move, direction)
                next_state = get_state(state, possible_move, direction)

                if _is_visited(next_state, depth - 1):
                     action, value = visited_states[next_state][depth-1]
                else:
                    action, value = _minimax(next_state, depth-1, alpha, beta)
                    _add_visited_state(next_state, depth-1, value, action)

                if value > max_value:
                    max_value = value
                    best_action = next_move
                        
                alpha = max(alpha, max_value)
                if(beta <= alpha):
                    break
            if best_action is None:
                print("CANNOT BEST ACTION")
                best_action = possible_move[0]
            # print("PLAYER 1 ENDED")
            # print("PLAYER 1:", best_action, max_value)
            return best_action, max_value    
        else:
            # print("PLAYER 2")
            min_value = 10000
            for (possible_move, direction) in possible_moves:
                next_move = (possible_move, direction)
                next_state = get_state(state, possible_move, direction)
                if _is_visited(next_state, depth - 1):
                     action, value = visited_states[next_state][depth-1]
                else:
                    action, value = _minimax(next_state, depth-1, alpha, beta)
                    _add_visited_state(next_state, depth-1, value, action)

                if value < min_value:
                    min_value = value
                    best_action = next_move
                        
                beta = min(beta, min_value)
                if(beta <= alpha):
                    break

            if best_action is None:
                print("CANNOT BEST ACTION")
                best_action = possible_move[0]
            # print("PLAYER 2:", best_action, min_value)


            return best_action, min_value  

    action, _ = _minimax(state, MAX_DEPTH, -10000, 10000)
    return action         

if __name__ == "__main__":
    board = [1000, 1, 3, 1, 3, 1, 1000, 0, 4, 1, 2, 1]
    print("BEFORE MOVE")
    
    PLAYER1_SCORE = 0
    PLAYER2_SCORE = 0
    state = State(board, -1, PLAYER1_SCORE, PLAYER2_SCORE)
    state.print_board()
    a = minimax_move(state)
    print(f"AFTER MOVE - DEPTH {MAX_DEPTH}")
    new_state = get_state(state, a[0], a[1])
    new_state.print_board()
    print("BEST MOVE: ", a) 
    print(new_state.gap_score())
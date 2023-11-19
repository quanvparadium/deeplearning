# import numpy


player1_score = 0
player2_score = 0

def print_board(board):
    print("""
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
    ''      ''      ''      ''      ''      ''      ''      ''
    ''      ''  {b:02d}  ''  {c:02d}  ''  {d:02d}  ''  {e:02d}  ''  {f:02d}  ''      ''
    ''      ''      ''      ''      ''      ''      ''      ''          
    ''  {a:02d}  ''''''''''''''''''''''''''''''''''''''''''  {g:02d}  ''
    ''      ''      ''      ''      ''      ''      ''      ''
    ''      ''  {l:02d}  ''  {k:02d}  ''  {j:02d}  ''  {i:02d}  ''  {h:02d}  ''      ''
    ''      ''      ''      ''      ''      ''      ''      ''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
""".format(a=board[0], b=board[1], c=board[2], d=board[3], e=board[4], f=board[5], 
           g=board[6], h=board[7], i=board[8], j=board[9], k=board[10], l=board[11]))

def single_move(index, is_clockwise):
    if index == 0 or index == 6:
        print("CANNOT MOVE")
        return -1
    if board[index] == 0:
        print("DON'T HAVE STONE TO MOVE")
        return -1
    if is_clockwise:
        total_stone = board[index]
        board[index] = 0
        for stone in range(total_stone):
            board[(index + 1 + stone) % 12] += 1
        return (index + 2 + stone) % 12
    else:
        total_stone = board[index]        
        board[index] = 0
        for stone in range(total_stone):
            board[(index - 1 - stone) % 12] += 1
        return (index - 2 - stone) % 12

def move(index, is_clockwise):
    global player1_score, player2_score
    previous_index = index
    next_index = single_move(previous_index, is_clockwise)
    while (next_index != -1):
        previous_index = next_index
        next_index = single_move(previous_index, is_clockwise)
    print(previous_index, next_index)
    if is_clockwise:
        if board[previous_index + 1] != 0:
            if 1 <= index <= 5:
                player1_score += board[previous_index + 1]
            elif  7 <= index <= 11:
                player2_score += board[previous_index + 1]
            else:
                print("CANNOT EAT - INDEX ", previous_index + 1)
            board[previous_index + 1] = 0                
    else:
        if board[previous_index - 1] != 0:
            if 1 <= index <= 5:
                player1_score += board[previous_index - 1]
            elif  7 <= index <= 11:
                player2_score += board[previous_index - 1]
            else:
                print("CANNOT EAT - INDEX ", previous_index - 1)
            board[previous_index - 1] = 0                
            

if __name__ == "__main__":
    board = [10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]
    print_board(board)

    move(3, False)
    print_board(board)
    print("PLAYER 1 - SCORE: ", player1_score)
    print("PLAYER 2 - SCORE: ", player2_score)


    
def print_board(board):
    print("""
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
    ''        ''      ''      ''      ''      ''      ''        ''
    ''        ''  {b:02d}  ''  {c:02d}  ''  {d:02d}  ''  {e:02d}  ''  {f:02d}  ''        ''
    ''        ''      ''      ''      ''      ''      ''        ''          
    ''  {a:04d}  ''''''''''''''''''''''''''''''''''''''''''  {g:04d}  ''
    ''        ''      ''      ''      ''      ''      ''        ''
    ''        ''  {l:02d}  ''  {k:02d}  ''  {j:02d}  ''  {i:02d}  ''  {h:02d}  ''        ''
    ''        ''      ''      ''      ''      ''      ''        ''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
""".format(a=board[0], b=board[1], c=board[2], d=board[3], e=board[4], f=board[5], 
           g=board[6], h=board[7], i=board[8], j=board[9], k=board[10], l=board[11]))


def capture(board, index, is_clockwise):
    if is_clockwise: rotation = 1
    else: rotation = -1
    offset = 0
    capture_score = 0
    while True:
        if board[(index + rotation*(offset + 1)) % 12] != 0: break
        if board[(index + rotation*(offset + 2)) % 12] != 0:
            capture_score += board[(index + rotation*(offset + 2)) % 12]
            board[(index + rotation*(offset + 2)) % 12] = 0
        else:
            break
        offset += 2
    return capture_score

def single_move(board, index, is_clockwise):
    """
        Return: current_index, next_index (if have)
    """
    if is_clockwise: rotation = 1
    else: rotation = -1
    total_stone = board[index]
    if index == 0 or index == 6:
        if board[index] // 1000 == 1:
            return index, -1
    elif total_stone == 0:
        return index, -1
    board[index] = 0
    for stone in range(total_stone):
        board[(index + rotation*(1 + stone)) % 12] += 1
    return (index + rotation*(total_stone)) % 12, (index + rotation*(1 + total_stone)) % 12 

def move(board, index, is_clockwise):
    next_index = index
    list_move = []
    while True:
        current_index, next_index = single_move(board, next_index, is_clockwise)
        list_move.append((current_index, next_index))
        if next_index in [-1, 0, 6]: 
            if (next_index in [0, 6]) and board[next_index] // 1000 == 0:
                continue
            break
    if list_move[-1][1] != -1:
        score = capture(board, list_move[-1][0], is_clockwise)    
    else:
        score = capture(board, list_move[-2][0], is_clockwise)    
    return score
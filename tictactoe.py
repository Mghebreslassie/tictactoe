def display_board(board):
    for x in range(7,0,-3):
        print(board[x: x+3])

def get_player_move(board):
    while True:
        position = ''
        try:
            position = int(input('Choose a position between 1 - 9'))
        except:
            print('invalid option')
        if position in range(1,10) and board[position] not in ['X','O']:
            return position
        else:
            print('please choose between 1 - 9')
        
        
def update_board(symbol, board):
    position = get_player_move(board)
    print(f"Player {symbol} moved to position {position}")
    board[position] = symbol

def change_player(symbol):
    if symbol == 'X':
        return 'O'
    else: 
        return 'X'

def check_for_win(board, symbol):
    connect_three = list(symbol)*3
    if connect_three == board[1:4]:
        return True
    elif connect_three == board[4:7]:
        return True
    elif connect_three == board[7:10]:
        return True
    elif connect_three == board[1:10:4]:
        return True
    elif connect_three == board[3:8:2]:
        return True
    elif connect_three == board[1:8:3]:
        return True
    elif connect_three == board[2:9:3]:
        return True
    elif connect_three == board[3:10:3]:
        return True
    else:
        return False



def tictactoe():
    print('Welcome to the game!')
    #check for true/false
    #validate input
    game_on = True
    while game_on:
        playing = input('Press \'y\' to play?')
        if playing[0].lower() == 'y':
            playing = True
        else:
            break
        player = 'X'
        
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        while playing == True:
            #get player coord and symb
            #validate pos chosen
            display_board(board)
            update_board(player, board)
            game_over = check_for_win(board, player)
            if game_over == True:
                print('Congrats player {} won!'.format(player))
                display_board(board)
                break
            else:
                player = change_player(player)
        replay = input('type y for a rematch')
        if replay[0].lower() == 'y':
            game_on = True
        else:
            game_on = False


tictactoe()
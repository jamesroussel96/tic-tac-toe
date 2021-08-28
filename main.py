import sys

game_state = True

#game board images
game_values = ['-', 'O', 'X']

global game_board

# All possible game board positions expressed as key value pairs
game_board = {'top_left': game_values[0], 'top_middle': game_values[0], 'top_right': game_values[0],
              'left': game_values[0], 'middle': game_values[0], 'right': game_values[0], 'bottom_left': game_values[0],
              'bottom_middle': game_values[0], 'bottom_right': game_values[0]}

def board():
# Visual representation of game board 
    print('|', game_board['top_left'], '|', game_board['top_middle'], '|', game_board['top_right'],  '|\n'
          '|', game_board['left'], '|', game_board['middle'], '|', game_board['right'],  '|\n'
          '|', game_board['bottom_left'], '|', game_board['bottom_middle'], '|', game_board['bottom_right'],  '|\n'
          '')
board()

#check all possible winning combinations
def board_status():
    if all([game_board['top_left'] == game_values[1], game_board['top_middle'] == game_values[1],
            game_board['top_right'] == game_values[1]]) or all([game_board['top_left'] == game_values[2],
            game_board['top_middle'] == game_values[2], game_board['top_right'] == game_values[2]]):
        global game_state
        game_state = False
    elif all([game_board['left'] == game_values[1], game_board['middle'] == game_values[1],
            game_board['right'] == game_values[1]]) or all([game_board['left'] == game_values[2],
            game_board['middle'] == game_values[2], game_board['right'] == game_values[2]]):
        game_state = False
    elif all([game_board['bottom_left'] == game_values[1], game_board['bottom_middle'] == game_values[1],
            game_board['bottom_right'] == game_values[1]]) or all([game_board['bottom_left'] ==
            game_values[2], game_board['bottom_middle'] == game_values[2],game_board['bottom_right'] == game_values[2]]):
        game_state = False
    elif all([game_board['top_left'] == game_values[1], game_board['left'] == game_values[1],
            game_board['bottom_left'] == game_values[1]]) or all([game_board['top_left'] == game_values[2],
            game_board['left'] == game_values[2], game_board['bottom_left'] == game_values[2]]):
        game_state = False
    elif all([game_board['top_middle'] == game_values[1], game_board['middle'] == game_values[1],
            game_board['bottom_middle'] == game_values[1]]) or all([game_board['top_middle'] == game_values[2],
            game_board['middle'] == game_values[2], game_board['bottom_middle'] == game_values[2]]):
        game_state = False
    elif all([game_board['top_right'] == game_values[1], game_board['right'] == game_values[1],
            game_board['bottom_right'] == game_values[1]]) or all([game_board['top_right'] == game_values[2],
            game_board['right'] == game_values[2], game_board['bottom_right'] == game_values[2]]):
        game_state = False
    elif all([game_board['top_left'] == game_values[1], game_board['middle'] == game_values[1],
            game_board['bottom_right'] == game_values[1]]) or all([game_board['top_left'] == game_values[2],
            game_board['middle'] == game_values[2], game_board['bottom_right'] == game_values[2]]):
        game_state = False
    elif all([game_board['top_right'] == game_values[1], game_board['middle'] == game_values[1],
            game_board['bottom_left'] == game_values[1]]) or all([game_board['top_right'] == game_values[2],
            game_board['middle'] == game_values[2], game_board['bottom_left'] == game_values[2]]):
        game_state = False

#player input
def player_choice():
    player = input('Player 1 or Player 2? Please enter 1 or 2.\n')
    move = input('Where will you make your move? Please enter a number between 1 and 9\n')
    if move == str(1):
        if ('top_left', game_values[1]) in game_board.items() or ('top_left', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['top_left'] = game_values[1]
                board()
            if player == str(2):
                game_board['top_left'] = game_values[2]
                board()
    elif move == str(2):
        if ('top_middle', game_values[1]) in game_board.items() or ('top_middle', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['top_middle'] = game_values[1]
                board()
            if player == str(2):
                game_board['top_middle'] = game_values[2]
                board()
    elif move == str(3):
        if ('top_right', game_values[1]) in game_board.items() or ('top_right', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['top_right'] = game_values[1]
                board()
            if player == str(2):
                game_board['top_right'] = game_values[2]
                board()
    elif move == str(4):
        if ('left', game_values[1]) in game_board.items() or ('left', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['left'] = game_values[1]
                board()
            if player == str(2):
                game_board['left'] = game_values[2]
                board()
    elif move == str(5):
        if ('middle', game_values[1]) in game_board.items() or ('middle', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['middle'] = game_values[1]
                board()
            if player == str(2):
                game_board['middle'] = game_values[2]
                board()
    elif move == str(6):
        if ('right', game_values[1]) in game_board.items() or ('right', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['right'] = game_values[1]
                board()
            if player == str(2):
                game_board['right'] = game_values[2]
                board()
    elif move == str(7):
        if ('bottom_left', game_values[1]) in game_board.items() or ('bottom_left', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['bottom_left'] = game_values[1]
                board()
            if player == str(2):
                game_board['bottom_left'] = game_values[2]
                board()
    elif move == str(8):
        if ('bottom_middle', game_values[1]) in game_board.items() or ('bottom_middle', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['bottom_middle'] = game_values[1]
                board()
            if player == str(2):
                game_board['bottom_middle'] = game_values[2]
                board()
    elif move == str(9):
        if ('bottom_right', game_values[1]) in game_board.items() or ('bottom_right', game_values[2]) in game_board.items():
            print('This space has already been filled. Please select another option.\n')
        else:
            if player == str(1):
                game_board['bottom_right'] = game_values[1]
                board()
            if player == str(2):
                game_board['bottom_right'] = game_values[2]
                board()


if game_state == False:
        sys.exit()

while game_state == True:
    player_choice()
    board_status()


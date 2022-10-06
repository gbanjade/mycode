#!/usr/bin/env python3
"""Himalayan Research | GBanjade
   Tic Tac Toe Game with AI"""

# Standard libraries
import random
import os
import time


# Function to clear the board
# Clears the visual display of
# previous play of the Tic Tac Toe and displays the updated board
# The new board will stack on top of each play if the clear
# function is not called first on diplay_board method

def clear():
    """ Clears the board"""
    os.system('clear')


# Displays the nicely formatted Tic Tac Toe board layout

def display_baord(board):
    """ Diplays the board"""
    clear()
    print("TIC TAC TOE with AI")
    print("-------------------\n")
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Allows human player to choose a marker
def human_marker_selection():
    """ Human marker selection function"""
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Human: Do you want to be X or O? ').upper()
    # Returns a tuples, tuples unpacking is done to identify the
    # marker for the Human  and AI
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Places the marker on the desired postion of the board
def place_marker(board, marker, position):
    """Marker position on the board"""
    board[position] = marker

# Checks if AI or Human has won
# Returns True if any of the player has won the game
def win_check(board, mark):
    """Checks for winner"""

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# Decides randomly on which player goes first
def choose_first():
    """Randomly chooses who goes first"""
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'Human'

# Checks if the board position is available, returns boolean depending on the avaibility
def space_check(board, position):
    """Checks for empty space"""
    return board[position] == ' '

# Checks the board is full and returns a boolean value
def full_board_check(board):
    """Checks all the spaces on board"""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Allows a human player to seclect a position from (1-9)
def human_choice(board):
    """Allows human to pick a position"""
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # Making sure the human gives the integer
        try:
            position = int(input(f'\nChoose position: (1-9)'))
        except ValueError:
            print("Not an integer! Try again.")
            continue

    return position

# AI will choose a position based on the coded algorithm
def ai_choice(board):
    """Allows AI to choose a position"""
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # Check for a winning position and if found, select that position
        for i in range(1, 10):
            copy_of_board = board.copy()
            if space_check(copy_of_board, i):
                place_marker(copy_of_board, AI_marker, i)
                if win_check(copy_of_board, AI_marker):
                    return i

        # Check if the human can win game on the next move
        for i in range(1, 10):
            copy_of_board = board.copy()
            if space_check(copy_of_board, i):
                place_marker(copy_of_board, human_marker, i)
                if win_check(copy_of_board, human_marker):
                    return i

        # Try to take the corners if free
        corners = [1, 3, 7, 9]
        random_corners = random.choice(corners)
        for i in corners:
            if space_check(board, random_corners):
                return random_corners

        # Try to take the center position if it's free
        if space_check(board, 5):
            return 5

        # Move on one of the remaining sidesx
        remaining_choice = [2, 4, 6, 8]
        return random.choice(remaining_choice)


# Allows to play the game again
def replay():
    """Gives option to play game again"""
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def main():
    """runtime code"""

    print("Welcome to Tic Tac Toe Game with AI\n\n")

    # While loop to keep the game running
    while True:

        # Creating a board to play a game
        the_board = [' '] * 10

        # Choosing a marker for a player
        global human_marker
        global AI_marker
        human_marker, AI_marker = human_marker_selection()

        # Determining who goes first
        turn = choose_first()
        print(f'\n{turn} will go first\n')

        play_game = input("Ready to play the game? Y or N?")

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        # Playing a game
        while game_on:
            if turn == 'Human':
                # Show the board
                display_baord(the_board)

                # Choose a position
                position = human_choice(the_board)

                # Place the marker
                place_marker(the_board, human_marker, position)

                # Checking to see if human has own
                if win_check(the_board, human_marker):
                    display_baord(the_board)
                    print(f'Congratulations! {turn}  wins!')
                    game_on = False
                else:
                    # Checking for a tie
                    if full_board_check(the_board):
                        display_baord(the_board)
                        print("TIE GAME!")
                        break
                    else:
                        turn = 'AI'
            else:
                # AI turn
                display_baord(the_board)

                # Stratigically place the AI position
                position = ai_choice(the_board)

                place_marker(the_board, AI_marker, position)
                time.sleep(1)

                # Checking to see if AI has own
                if win_check(the_board, AI_marker):
                    display_baord(the_board)
                    print(f'Congratulation! {turn} wins!!')
                    break
                else:
                    # Checking for a tie
                    if full_board_check(the_board):
                        display_baord(the_board)
                        print("TIE GAME!")
                        break
                    else:
                        turn = 'Human'

        if not replay():
            break


if __name__ == "__main__":
    main()

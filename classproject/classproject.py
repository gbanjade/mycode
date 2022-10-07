"""Himalayan Research | GBanjade
   Tic Tac Toe Game with AI"""

import random
import os
import time


def clear():
    """Clear the board after player makes a move"""
    os.system('clear')


def display_baord(board):
    """Displays nicely formatted Tic Tac Toe Board"""
    clear()
    print("TIC TAC TOE game with AI")
    print("------------------------\n\n")
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


def human__selection():
    """Allows human to choose a marker """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Human: Do you want to be X or O? \n\n').upper()
    # Returns a tuples, tuples unpacking is done to identify the
    # marker for the Human  and AI
    if marker == 'X':
        return ('X', 'O')

    return ('O', 'X')


def place_marker(board, marker, position):
    """Places the marker on the desired position of the board """
    board[position] = marker


def win_check(board, mark):
    """Checks if AI or Human has won
    Returns True if any of the player has won the game"""

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


def choose_first():
    """Decides randomly on which player goes first"""
    if random.randint(0, 1) == 0:
        return 'AI'
    return 'Human'


def space_check(board, position):
    """Checks if the position is available,
    returns boolean"""
    return board[position] == ' '


def full_board_check(board):
    """Checks if the board is full"""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def human_choice(board):
    """Allows human to select a position from (1-9)"""
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # Making sure the human gives the int
        try:
            position = int(input('\nChoose position: (1-9)'))
        except ValueError:
            print("Not an integer! Try again.")
            continue
    return position


def ai_choice(board):
    """AI will choose a position base on the algorithm"""
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # Check for a winning position and if found, select that position
        for i in range(1, 10):
            copy_of_board = board.copy()
            if space_check(copy_of_board, i):
                place_marker(copy_of_board, AI_MARKER, i)
                if win_check(copy_of_board, AI_MARKER):
                    return i

        # Check if the human can win game on the next move
        for i in range(1, 10):
            copy_of_board = board.copy()
            if space_check(copy_of_board, i):
                place_marker(copy_of_board, HUMAN_MARKER, i)
                if win_check(copy_of_board, HUMAN_MARKER):
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


def replay():
    """Gives option to play game again"""
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def main():
    """Runtime code"""
    print("Welcome to Tic Tac Toe Game with AI\n\n")

    # While loop to keep the game running
    while True:

        # Creating a board to play a game
        the_board = [' '] * 10

        # Defining global variables
        global HUMAN_MARKER
        global AI_MARKER

        # Choosing a marker for a player
        HUMAN_MARKER, AI_MARKER = human__selection()

        # Determining who goes first
        turn = choose_first()
        print(f'\n{turn} will go first\n\n')

        play_game = input("Ready to play the game? Y or N?: ")

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
                place_marker(the_board, HUMAN_MARKER, position)

                # Checking to see if human has own
                if win_check(the_board, HUMAN_MARKER):
                    display_baord(the_board)
                    print(f'Congratulations! {turn} wins!')
                    game_on = False
                else:
                    # Checking for a tie
                    if full_board_check(the_board):
                        display_baord(the_board)
                        print("TIE GAME!")
                        break
                    turn = 'AI'
            else:
                # AI turn
                display_baord(the_board)

                # Stratigically place the AI position
                position = ai_choice(the_board)

                place_marker(the_board, AI_MARKER, position)
                time.sleep(1)

                # Checking to see if AI has own
                if win_check(the_board, AI_MARKER):
                    display_baord(the_board)
                    print(f'Congratulation! {turn} wins!!')
                    break

                    # Checking for a tie
                if full_board_check(the_board):
                    display_baord(the_board)
                    print("TIE GAME!")
                    break
                turn = 'Human'

        if not replay():
            break


if __name__ == "__main__":
    main()


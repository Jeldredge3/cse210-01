"""W02_Tic-Tac-Toe_JordanEldredge"""

# Update: Created this comment in a branch to commit to the repository.

import time
import random

half_section = "- - - - - - - - - - - - -"
new_section = "-------------------------"
tab1 = "    "
tab2 = "        "

print(new_section)
print("Tic-Tac-Toe")

# Set the options for the console menu.
option_1 = "How to Play"
option_2 = "Play vs Computer"
option_3 = "Play vs Another Player"
option_0 = "Quit"
# Format and display the options for the console menu.
option_menu = f"{new_section} \n(1) {option_1} \n(2) {option_2} \n(3) {option_3} \
    \n(0) {option_0} \
    \n\nPlease Enter one of the following options."

# Global variables for the player marks.
player1_mark = "x"
player2_mark = "o"
computer_mark = "c"

def main():
    console_exit = "no"

    while console_exit != "yes":
        print(option_menu)
        user_option = input(": ")
        print(half_section)

        if user_option == "0": # Quit
            print("Exiting...\n")
            time.sleep(2.00)
            console_exit = "yes"

        elif user_option == "1": # How to Play   
            display_instructions()

        elif user_option == "2": # Player vs Random
            print("New Game: Player vs Random")
            print(new_section)
            game_start_vs_computer() 

        elif user_option == "3": # Player vs Player
            print("New Game: Player 1 vs Player 2")
            print(new_section)  
            game_start_vs_player()

        else:
            print(f"'{user_option}' is not a valid option.")

def display_instructions():
    # Displays the rules / instructions for Tic-Tac-Toe.
    print("Tic-Tac-Toe is a turn based game where each player takes turns marking an empty tile.")
    print("Once a player creates an unbroken line of 3 marks (horizontal, vertical, or diagonal), they will win the game.\n")
    print("1 | 2 | 3 ")
    print("--+---+---")
    print("4 | 5 | 6 ")
    print("--+---+---")
    print("7 | 8 | 9 ")
    print("\nThe grid for this game will be 3 rows by 3 columns.")
    print("Type in the number associated with the position to select it.")
    print("Players will be unable to mark an already marked tile.")

def game_start_vs_player():
    # Define the position values in the grid, establish the amount of empty tiles.
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tiles = []
    for position in positions:
        tiles.append(" ")

    end_game = "No"
    max_turns = len(positions)
    turn = 0

    if " " in tiles:
        pass

    # Keep game active if victory is not achieved or if there are still empty tiles.
    while end_game == "No":
        game_over = "Pending"
        win_location = "N/A"
        self_count = 0
        opponent_count = 0
        empty_count = 0
        victor = "Draw"

        # Only proceeds if game is active.
        if end_game == "No":
            turn += 1
            print(half_section)
            print(f"Player 1 - Turn {turn}/{max_turns}\n")
            # Display the grid.
            display_grid(positions, tiles)
            # Player-x's turn.
            player_turn(positions, tiles, player1_mark)
            # Check grid for any lines of 3 using the check_grid() function.
            check_results = check_grid(positions, tiles, player1_mark)
            game_over = check_results[0]
            if game_over == "Yes": # If the check_grid() function found a line of 3, end the game.
                victor = "Player 1"
                victor_mark = player1_mark
                win_location = check_results[1]
                end_game = "Yes"
            if " " in tiles: # Check for remaining empty tiles.
                pass
            else: # End the game if no empty tiles remain.
                end_game = "Yes"

        # Only proceeds if game is active.
        if end_game == "No":
            turn += 1
            print(half_section)
            print(f"Player 2 - Turn {turn}/{max_turns}\n")
            # Update the grid.
            display_grid(positions, tiles)
            # Player-o's turn.
            player_turn(positions, tiles, player2_mark)
            # Check grid for any lines of 3 using the check_grid() function.
            check_results = check_grid(positions, tiles, player2_mark)
            game_over = check_results[0]
            if game_over == "Yes": # If the check_grid() function found a line of 3, end the game.
                victor = "Player 2"
                victor_mark = player2_mark
                win_location = check_results[1]
                end_game = "Yes"
            if " " in tiles: # Check for remaining empty tiles.
                pass
            else: # End the game if no empty tiles remain.
                end_game = "Yes"

        if end_game == "Yes":
            print(new_section)
            print("Final Results:\n")
            # Display the updated grid.
            display_grid(positions, tiles)
            check_results = check_grid(positions, tiles, player2_mark)
            # CHECK RESULTS INDEX: [0] game_over, [1] win_location, [2] player1_counter, [3] player2_counter, [4] empty_counter
            time.sleep(1.00)
            if victor != "Draw": 
                print(f"\n{victor} Wins!")
                print(f"Connected 3 '{victor_mark}'s on {win_location}.")
            else:
                print("\nGame ends in a Draw.")
            
def game_start_vs_computer():
    # Define the position values in the grid, establish the amount of empty tiles.
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tiles = []
    for position in positions:
        tiles.append(" ")

    end_game = "No"
    max_turns = len(positions)
    turn = 0

    if " " in tiles:
        pass

    # Keep game active if victory is not achieved or if there are still empty tiles.
    while end_game == "No":
        game_over = "Pending"
        win_location = "N/A"
        self_count = 0
        opponent_count = 0
        empty_count = 0
        victor = "Draw"

        # Only proceeds if game is active.
        if end_game == "No":
            turn += 1
            print(half_section)
            print(f"Player - Turn {turn}/{max_turns}\n")
            # Display the grid.
            display_grid(positions, tiles)
            # Player-x's turn.
            player_turn(positions, tiles, player1_mark)
            # Check grid for any lines of 3 using the check_grid() function.
            check_results = check_grid(positions, tiles, player1_mark)
            game_over = check_results[0]
            if game_over == "Yes": # If the check_grid() function found a line of 3, end the game.
                victor = "Player"
                victor_mark = player1_mark
                win_location = check_results[1]
                end_game = "Yes"
            if " " in tiles: # Check for remaining empty tiles.
                pass
            else: # End the game if no empty tiles remain.
                end_game = "Yes"

        # Only proceeds if game is active.
        if end_game == "No":
            turn += 1
            print(half_section)
            print(f"Computer - Turn {turn}/{max_turns}\n")
            # Update the grid.
            display_grid(positions, tiles)
            # Player-o's turn.
            computer_turn(positions, tiles, computer_mark)
            # Check grid for any lines of 3 using the check_grid() function.
            check_results = check_grid(positions, tiles, computer_mark)
            game_over = check_results[0]
            if game_over == "Yes": # If the check_grid() function found a line of 3, end the game.
                victor = "Computer"
                victor_mark = computer_mark
                win_location = check_results[1]
                end_game = "Yes"
            if " " in tiles: # Check for remaining empty tiles.
                pass
            else: # End the game if no empty tiles remain.
                end_game = "Yes"

        if end_game == "Yes":
            print(new_section)
            print("Final Results:\n")
            # Display the updated grid.
            display_grid(positions, tiles)
            check_results = check_grid(positions, tiles, player2_mark)
            # CHECK RESULTS INDEX: [0] game_over, [1] win_location, [2] player1_counter, [3] player2_counter, [4] empty_counter
            time.sleep(1.00)
            if victor != "Draw": 
                print(f"\n{victor} Wins!")
                print(f"Connected 3 '{victor_mark}'s on {win_location}.")
            else:
                print("\nGame ends in a Draw.")
            


def display_grid(pos, tiles):
    """ Takes 2 parameters:
        Position (pos) - absolute, allows the player to type the number of the corresponding area.
        Tiles - variable, enables the positions to be marked or empty."""
    # 1 | 2 | 3 
    # --+---+---
    # 4 | 5 | 6
    # --+---+---
    # 7 | 8 | 9
    print(f"{tab2}{tiles[0]} | {tiles[1]} | {tiles[2]}  ")
    print(f"{tab2}--+---+---")
    print(f"{tab2}{tiles[3]} | {tiles[4]} | {tiles[5]}  ")
    print(f"{tab2}--+---+---")
    print(f"{tab2}{tiles[6]} | {tiles[7]} | {tiles[8]}  ")

def player_turn(positions, tiles, mark):
    # Check if the player move is acceptable, return the position selected.
    turn_exit = "no"
    while turn_exit != "yes":
        print("\nType in a tile's number to mark the position.")
        player_move = int(input(": "))
        p_index = player_move - 1
        max_index = len(positions) - 1
        if p_index == -1: # Return to menu if user enters 0.
            print("Pass.")
            turn_exit = "yes"
        elif p_index < -1 or p_index > max_index: # Index is below the minimum amount of 0.
            print(half_section)
            print(f"'{player_move}' is not a valid option.\n")
            print("Enter a number between 1-9. Tile sequence goes left to right, top to bottom.")
            display_grid(positions, tiles)
        else:
            if tiles[p_index] == " ":
                tiles[p_index] = mark
                turn_exit = "yes"
            else:
                print(half_section)
                print(f"unable to move. Position '{p_index + 1}' is taken.\n")
                display_grid(positions, tiles)

def computer_turn(positions, tiles, mark):
    print("\nComputer's turn...")
    time.sleep(1.00)
    # Check if the computer move is acceptable, return the position selected.
    max_index = len(positions)
    turn_exit = "no"
    while turn_exit != "yes":
        c_index = random.choice(range(0, max_index))
        computer_move = c_index + 1
        if tiles[c_index] == " ":
            # Computer can mark the position.
            tiles[c_index] = mark
            print(f"Computer marks position '{computer_move}' with '{mark}'.")
            time.sleep(1.00)
            turn_exit = "yes"
        else:
            # Computer cannot mark tile as it was previously marked.
            pass

    while turn_exit != "yes":
        print("\nType in a tile's number to mark the position.")
        player_move = int(input(": "))
        p_index = player_move - 1
        max_index = len(positions) - 1
        if p_index == -1: # Return to menu if user enters 0.
            print("Pass.")
            turn_exit = "yes"
        elif p_index < -1 or p_index > max_index: # Index is below the minimum amount of 0.
            print(half_section)
            print(f"'{player_move}' is not a valid option.\n")
            print("Enter a number between 1-9. Tile sequence goes left to right, top to bottom.")
            display_grid(positions, tiles)
        else:
            if tiles[p_index] == " ":
                tiles[p_index] = mark
                turn_exit = "yes"
            else:
                print(half_section)
                print(f"unable to move. Position '{p_index + 1}' is taken.\n")
                display_grid(positions, tiles)

def check_grid(pos, tiles, mark):
    """ Checks the grid each marked and unmarked tile. Any unbroken row of the same mark will result in victory. 
    If all tiles are marked and there is no unbroken row, game will result in a tie.
    Returns the results from the tile checking in the form of a string."""
    empty_counter = 0
    player1_counter = 0
    player2_counter = 0
    game_over = "No"
    win_location = "N/A"

    # Count the number of marked and unmarked tiles.
    for tile in tiles:
        if tile == " ":
            empty_counter += 1
        elif tile == player1_mark:
            player1_counter += 1
        elif tile == player2_mark:
            player2_counter += 1

    # INDEX REFERENCE CHART
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8

    """ Check all posibilities for Player Victory """
    # Check for row lines of 3.
    if tiles[0] == mark and tiles[1] == mark and tiles[2] == mark:
        game_over = "Yes"
        win_location = "row 1"
    elif tiles[3] == mark and tiles[4] == mark and tiles[5] == mark:
        game_over = "Yes"
        win_location = "row 2"
    elif tiles[6] == mark and tiles[7] == mark and tiles[8] == mark:
        game_over = "Yes"
        win_location = "row 3"
    # Check for column lines of 3.
    elif tiles[0] == mark and tiles[3] == mark and tiles[6] == mark:
        game_over = "Yes"
        win_location = "column 1"
    elif tiles[1] == mark and tiles[4] == mark and tiles[7] == mark:
        game_over = "Yes"
        win_location = "column 2"
    elif tiles[2] == mark and tiles[5] == mark and tiles[8] == mark:
        game_over = "Yes"
        win_location = "column 3"
    # Check for diagonal lines of 3.
    elif tiles[0] == mark and tiles[4] == mark and tiles[8] == mark:
        game_over = "Yes"
        win_location = "diagonal left-to-right"
    elif tiles[2] == mark and tiles[4] == mark and tiles[6] == mark:
        game_over = "Yes"
        win_location = "diagonal right-to-left"

    # Return the results of the check: If the game was won, what line won the game, player's marks, opponent's marks, and empty tiles.
    return game_over, win_location, player1_counter, player2_counter, empty_counter

# Call main to start this program.
if __name__ == "__main__":
    main()
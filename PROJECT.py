import json

class TicTacToe:
    def __init__(self):
        # Initialize the game board and set the starting player
        self.board = [str(i) for i in range(1, 10)]  # Board positions from 1 to 9
        self.current_player = 'X'  # Player 'X' starts first
        self.player_names = {'X': 'Player 1', 'O': 'Player 2'}  # Default player names
        self.game_state_file = 'game_state.txt'  # File to save the game state
        self.game_active = True  # Flag to track if the game is ongoing

    def print_board(self):
        # Display the current state of the board
        print("\nCurrent Board:")
        print(" | ".join(self.board[0:3]))  # First row
        print("---+---+---")  # Row separator
        print(" | ".join(self.board[3:6]))  # Second row
        print("---+---+---")  # Row separator
        print(" | ".join(self.board[6:9]))  # Third row

    def switch_player(self):
        # Switch the current player between 'X' and 'O'
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check if the current player has won
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for combo in winning_combinations:
            # If all three positions in a combination are the same
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return True  # A winner is found
        return False  # No winner yet

    def is_draw(self):
        # Check if the game is a draw (no empty spaces left)
        return all(cell in ['X', 'O'] for cell in self.board)

    def save_game_state(self):
        # Save the current game state to a file
        game_state = {
            'board': self.board,  # Current board state
            'current_player': self.current_player  # Current player's turn
        }
        with open(self.game_state_file, 'w') as file:
            json.dump(game_state, file)  # Write game state to file
        print("Game state saved!")
        print(f"(Current board and player turn recorded in {self.game_state_file})")

    def reset_game(self):
        # Reset the game to its initial state
        self.board = [str(i) for i in range(1, 10)]  # Reset board positions
        self.current_player = 'X'  # Reset starting player
        self.game_active = True  # Set game to active

    def get_player_names(self):
        # Get player names from input
        self.player_names['X'] = input("Enter name for Player 1 (X): ")
        self.player_names['O'] = input("Enter name for Player 2 (O): ")

    def play(self):
        # Main game loop
        self.get_player_names()  # Get player names before starting
        print("Welcome to Tic Tac Toe!")

        while self.game_active:
            self.print_board()  # Display the current board
            move = input(f"{self.player_names[self.current_player]}, enter your move (1-9): ")

            # Validate the move
            if move.isdigit() and int(move) in range(1, 10):
                move = int(move) - 1  # Convert to zero-based index
                if self.board[move] not in ['X', 'O']:  # Check if the position is free
                    self.board[move] = self.current_player  # Place the current player's mark
                    if self.check_winner():
                        self.print_board()  # Show the board
                        print(f"{self.player_names[self.current_player]} wins!")  # Announce the winner
                        self.save_game_state()  # Save game state after winning
                        self.game_active = False  # End the game
                    elif self.is_draw():
                        self.print_board()  # Show the board
                        print("It's a draw!")  # Announce the draw
                        self.save_game_state()  # Save game state after draw
                        self.game_active = False  # End the game
                    else:
                        self.switch_player()  # Switch to the other player
                else:
                    print("Invalid move! That position is already taken. Try again.")  # Handle invalid move
            else:
                print("Invalid input! Please enter a number between 1-9.")  # Handle invalid input

        # Prompt to play again after the game ends
        if input("Would you like to play again? (yes/no): ").lower() == 'yes':
            self.reset_game()  # Reset the game
            self.play()  # Start a new game

if __name__ == "__main__":
    game = TicTacToe()  # Create a new game instance
    game.play()  # Start the game

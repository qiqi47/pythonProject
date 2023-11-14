# Required class:
# OwnBoard: Define own board
# Properties and Methods
# ShipList: property that stores the location of ship, and its condition (safe or hit)
# HitList: property that stores the location of enemy bombardment, and the condition (hit or miss)
# Add: method that add ship to the board
# Evaluate: method that checks if the opponent’s bombardment hit or failed, reflect the condition to ShipList and HitList
# ShowOwn: Show visualization of ShipList of its own.
# ShowOpponent: Show HitList of the opponent.
# 'X' for placing and hit battleship
# ' ' for empty space
# '-' for missed shot

class Board:
    def __init__(self):
        # This initialize board state and shiplist for each instance.
        self.state = [['']*10 for x in range(10)]
        self.shipList = {}

    def add_ship(self, length, coordination, direction):
        """Add a ship to the board according to the coordination and direction.
        Throw an error if it is out of bound."""
        # Implement the logic to add a ship to the board.

    def evaluate(self, coordination):
        """Check if the bomb hit or failed, and reflect the condition to shipList."""
        # Implement the logic to check if the opponent's bombardment hit or failed.

    def show_result(self):
        """Show visualization of shipList of its own."""
        # Implement the logic to display the shipList in a grid.


own_board = Board()
own_board.add_ship(4, "1A", "right")
own_board.show_result()

# Get the name of the players
player1_name = input("Player 1 Name: ")
player2_name = input("Player 2 Name: ")

# Create player boards
player1_board = Board()
player2_board = Board()

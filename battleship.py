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

own_board = OwnBoard()
own_board.add_ship(4, "1A", "right")
own_board.show_own()

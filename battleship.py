class Board:
    def __init__(self):
        # This initialize board state and shiplist for each instance.
        self.state = [[' ']*10 for x in range(10)]
        self.shipList = {"battleship": ['', '', '', '', ''],
                         "cruiser1": ['', '', ''],
                         "cruiser2": ['', '', ''],
                         "destroyer1": ['', ''],
                         "destroyer2": ['', ''],
                         }

    def coord_to_index(self, coordination):
        # Convert coordinate string to row and column indices.
        col = ord(coordination[1]) - ord('A')
        row = int(coordination[0]) - 1
        return row, col

    def add_ship(self, length, coordination, direction):
        """Add a ship to the board according to the coordination and direction.
        Throw an error if it is out of bound."""
        # Implement the logic to add a ship to the board.
        row, col = self.coord_to_index(coordination)
        if direction.lower() == 'horizontal':  # if the ship is horizontal
            if col + length > 10:   # to judge if it is out of bound
                raise ValueError("Ship out of bounds")
            for i in range(length):
                if self.state[row][col + i] == 'X':  # to judge if it is overlap
                    raise ValueError("Ships cannot overlap")
                self.state[row][col + i] = 'X'  # to note the position
                # to note the ship is hit or not

                """I will construct this part in the main body, so the coordination of
                each ship will be recorded in self.shipList"""
                # self.shipList[(row, col + i)] = 'safe'

        elif direction.lower() == 'vertical':  # if the ship is vertical
            if row + length > 10:
                raise ValueError("Ship out of bounds")
            for i in range(length):
                if self.state[row + i][col] == 'X':
                    raise ValueError("Ships cannot overlap")
                self.state[row + i][col] = 'X'

                # same as above
                # self.shipList[(row + i, col)] = 'safe'
        else:
            raise ValueError("Invalid direction")
        return

    def evaluate(self, coordination):
        """Check if the bomb hit or failed, and reflect the condition to shipList. 
        Intact ship is "X" and Intact """
        # Implement the logic to check if the opponent's bombardment hit or failed.
        row, col = self.coord_to_index(coordination)

        if self.state[row][col] == "@" or self.state[row][col] == "V":
            raise ValueError("You can't bomb same place again")

        elif self.state[row][col] == "X":
            # Mark as hit with "@"
            self.state[row][col] = "@"

            # Record hit in shipList
            for list in self.shipList.values():
                """check each list and remove hit coordination. 
                Only empty list will remain if all part of a ship is hit."""
                if coordination in list:
                    list.remove(coordination)

            return 'hit'

        else:
            # Mark the cell with "V" as miss. "V" because it looks like water splash.
            self.state[row][col] = "V"
            return 'miss'

        # if (row, col) in self.shipList:
            # self.shipList[(row, col)] = 'hit'
            # return 'hit'
        # else:
            # return 'miss'

    def sink_Evaluation(self):
        # check each ship of shipList dictionary
        for ship in self.shipList:
            # If the list is empty after attack, that means the ship sunk.
            if list.value == []:
                print(f'{list.key} sunk.')
                # Delete sunk ship from the shipList
                del self.shipList[list.key]
                break
        return

    def own_Condition(self):
        """This method visualizes location of your ships and their conditions. Hit is
        '@', and miss is 'V'. """

        board_map = "  A B C D E F G H I J\n"
        # Double for loop, but limited to 100 checks. No issue.
        for i in range(10):
            row = ""
            for j in range(10):
                # Copy location of ship not bombed
                if self.state[i][j] == "X":
                    row += "X"
                # Copy location of ship hit
                elif self.state[i][j] == "@":
                    row += "@"
                else:
                    row += ' '
            # Adding row number, separator and append to board_map
            board_map += str(i+1) + "|" + "|".join(row) + "|\n"

        print(board_map)
        return

    def opponent_Condition(self):
        """This method visualizes location of your hit / not hit"""

        board_map = "  A B C D E F G H I J\n"
        for i in range(10):
            row = ""
            for j in range(10):
                if self.state[i][j] == "@":
                    row += "@"
                elif self.state[i][j] == "V":
                    row += "V"
                else:
                    row += ' '
            # Adding row number, separator and append to board_map
            board_map += str(i+1) + "|" + "|".join(row) + "|\n"

        print(board_map)
        return


own_board = Board()
own_board.add_ship(4, "1A", "right")
own_board.show_result()

# Get the name of the players
player1_name = input("Player 1 Name: ")
player2_name = input("Player 2 Name: ")

# Create player boards
player1_board = Board()
player2_board = Board()

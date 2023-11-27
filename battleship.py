import os


class Board:
    def __init__(self):
        # This initialize board state and shipList for each instance.
        self.state = [[' ']*10 for x in range(10)]
        self.shipList = {"battleship": ['', '', '', '', ''],
                         "cruiser1": ['', '', ''],
                         "cruiser2": ['', '', ''],
                         "destroyer1": ['', ''],
                         "destroyer2": ['', ''],
                         }
        # Keep track of number of ship on board
        self.shipNum = 0

    def coord_to_index(self, coordination):
        # Convert coordinate string to row and column indices.
        # Check the length of the coordination input.
        if len(coordination) != 2:
            raise ValueError(
                "Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        # Check if input falls in 1-9, A-J limit.
        elif int(ord(coordination[1])) < 65 or int(ord(coordination[1])) > 74 or int(coordination[0]) < 1 or int(coordination[0]) > 10:
            raise ValueError(
                "Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        else:
            col = ord(coordination[1]) - ord('A')
            row = int(coordination[0]) - 1
            return row, col

    # Added parameter "name" to send info to shipList
    def add_ship(self, name, length, coordination, direction):
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
                self.state[row][col + i] = 'X'

                # Adding coordination information to shipList in each iteration.
                self.shipList[name][i] = (str(row+1) + str(chr(col + i)))

        elif direction.lower() == 'vertical':  # if the ship is vertical
            if row + length > 10:
                raise ValueError("Ship out of bounds")
            for i in range(length):
                if self.state[row + i][col] == 'X':
                    raise ValueError("Ships cannot overlap")
                self.state[row + i][col] = 'X'
                # Adding coordination information to shipList in each iteration.
                self.shipList[name][i] = (str(row + 1 + i) + str(chr(col)))
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
        for ship_key, ship_value in self.shipList.items():
            # If the list is empty after attack, that means the ship sunk.
            if ship_value == []:
                print(f'{ship_key} sunk.')
                # Delete sunk ship from the shipList
                del self.shipList[ship_key]
                break
        return

    def own_Condition(self):
        """This method visualizes location of your ships and their conditions. Hit is
        '@', and miss is 'V'. """

        board_map = "   A B C D E F G H I J\n"
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
            if i+1 < 10:
                board_map += str(i+1) + " |" + "|".join(row) + "|\n"
            else:
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

            if i+1 < 10:
                board_map += str(i+1) + " |" + "|".join(row) + "|\n"
            else:
                board_map += str(i+1) + "|" + "|".join(row) + "|\n"

        print(board_map)
        return

    def bomb_ship(self, opponent_board):
        """Take input from the player for bombing and update the board."""
        while True:
            try:
                coord = input("Enter coordinates to bomb (e.g., 1A): ")
                result = opponent_board.evaluate(coord)
                print(result)

                if result == 'hit':
                    self.sink_Evaluation()

                opponent_board.opponent_Condition()
                break
            except ValueError as msg:
                print(msg)


# Get the name of the players
player1_name = input("Player 1 Name: ")
player2_name = input("Player 2 Name: ")

# Create player boards
player1_board = Board()
player2_board = Board()

print(f'{player1_name}\'s turn. Hand device to {player1_name}.')

# Create flags
player1_set = False
player2_set = False

while player1_set == False:
    shipName = list(player1_board.shipList)[player1_board.shipNum]
    shipLength = len(player1_board.shipList[shipName])

    print(f'\nPlace your {shipName}. Length is {shipLength}.\n')

    loc = input(
        f'''Input the coordination for the left edge of your {shipName}.\nCoordination should be a combination of a number from 1-10 and an alphabet from A-J (Ex. 1A).\n''')
    direction = input(
        'Input which direction you would like to stretch your ship (option: vertical or horizontal).\n')

    try:
        player1_board.add_ship(shipName, shipLength, loc, direction)
        print(f'\n{shipName} successfully added.\n')
        print("Following is the current condition of your map:\n")

        player1_board.own_Condition()

        player1_board.shipNum += 1

        if player1_board.shipNum == 5:
            player1_set = True

    except ValueError as msg:
        print(msg)

input(f'{player1_name} completed the setting. Press enter to clear screen and hand the terminal to {player2_name}.')

# Clear screen. Should work well in terminal (not tested yet). Another idea is to print multiple empty lines.
os.system('clear')

while player2_set == False:
    shipName = list(player2_board.shipList)[player2_board.shipNum]
    shipLength = len(player2_board.shipList[shipName])

    print(f'\nPlace your {shipName}. Length is {shipLength}.\n')

    loc = input(
        f'''Input the coordination for the left edge of your {shipName}.\nCoordination should be a combination of a number from 1-10 and an alphabet from A-J (Ex. 1A).\n''')
    direction = input(
        'Input which direction you would like to stretch your ship (option: vertical or horizontal).\n')

    try:
        player2_board.add_ship(shipName, shipLength, loc, direction)
        print(f'\n{shipName} successfully added.\n')
        print("Following is the current condition of your map:\n")

        player2_board.own_Condition()

        player2_board.shipNum += 1

        if player2_board.shipNum == 5:
            player2_set = True

    except ValueError as msg:
        print(msg)

while True:
    print(f"{player1_name}'s turn.")
    player1_board.bomb_ship(player2_board)

    # Check if player 1 has won
    if not player2_board.shipList:
        print(f"{player1_name} has bombed all the ships. {player1_name} wins!")
        break

    input("Press enter to clear the screen and hand the terminal to Player 2.")
    os.system('clear')

    print(f"{player2_name}'s turn.")
    player2_board.bomb_ship(player1_board)

    # Check if player 2 has won
    if not player1_board.shipList:
        print(f"{player2_name} has bombed all the ships. {player2_name} wins!")
        break

    input("Press enter to clear the screen and hand the terminal to Player 1.")
    os.system('clear')

import os


class Board:
    def __init__(self):
        """This initialize board state and shipList for each instance."""
        self.state = [[' ']*10 for x in range(10)]
        self.shipList = {"destroyer1": ['', ''], "destroyer2": ['', '']}
        # Keep track of number of ship on board
        self.shipNum = 0

    def coord_to_index(self, command):
        """Convert coordinate string to row and column indices. For placing ship purpose"""
        # Check the length of the coordination input.
        if len(command) < 3 or len(command) > 4:
            raise ValueError(
                "Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J + direction flag (v or h).")
        coordination = command[:-1]
        flag = command[-1]

        if flag != "v" and flag != "h":
            raise ValueError("Invalid direction flag. Should be v or h.")
        # Check if input falls in 1-9, A-J limit.
        if int(ord(coordination[-1])) < 65 or int(ord(coordination[-1])) > 74 or int(coordination[:-1]) < 1 or int(coordination[:-1]) > 10:
            raise ValueError(
                "Invalid coordination. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        else:
            col = ord(coordination[-1]) - ord('A')
            row = int(coordination[:-1]) - 1
            return row, col, flag

    def bomb_coord_to_index(self, coordination):
        """Convert coordinate string to row and column indices. For bombing purpose"""
        # Check the length of the coordination input.
        if len(coordination) < 2 or len(coordination) > 3:
            raise ValueError(
                "Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        if int(ord(coordination[-1])) < 65 or int(ord(coordination[-1])) > 74 or int(coordination[:-1]) < 1 or int(coordination[:-1]) > 10:
            raise ValueError(
                "Invalid coordination. Should be a combination of a number from 1-10 and an alphabet from A-J.jg")
        else:
            col = ord(coordination[-1]) - ord('A')
            row = int(coordination[:-1]) - 1
            return row, col

    # Added parameter "name" to send info to shipList
    def add_ship(self, name, shipLength, command):
        """Add a ship to the board according to the coordination and direction.
        Throw an error if it is out of bound."""
        # Implement the logic to add a ship to the board.
        row, col, flag = self.coord_to_index(command)
        if flag == 'h':  # if the ship is horizontal
            if col + shipLength > 10:   # to judge if it is out of bound
                raise ValueError("Ship out of bounds")
            for i in range(shipLength):
                if self.state[row][col + i] == 'X':  # to judge if it is overlap
                    raise ValueError("Ships cannot overlap")
            # If no overlap, add the ship to the board
            for i in range(shipLength):
                self.state[row][col + i] = 'X'
                self.shipList[name][i] = (str(row+1) + chr(col + 65 + i))

        elif flag == 'v':  # if the ship is vertical
            if row + shipLength > 10:
                raise ValueError("Ship out of bounds")
            for i in range(shipLength):
                if self.state[row + i][col] == 'X':
                    raise ValueError("Ships cannot overlap")
             # If no overlap, add the ship to the board
            for i in range(shipLength):
                self.state[row + i][col] = 'X'
                self.shipList[name][i] = (str(row+i+1) + chr(col + 65))

        return

    def evaluate(self, coordination):
        """Check if the bomb hit or failed, and reflect the condition to shipList. 
        Intact ship is "X" and Intact """
        # Implement the logic to check if the opponent's bombardment hit or failed.
        row, col = self.bomb_coord_to_index(coordination)

        if self.state[row][col] == "@" or self.state[row][col] == "V":
            raise ValueError("You can't bomb same place again")

        elif self.state[row][col] == "X":
            # Mark as hit with "@"
            self.state[row][col] = "@"

            # Record hit in shipList
            for location in self.shipList.values():
                #check each list and remove hit coordination. Only empty list will remain if all part of a ship is hit.
                if coordination in location:
                    location.remove(coordination)
            return 'hit!!\n'

        else:
            # Mark the cell with "V" as miss. "V" because it looks like water splash.
            self.state[row][col] = "V"
            return 'miss...\n'

    def sink_Evaluation(self):
        """This evaluates if certain ship in shipList is sunk."""
        # check each ship of shipList dictionary
        for ship_key, ship_value in self.shipList.items():
            # If the list is empty after attack, that means the ship sunk.
            if ship_value == []:
                print(
                    f'Opponent {ship_key} sunk. Inform the opponent about it.\n')
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
                # show the location of ship opponent hit
                elif self.state[i][j] == "@":
                    row += "@"
                # show the location of ship opponent missed
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

    def bomb_Dashboard(self, opponent_board):
        """This method visualizes location of your hit / not hit"""
        board_map = "Opponent's map           Own map \n   A B C D E F G H I J      A B C D E F G H I J\n"
        for i in range(10):
            row = ""
            for j in range(21):
                if j < 10:
                    # Copy location of ship not bombed
                    if opponent_board.state[i][j] == "@":
                        row += "@"
                    elif opponent_board.state[i][j] == "V":
                        row += "V"
                    else:
                        row += ' '

                elif j == 10:
                    if i+1 < 10:
                        row = str(i+1) + " |" + "|".join(row) + \
                            "|  " + str(i+1) + " |"
                    else:
                        row = str(i+1) + "|" + "|".join(row) + \
                            "|  " + str(i+1) + "|"
                else:
                    # Copy location of ship not bombed
                    if self.state[i][j-11] == "X":
                        row += "X|"
                    elif self.state[i][j-11] == "@":
                        row += "@|"
                    elif self.state[i][j-11] == "V":
                        row += "V|"
                    else:
                        row += ' |'

            board_map += row + "\n"

        print(board_map)

    def bomb_ship(self, opponent_board):
        """Take input from the player for bombing and update the board."""
        while True:
            try:
                self.bomb_Dashboard(opponent_board)
                coord = input("Enter coordinates to bomb (e.g., 1A): ")
                result = opponent_board.evaluate(coord)
                print(result)

                if result == 'hit':
                    self.sink_Evaluation()
                self.bomb_Dashboard(opponent_board)

                break
            except ValueError as msg:
                print(msg)
 
#Global function to clear screen. Work on both Mac and PC                
def cls():
    os.system("cls" if os.name == "nt" else "clear")


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

    try:
        # Display the current state of the board before adding the ship
        player1_board.own_Condition()
        command = input(
            f'''Input the coordination and direction flag for the left edge of your {shipName}.\nCoordination should be a combination of a number from 1-10 and an alphabet from A-J (Ex. 1A).\nDirection flag states if the ship is placed vertical (v) or horizontal (h).\nInput should be like "1Av".\n''')

        # Now call add_ship after validation
        player1_board.add_ship(shipName, shipLength, command)
        print(f'\n{shipName} successfully added.\n')
        print("Following is the current condition of your map:\n")

        player1_board.own_Condition()
        player1_board.shipNum += 1

        if player1_board.shipNum == 2:
            player1_set = True

    except ValueError as msg:
        print(msg)

input(f'{player1_name} completed the setting. Press enter to clear screen and hand the terminal to {player2_name}.')

# Clear screen.
cls()

while player2_set == False:
    shipName = list(player2_board.shipList)[player2_board.shipNum]
    shipLength = len(player2_board.shipList[shipName])

    print(f'\nPlace your {shipName}. Length is {shipLength}.\n')

    try:
     # Display the current state of the board before adding the ship
        player2_board.own_Condition()
        command = input(
            f'''Input the coordination and direction flag for the left edge of your {shipName}.\nCoordination should be a combination of a number from 1-10 and an alphabet from A-J (Ex. 1A).\nDirection flag states if the ship is placed vertical (v) or horizontal (h).\nInput should be like "1Av".\n''')

        player2_board.add_ship(shipName, shipLength, command)
        print(f'\n{shipName} successfully added.\n')
        print("Following is the current condition of your map:\n")

        player2_board.own_Condition()
        player2_board.shipNum += 1

        if player2_board.shipNum == 2:
            player2_set = True

    except ValueError as msg:
        print(msg)
        
input(f'{player2_name} completed the setting. Press enter to clear screen and hand the terminal to {player1_name}.')

# Clear screen. 
cls()

print("Let's start the game!")

while True:
    print(f"{player1_name}'s turn.")
    player1_board.bomb_ship(player2_board)
    player2_board.sink_Evaluation()

    # Check if player 1 has won
    if not player2_board.shipList:
        print(f"{player1_name} has bombed all the ships. {player1_name} wins!")
        break

    input("Press enter to clear the screen and hand the terminal to Player 2.")
    cls()

    print(f"{player2_name}'s turn.")
    player2_board.bomb_ship(player1_board)
    player1_board.sink_Evaluation()

    # Check if player 2 has won
    if not player1_board.shipList:
        print(f"{player2_name} has bombed all the ships. {player2_name} wins!")
        break

    input("Press enter to clear the screen and hand the terminal to Player 1.")
    
    cls()
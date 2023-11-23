class Board:
    def __init__(self):
        # This initialize board state and shipList for each instance.
        self.state = [[' ']*10 for x in range(10)]
        self.shipList = {"battleship":['','','','',''],
                         "cruiser1":['','',''],
                         "cruiser2":['','',''],
                         "destroyer1":['',''],
                         "destroyer2":['',''],
                        }
        #Keep track of number of ship on board
        self.shipNum = 0

    def coord_to_index(self, coordination):
        # Convert coordinate string to row and column indices.
        #Check the length of the coordination input.
        if len(coordination) != 2:
            raise ValueError("Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        elif coordination[1] < 65 or coordination[1] > 74 or int(coordination[0]) < 1 or int(coordination[0]) > 10:
            raise ValueError("Invalid input. Should be a combination of a number from 1-10 and an alphabet from A-J.")
        else:
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
                #self.shipList[(row, col + i)] = 'safe'

        elif direction.lower() == 'vertical':  # if the ship is vertical
            if row + length > 10:
                raise ValueError("Ship out of bounds")
            for i in range(length):
                if self.state[row + i][col] == 'X':
                    raise ValueError("Ships cannot overlap")
                self.state[row + i][col] = 'X'
                #same as above
                #self.shipList[(row + i, col)] = 'safe'
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
            #Mark as hit with "@"
            self.state[row][col] = "@"
            
            #Record hit in shipList
            for list in self.shipList.values():
                """check each list and remove hit coordination. 
                Only empty list will remain if all part of a ship is hit."""
                if coordination in list:
                    list.remove(coordination)
                 
            return 'hit'
            
        else:
            #Mark the cell with "V" as miss. "V" because it looks like water splash.
            self.state[row][col] = "V"
            return 'miss'      
        
        #if (row, col) in self.shipList:
            #self.shipList[(row, col)] = 'hit'
            #return 'hit'
        #else:
            #return 'miss'
            
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
        
        board_map = "  A B C D E F G H I J\n"
        #Double for loop, but limited to 100 checks. No issue. 
        for i in range(10):
            row = ""
            for j in range(10):
                #Copy location of ship not bombed
                if self.state[i][j] == "X":
                    row += "X"
                #Copy location of ship hit
                elif self.state[i][j] == "@":
                    row += "@"
                else:
                    row += ' '
            #Adding row number, separator and append to board_map
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
            #Adding row number, separator and append to board_map
            board_map += str(i+1) + "|" + "|".join(row) + "|\n"
        
        print(board_map)
        return

# Get the name of the players
player1_name = input("Player 1 Name: ")
player2_name = input("Player 2 Name: ")

# Create player boards
player1_board = Board()
player2_board = Board()

print(f'{player1_name}s turn. Hand device to {player1_name}.')

#Create flags
player1_set = False
player2_set = False

while player1_set == False:
    status1 = input(f'''{player1_name}'s turn. Type in one of following commands:
                            set = Set your ship. You have 5 ships.
                            view = view the current status of your map. \"X\" is the location of your ship.''')
    
    if status1.lower == "set":
        shipName = player1_board.shipList[player1_board.shipNum].key
        shipLength = player1_board.shipList[player1_board.shipNum].value
        print(f'Place your {shipName}. Length is {shipLength}.')
        loc = input(f'''Input the coordination for the left edge of your {shipName}.
                        Coordination should be a combination of a number from 1-10 and an alphabet from A-J (Ex. 1A).''')
        direction = input(f'Input which direction you would like to stretch your ship (option: vertical or horizontal).')
        
        try:
            player1_board.add_ship(shipLength,loc,direction)
            print(f'{shipName} successfully added.')
            player1_board.shipNum += 1
            
        except ValueError as msg:
            print(msg)
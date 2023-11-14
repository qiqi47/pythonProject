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
        #This initialize board state and shiplist for each instance.
        self.state = [['']*10 for x in range(10)] 
        self.shipList = [[]*5 for x in range(5)] 
        #Originally there should be 5 ships. Those lists will keep the coordination of each ship and delete coordination 
        #when the place is bombed. When the list turned empty, the ship is considered to be sunk.

    def add(self,length of the ship, coordination,direction):
        """This method add ship to the board according to the coordination. Length of the ship will be 4, 3(x2), 2(x2),1.
        Player can select one coordination (like 1A), and then can select which way to extend the ship. For example, if
        the player select "right" for a ship of length 3, coordination will be 1A,1B,1C. Should throw an error if it is 
        out of bound."""

    def showShipLocation(self):
        """This method get infromation from board, and shows where the ships are located, and it's condition (hit or not). 
        This requires some work, because we don't want to print the board state in a form of a list. Rather, it should 
        show in form of grid.

    def showBoardState(self):
        """This method get infromation from board, and shows which part of the board is bombed, and if it is a hit or not. 
        In the game, this method will be used by an opponent."""

    def bomb(self, coordination):
        """This method changes status of the board and shiplist after opponent's bombing"""

#Following is the structure of the game that I imagine.

#Get the name of the player 1 and 2 (Maybe not necessary).
x = input(Player1_name)
y = input(Player2_name)

while(player 1 and player 2 haven't set their status):
    while(player 1 haven't set the ships):
        #player 1 can add ship, and see own map.

    while(player 2 haven't set the ships):
        #player 2 can add ship, and see own map.

#Setting part is over, real game starts

while (player 1 and player 2 have ship):
    while(player 1 haven't finished bombing):
        #player 1 can see own ship, opponent's hit-map, or bomb certain location
    while(player 2 haven't finished bombing):
        #player 2 can see own ship, opponent's hit-map, or bomb certain location

print(player X wins)


-------------------------------------------------------------------------------------------------------------------------------
"""I think we are sharing the same idea, but my idea is to implement the board as a class so it will be more concise. 
ShipList will be a property of the class""" 

from random import randint

HIDDEN_BOARD = [[' ']*10 for x in range(10)] # computer board
OWN_BOARD =  [[' ']*10 for x in range(10)] # player board

ShipList = {}

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9),randint(0,9)
        ShipList[ship_column] = ship_row

def ShowList(board):
    



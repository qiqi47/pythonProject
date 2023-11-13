

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

from random import randint

HIDDEN_BOARD = [[' ']*10 for x in range(10)] # computer board
OWN_BOARD =  [[' ']*10 for x in range(10)] # player board

ShipList = {}

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9),randint(0,9)
        ShipList[ship_column] = ship_row

def ShowList(board):
    



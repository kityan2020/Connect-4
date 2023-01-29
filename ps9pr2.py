#
# ps9pr2.py (Problem Set 9, Problem 2)
#Partner: Dongjoon Shin
#Partner email:dongjoon@bu.edu
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """ A data type for player"""
    def __init__(self, checker):
        """ A  constructor for a Player object"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0 
    def __repr__(self):
        """ Returns a string representing a Player object to indicate which
        checker the Player object is using.
        """
        return 'Player ' + self.checker
    def opponent_checker(self):
        """ Returns a one-character string representing the checker of the 
        Player object’s opponent. This should be either X or O
        """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
    def next_move(self, b):
        """ accepts a Board object b as a parameter and 
        returns the column where the player wants to make the next move.
        """
        while True:
            col = input('Enter a column: ')
            if int(col) not in range(b.width):
                print('Try again!')
            else:
                self.num_moves += 1
                return int(col)
                
                break
        

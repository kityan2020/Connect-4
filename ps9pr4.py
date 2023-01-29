#Kit Chung Yan
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ A data type for AI"""
    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor for AI"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    def __repr__(self):
        """Returns a string representing an AIPlayer object."""
        return 'Player '+ (self.checker) + ' (' + self.tiebreak +', ' + str(self.lookahead)+ ')'
    def max_score_column(self, scores):
        """ a list scores containing a score for each column of the board
        and returns the index of the column with the maximum score
        """
        maxs = 0
        if self.tiebreak == 'LEFT':
            for x in range(len(scores)):
                if maxs < scores[x]:
                    maxs = scores[x]
                    index = x
            return index
        elif self.tiebreak == 'RIGHT':
           maxs = 0
           for x in range(len(scores)):
               if scores[x] >= maxs:
                   maxs = scores[x]
                   index = x
           return index
        elif self.tiebreak == 'RANDOM':
           x = [s for s in range(len(scores)) if scores[s] >= max(scores)]
           return random.choice(x)
           
        
           
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker)== True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker,col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_score = max(opp.scores_for(b))
                if opp_score == 0:
                    scores[col] = 100
                elif opp_score == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    def next_move(self,b):
        """replace the next_move method inherited from Player and return
        the AIPlayer's judgment of its best possible move
        """
        self.num_moves+=1
        return self.max_score_column(self.scores_for(b))
        
        
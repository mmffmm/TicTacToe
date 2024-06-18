import pygame as p
import tictactoe_engine as engine
import main as main

class Move ():
    
    def __init__(self, game_state):
        self.pick_x = 0
        self.pick_y = 0
        self.gs = game_state
        self.clicked = 0
        self.rule = Rule(self.gs)

    def click(self):
        self.pick_x, self.pick_y = p.mouse.get_pos()
        self.pick_x, self.pick_y = self.pick_x//200, self.pick_y//200
        print ("pick_x = ", self.pick_x)
        print ("pick_y = ", self.pick_y)
        print ("value = ", self.gs.board[self.pick_y][self.pick_x])


        if self.gs.board[self.pick_y][self.pick_x] == "--":
            if self.clicked%2 == 0:
                self.gs.board[self.pick_y][self.pick_x] = "X"
            elif self.clicked%2 == 1:
                self.gs.board[self.pick_y][self.pick_x] = "O"
   
        self.clicked+=1

        game_over = self.rule._checkGameOver()
        if game_over:
            print('game_over')

        return self.gs
    
class Rule() :

    def __init__(self, gs):
        self.gs = gs
    
    def _checkGameOver(self):
        #check for straight lines
        #for horizontal and vertical
        for i in [0,1,2]:
            if self.gs.board[0][i] != "--" and self.gs.board[0][i] == self.gs.board[1][i] == self.gs.board[2][i]:
                return True
            if self.gs.board[i][0] != "--" and self.gs.board[i][0] == self.gs.board[i][1] == self.gs.board[i][2]:
                return True
            
        if self.gs.board[0][0] != "--" and self.gs.board[0][0] == self.gs.board[1][1] == self.gs.board[2][2]:
            return True
        
        if self.gs.board[2][0] != "--" and self.gs.board[2][0] == self.gs.board[1][1] == self.gs.board[0][2]:
            return True
        
        return False








#         pass

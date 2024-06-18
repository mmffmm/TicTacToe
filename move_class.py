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

        return self.gs
    
class Rule() :

    def __init__(self, gs):
        self.gs = gs
        self.gameover = False
    
    def _checkGameOver(self):
        #check for straight lines
        #for horizontal, changes y only
        for i in [0,1,2]:
            if self.gs.board[0][i] != "--" and self.gs.board[0][i] == self.gs.board[1][i] == self.gs.board[2][i]:
                self.gameover = True
                break







#         pass

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
        self.game_over = False
        self.lines = []

    def click(self):
        self.pick_x, self.pick_y = p.mouse.get_pos()

        if self.pick_x<600:
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
            # else:
            #     pass
    
            if self.clicked>=5:
                self.game_over, self.lines = self.rule._checkGameOver()
                if self.game_over:
                    print('game_over')

            return self.game_over, self.lines
        
        else:
            return self.game_over, self.lines
    
class Rule() :

    def __init__(self, gs):
        self.gs = gs
    
    def _checkGameOver(self):
        #check for straight lines
        
        for i in [0,1,2]: # x start, x end, y start, y end
            #vertical
            if self.gs.board[0][i] != "--" and self.gs.board[0][i] == self.gs.board[1][i] == self.gs.board[2][i]:
                return True, [i*200+100,i*200+100,0,2*200+200]
            
            #horizontal
            if self.gs.board[i][0] != "--" and self.gs.board[i][0] == self.gs.board[i][1] == self.gs.board[i][2]:
                return True, [0,2*200+200,i*200+100,i*200+100]

        #for diagonal    
        if self.gs.board[0][0] != "--" and self.gs.board[0][0] == self.gs.board[1][1] == self.gs.board[2][2]:
            return True, [0,2*200+200,0,2*200+200]
        
        if self.gs.board[2][0] != "--" and self.gs.board[2][0] == self.gs.board[1][1] == self.gs.board[0][2]:
            return True, [2*200+200,0,0,2*200+200]
        
        return False, []

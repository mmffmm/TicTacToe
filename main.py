import pygame as p
import sys
import move_class as move
import tictactoe_engine as engine


WIDTH = 800
HEIGHT = 600
DIMENSION = 3
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

def initialize_game():
    global gs, click, game_over, lines
    gs = engine.Engine()
    # rule_instance = move.Rule()
    click = move.Move(gs)
    game_over = click.game_over
    lines = click.lines

# traveerse 2d array = array[y][x]
def main():
    global gs, click, game_over, lines
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    screen.fill(p.Color("grey"))
    p.display.update()
    clock = p.time.Clock()
    font = p.font.Font(None, 36)
    
    '''INIT'''
    initialize_game()
    restart = drawButton(screen, font)

    running = True

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                if restart.collidepoint(event.pos):
                    print('ho')
                    initialize_game()
                game_over, lines = click.click()
                
                 
                
        drawGameState(screen, gs, game_over, lines, font)
        clock.tick(MAX_FPS)
        p.display.flip()
        if game_over == True:
            pass




def drawGameState(screen, gs, game_over, lines, font):
    drawBoard(screen, game_over, lines)
    drawSymbol(screen, gs)



def drawBoard(screen, game_over, lines):
    colors = [p.Color("white"), p.Color("grey")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column)%2)] # cause in chess, if row+column is even number, then its white
            #draw rectangle(where is it drawn on, the color, p.Rect(x coordinate, y coordinate, width, height))
            p.draw.rect(screen, color, p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    p.draw.line(screen, p.Color('black'),(200,15),(200,585),10)
    p.draw.line(screen, p.Color('black'),(400,15),(400,585),10)
    p.draw.line(screen, p.Color('black'),(15,200),(585,200),10)
    p.draw.line(screen, p.Color('black'),(15,400),(585,400),10)

    if(game_over):
        print("yes")
        print(lines)
        p.draw.line(screen, p.Color('green'),(lines[0],lines[2]),(lines[1],lines[3]),10)
        game_over = False

def drawSymbol(screen, gs):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            symbol = gs.board[row][column]
            if symbol == "X":
                x_start = column * SQ_SIZE + SQ_SIZE // 5
                y_start = row * SQ_SIZE + SQ_SIZE // 5 
                x_end = (column + 1) * SQ_SIZE - SQ_SIZE // 5
                y_end = (row + 1) * SQ_SIZE - SQ_SIZE // 5
                p.draw.line(screen, p.Color('black'), (x_start, y_start), (x_end, y_end), 3)
                p.draw.line(screen, p.Color('black'), (x_start, y_end), (x_end, y_start), 3)
            elif symbol == "O":
                x_centre = column * SQ_SIZE + SQ_SIZE // 2
                y_centre = row * SQ_SIZE + SQ_SIZE // 2
                p.draw.circle(screen, p.Color("black"), (x_centre, y_centre), 60, 2)

            # elif symbol == "O":
            #     p.draw.circle(screen, p.Color('black'), column, row, SQ_SIZE, 3) 

def drawButton(screen, font):
    restart_rect = p.draw.rect(screen, p.Color(0,255,255), p.Rect(620, 50, 160, 50))
    text_surface = font.render('Restart', False, p.Color('black'))
    text_rect = text_surface.get_rect(center=restart_rect.center)
    screen.blit(text_surface, text_rect)

    return restart_rect


if __name__ == "__main__":
     main()


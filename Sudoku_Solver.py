# GUI.py
import pygame

import time
pygame.font.init()


board = [
         [0,0,9,0,3,0,0,1,0],
         [7,0,0,0,5,0,3,0,0],
         [0,0,2,8,0,6,0,4,0],
         [4,2,3,0,0,5,0,9,1],
         [0,0,0,9,1,2,0,0,0],
         [9,7,0,6,0,0,8,5,2],
         [0,9,0,3,0,8,1,0,0],
         [0,0,8,0,7,0,0,0,3],
         [0,5,0,0,2,0,4,0,0],

         ]

#Solves the board using a recursive backtracking algorithm,
#the findEmpty() method returns True if there are no more empty
#slots on the board, which then returns True for solve() all the way 
#back to the first time the function is called. If all numbers between
#1 and 9 are tried for a square and isValid() returns False for all of them,
#solve() returns false and the previous call of solve() would continue with its 
#for loop to try a different number. The process backtracks as much as 
#necessary until the most recent solve() returns True, which ends the
#algorithm and completes the Sudoku board.
def solve(board, win):
    empty = findEmpty(board)
    if empty==False:
        return True
    else:
        row = empty[0]
        col = empty[1]

    for i in range(1,10):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        if isValid(board,i,[row,col]):
            board[row][col] = i
            masterDraw(win)
            

            if solve(board, win):
                return True

            board[row][col] = 0

    return False




# check if the guessed number at position is valid (i.e. it does not violate the rules)     
def isValid(board, num, pos):
    row = pos[0]
    col = pos[1]

    # check the row
    for i in board[row]:
        if i==num:
            return False

    # check the column
    for i in board:
        if i[col]==num:
            return False

    # check the 3 by 3 square
    box_x = (row//3)*3
    box_y = (col//3)*3

    for i in range(3):
        for j in range(3):
            if board[box_x+i][box_y+j]==num:
                return False
    return True




#finds an empty square on the board to start the algorithm
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                return [i,j]
    return False


class Grid():
   



    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        #self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None
     
    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 3
            else:
                thick = 1

            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)


    def drawNums(self, win):
        gap = self.width / 9
        fnt = pygame.font.SysFont("TimesNewRoman", 40)
        x=0
        y=0
        for i in board:
            for j in i:

                if j is not 0:
                    num = fnt.render(str(j), 1, (0, 0, 0))
                    win.blit(num, (x + (gap/2 - num.get_width()/2), y + (gap/2 - num.get_height()/2)))
      
                x+=gap
            y+=gap
            x=0


Board = Grid(9, 9, 720, 720)
        

def masterDraw(win):
    win.fill((255,255,255))
    Board.draw(win)
    Board.drawNums(win)
    pygame.display.update()

    




def main():
    win = pygame.display.set_mode((720,720))
    pygame.display.set_caption("Sudoku")
    
    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            solve(board, win)
            
           


        win.fill((255,255,255))
    
        #Board.draw(win)
        masterDraw(win)


main()
pygame.quit()














import numpy as np
import copy
import math
import random

board = np.array([['' for _ in range(3)] for _ in range(3)])
scores = {'X':1, 'O':-1, 'Tie':0}

def minimax(board, depth, isMax=False):
    result = winstate(board)
    if result:
        #print(scores[result])
        return scores[result]
    if isMax:
        bestScore = -100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='X'
                    score = minimax(board, depth+1)
                    board[i][j]=''
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='O'
                    score = minimax(board, depth+1, True)
                    board[i][j]=''
                    bestScore = min(score, bestScore)
        return bestScore

class ai:
    def __init__(self, board):
        self.board = board
        self.figure = 'X'

    def rand_move(self):
        availables = []
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == '':
                    availables.append((row,column))
                    
        move = random.choice(availables)
        board[move[0]][move[1]] = self.figure
        return board

    def move(self):
        best_score = -100 #neg infinity
        row_col = (1,1)
        flag=0
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == '':
                    board[row][column] = 'X'
                    score = minimax(board,0)
                    board[row][column] = ''
                    if score>best_score:
                        best_score = score
                        row_col = (row, column)
                        print(score)
                    if score == -1:
                        flag = 1
                        print("he")
                        break
            if flag==1:
                print("he")
                break
        board[row_col[0]][row_col[1]] = self.figure
        return board

    
class human:
    def __init__(self, board):
        self.board = board
        self.figure = 'O'
        
    def move(self, row_col):
        self.board[row_col[0]][row_col[1]] = self.figure
        return self.board
        
def winstate(board):
    for i in range(len(board)):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != '':
            return board[i][0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != '':
            return board[0][i]
    if '' != board[0, 0] and board[0, 0] == board[1, 1] and board[1, 1] == board[2, 2]:
        return board[1, 1]
    if '' != board[2, 0] and board[2, 0] == board[1, 1] and board[1, 1] == board[0, 2]:
        return board[1, 1]
    if np.all(board != ''):
        return 'Tie'
    return

player = human(board)
ai_player = ai(board)
for i in range(9):
    if i%2==0:
        board = ai_player.move()
    else:
        user_input = input("Enter row, col as a tuple: ")
        row_col = tuple(int(x) for x in user_input.split(","))
        board = player.move(row_col)
    print(board)
        
    my_state = winstate(board)
    if my_state:
        if my_state=='X':
            print("X won")
        elif my_state=="O":
            print("O won")
        else:
            print("Draw")
        break
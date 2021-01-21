# Name: Rushil Umaretiya
# Date: 12/16/2020
import random

class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   def __str__(self):
      return "Random Player"

   def best_strategy(self, board, color):
      # returns best move
      # (column num, row num), 0
      try:
        best_move = random.choice(list(self.find_moves(board, color)))
      except IndexError:
          return (-1,-1), 0
      
      return (best_move // 5, best_move % 5), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24

      possible_moves = set()

      for x in range(len(board)):
         for y in range(len(board[x])):
            if self.first_turn and board[x][y] == '.': possible_moves.add(x*5+y)
            elif (color == self.black and board[x][y] == 'X') or (color == self.white and board[x][y] == 'O'):
               for direction in self.directions:
                  curr_x = x + direction[0]
                  curr_y = y + direction[1]
                  stop = False
                  while 0 <= curr_x < 5 and 0 <= curr_y < 5:
                     if board[curr_x][curr_y] != '.':
                           stop = True
                     if not stop:
                           possible_moves.add(curr_x*5+curr_y)
                     curr_x += direction[0]
                     curr_y += direction[1]

      self.first_turn = False
      return possible_moves

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
      self.color = None

   def __str__(self):
      return "Custom Player"

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])

      self.color = color
      v, best_move = self.alphabeta(board, color, search_depth=4, alpha=-999999999, beta=9999999)
      # v, best_move = self.minimax(board, color, search_depth=4)
      return (best_move // self.x_max, best_move % self.y_max), v

   def minimax(self, board, color, search_depth):
      return self.max_value(board, color, search_depth)

   def max_value(self, board, color, search_depth):
      # return value and state: (val, state)
      if search_depth <= 0 or self.terminal_test(board, color):
         return self.evaluate(board, self.color), board
      v = -99999
      result = 0
      for move in self.find_moves(board, color):
         max_val, max_state = self.min_value(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1)
         if v < max_val:
            v = max_val
            result = move

      return v, result

   def min_value(self, board, color, search_depth):
      # return value and state: (val, state)
      if search_depth <= 0 or self.terminal_test(board, color):
         return self.evaluate(board, self.color), board

      v = 999999999
      result = 0
      for move in self.find_moves(board, color):
         min_val, min_state = self.max_value(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1)
         if v > min_val:
            v = min_val
            result = move

      return v, result

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      terminal_test = self.terminal_test(board, color)
      if search_depth <= 0 or terminal_test:
         if terminal_test:
            for i in range(len(board)):
               for j in range(len(board[i])):
                  if (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                     move = i*self.x_max+j
            if color == self.color:
               return 9999, move
            else:
               return -9999, move
         return self.evaluate(board, self.color), 0

      if search_depth % 2 == 0:
         v = -9999999999
         result = 0
         for move in self.find_moves(board, color):
            max_val, max_state = self.alphabeta(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1, alpha, beta)
            if v < max_val:
               v = max_val
               result = move
            if v > beta:
               return v, result
            alpha = max(alpha, v)
         return v, result
      else:
         v = 9999999999
         result = 0
         for move in self.find_moves(board, color):
            min_val, min_state = self.alphabeta(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1, alpha, beta)
            if v > min_val:
               v = min_val
               result = move
            if v < alpha:
               return v, result
            beta = min(beta, v)
         return v, result

   def make_move(self, board, color, move):
      successor = [x[:] for x in board]
      for i in range(len(board)):
         for j in range(len(board[i])):
            if (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
               successor[i][j] = "W"
      successor[move // 5][move % 5] = 'X' if color == self.black else 'O'
      return successor
      
   def terminal_test (self, board, color):
      my_moves = self.find_moves(board, color)
      opponent_moves = self.find_moves(board, self.opposite_color[color])
      if len(my_moves) == 0 or len(opponent_moves) == 0:
         return True
      else:
         return False

   def evaluate(self, board, color):
      my_moves = len(self.find_moves(board, color))
      opponent_moves = len(self.find_moves(board, self.opposite_color[color]))
      if my_moves == 0 and opponent_moves == 0:
         return 0
      elif my_moves == 0:
         return -1000
      elif opponent_moves == 0:
         return 1000
      else:
         return my_moves - opponent_moves

   def find_moves(self, board, color):
      # finds all possible moves
      possible_moves = set()
      for x in range(len(board)):
         for y in range(len(board[x])):
            if len([y for x in board for y in x if y != '.']) < 2 and board[x][y] == '.': possible_moves.add(x*5+y)
            elif (color == self.black and board[x][y] == 'X') or (color == self.white and board[x][y] == 'O'):
               for direction in self.directions:
                  curr_x = x + direction[0]
                  curr_y = y + direction[1]
                  stop = False
                  while 0 <= curr_x < 5 and 0 <= curr_y < 5:
                     if board[curr_x][curr_y] != '.':
                           stop = True
                     if not stop:
                           possible_moves.add(curr_x*self.y_max+curr_y)
                     curr_x += direction[0]
                     curr_y += direction[1]

      return possible_moves
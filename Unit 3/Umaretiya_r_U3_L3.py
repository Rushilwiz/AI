# Name: Rushil Umaretiya
# Date: 1/8/2021

import random

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      random_move, flipped_stones = random.choice(list(self.find_moves(board, color).items()))

      return (random_move // self.x_max, random_move % self.y_max), len(flipped_stones)

   def stones_left(self, board):
      left = 0
      for i in range(board):
         for j in range(board[i]):
            if board[i][j] == '.': left += 1
      
      return left

   def find_moves(self, board, color):
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i * self.y_max + j: flipped_stones})
    return moves_found

   def find_flipped(self, board, x, y, color):
      if board[x][y] != ".":
         return []
      
      if color == self.black:
         color = "@"
      else:
         color = "O"
      
      flipped_stones = []

      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]

      return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.logging = True
      self.white = "#ffffff" # "O"
      self.black = "#000000" # "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.heuristic_table = [
         [999,-3,2,2,2,2,-3,999],
         [-3,-4,-1,-1,-1,-1,-4,-3],
         [2,-1,1,0,0,1,-1,2],
         [2,-1,0,1,1,0,-1,2],
         [2,-1,0,1,1,0,-1,2],
         [2,-1,1,0,0,1,-1,2],
         [-3,-4,-1,-1,-1,-1,-4,-3],
         [999, -3, 2, 2, 2, 2, -3, 999],
      ]

   def best_strategy(self, board, color):
      self.x_max = len(board)
      self.y_max = len(board[0])
      
      stones_left = self.stones_left(board)
      if stones_left > 32:
         sd = 5
      elif stones_left > 10:
         sd = 6
      else:
         sd = 8
      
      v, best_move = self.alphabeta(board, color, search_depth=sd, alpha=-9999999999, beta=9999999999)   # returns state

      return (best_move // self.x_max, best_move % self.y_max), 0

   def minimax(self, board, color, search_depth):
      # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta, last_move=-1):
      if search_depth <= 0 or self.terminal_test(board):
         return self.evaluate(board, color, last_move), board

      if search_depth % 2 == 0:
         v = -9999999999
         result = board
         for move, flipped in self.find_moves(board, color).items():
            max_val, max_state = self.alphabeta(self.make_move(board, color, move, flipped), self.opposite_color[color], search_depth - 1, alpha, beta, move)
            v = max (v, max_val)
            result = move
            if v > beta:
               return v, result
            alpha = max(alpha, v)
         
         return v, result
      else:
         v = 9999999999
         result = board
         for move, flipped in self.find_moves(board, color).items():
            min_val, min_state = self.alphabeta(self.make_move(board, color, move, flipped), self.opposite_color[color], search_depth - 1, alpha, beta, move)
            v = min (v, min_val)
            result = move
            if v < alpha:
               return v, result
            beta = max(beta, v)

         return v, result

   def terminal_test(self, board):
      return self.stones_left(board) == 0

   def stones_left(self, board):
      left = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.': left += 1
      
      return left

   def make_move(self, board, color, move, flipped):
      my_board = [row[:] for row in board]

      if color == self.black:
         color = "@"
      else:
         color = "O"
      
      my_board[move // self.x_max][move % self.y_max] = color
      for flip in flipped:
         my_board[flip[0]][flip[1]] = color
      
      return my_board

   def evaluate(self, board, color, last_move, possible_moves=[]):
      score = self.score(board, color)
      if last_move != -1:
         heuristic = self.heuristic_table[last_move // self.x_max][last_move % self.y_max]
         return score * heuristic
      else:
         return score



   def score(self, board, color):
      if color == self.black:
         color = "@"
      else:
         color = "O"

      score = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == color:
               score += 1
            elif board[i][j] != '.':
               score -= 1

      return score
      

   def find_moves(self, board, color):
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                  moves_found.update({i * self.y_max + j: flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
      if board[x][y] != ".":
         return []
      
      if color == self.black:
         color = "@"
      else:
         color = "O"
      
      flipped_stones = []

      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
               if board[x_pos][y_pos] == ".":
                  break
               if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
               temp_flip.append([x_pos, y_pos])
               x_pos += incr[0]
               y_pos += incr[1]

      return flipped_stones
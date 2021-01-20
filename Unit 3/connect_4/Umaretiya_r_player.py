# Name: Rushil Umaretiya
# Date: 1/18/21

import random

class RandomBot:
   def __init__(self):
      self.yellow = "O"
      self.red = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.red: self.yellow, self.yellow: self.red}
      self.x_max = None
      self.y_max = None

   def __str__(self):
      return "Random Bot"

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#ffff00":
         color = "O"
      else:
         color = "X"
      
      best_move = random.choice(self.find_moves(board, color))

      return best_move, 0

   def find_moves(self, board, color):
      moves_found = []
      for col in range(self.x_max):
         for row in reversed(range(self.y_max)):
               if board[col][row] == '.':
                  moves_found.append([col, row])
                  break
      return moves_found

class SmartBot:

   def __init__(self):
      self.yellow = "O"
      self.red = "X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.red: self.yellow, self.yellow: self.red}
      self.x_max = None
      self.y_max = None
      self.color = None

   def __str__(self):
      return "Smart Bot"

   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])

      if color == "#ffff00":
         color = "O"
      else:
         color = "X"
      self.color = color

      sd = 4
      v, best_move = self.alphabeta(board, color, sd, 9999999999, 9999999999)   # returns state

      return best_move, v
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      terminal_test = self.terminal_test(board, color)
      if search_depth <= 0 or terminal_test:
         if terminal_test:
            if color == self.color:
               return 99999999, board
            else:
               return -99999999, board
         heuristic = self.evaluate(board, color)
         print("I'm seeing a heuristic of: ", heuristic)
         return heuristic, board
      
      if search_depth % 2 == 0:
         v = -9999999999
         result = board
         for move in self.find_moves(board, color):
            max_val, max_state = self.alphabeta(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1, alpha, beta)
            v = max (v, max_val)
            result = move
            if v > beta:
               return v, result
            alpha = max(alpha, v)
         
         return v, result
      else:
         v = 9999999999
         result = board
         for move in self.find_moves(board, color):
            min_val, min_state = self.alphabeta(self.make_move(board, color, move), self.opposite_color[color], search_depth - 1, alpha, beta)
            v = min (v, min_val)
            result = move
            if v < alpha:
               return v, result
            beta = max(beta, v)

         return v, result

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1

   def make_move(self, board, color, move):
      my_board = [row[:] for row in board]

      if color == "#ffff00":
         color = "O"
      else:
         color = "X"
      
      my_board[move[0]][move[1]] = color
      
      return my_board

   def terminal_test(self, board, color):
      for col in range(len(board)):
         for row in range(len(board[col])):
            if board[col][row] == color:
               for direction in self.directions:
                  x_pos = col
                  y_pos = row
                  row_count = 0
                  while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                     if board[x_pos][y_pos] == color:
                        row_count += 1
                        if row_count == 4: return True
                     else:
                        break
                     x_pos += direction[0]
                     y_pos += direction[1]
      return False

   def evaluate(self, board, color):
      heuristic = 0
      
      # Center Column
      center_array = [i for i in board[self.x_max // 2]]
      center_heuristic = center_array.count(color)
      heuristic += center_heuristic * 3

      # Columns
      for col in range(self.x_max):
         col_array = [i for i in board[col]]
         for row in range(self.y_max - 3):
            array = col_array[row : row + 4]
            heuristic += self.evaluate_array(array, color)
      
      # Rows
      for row in range(self.y_max):
         row_array = [i[row] for i in board]
         for col in range(self.x_max - 3):
            array = row_array[col : col + 4]
            heuristic += self.evaluate_array(array, color)
      
      # Diagonals
      for col in range(self.x_max - 3):
         for row in range(self.y_max - 3):
            array = [board[col + i][row + 1] for i in range(4)]
            heuristic += self.evaluate_array(array, color)
      
      for col in range(self.x_max - 3):
         for row in range(self.y_max - 3):
            array = [board[col + 3 - i][row + i] for i in range(4)]
            heuristic += self.evaluate_array(array, color)
      
      return heuristic

   def evaluate_array(self, array, color):
      heuristic = 0
      opposite_color = self.opposite_color[color]

      if array.count(color) == 4:
         heuristic += 999
      elif array.count(color) == 3 and array.count('.') == 1:
         heuristic += 5
      elif array.count(color) == 2 and array.count('.') == 2:
         heuristic += 2
      
      if array.count(opposite_color) == 3 and array.count('.') == 1:
         heuristic -= 100
      
      return heuristic

   def find_moves(self, board, color):
      moves_found = []
      for col in range(self.x_max):
         for row in reversed(range(self.y_max)):
               if board[col][row] == '.':
                  moves_found.append([col, row])
                  break
      return moves_found
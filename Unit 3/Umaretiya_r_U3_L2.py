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

   def __str__(self):
      return "Custom Player"

   def utility (self, board, color):
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
      
   def terminal_test (self, board, color):
      my_moves = self.find_moves(board, color)
      opponent_moves = self.find_moves(board, self.opposite_color[color])
      if len(my_moves) == 0 or len(opponent_moves) == 0:
         return True
      else:
         return False

   def best_strategy(self, board, color):
      # returns best move
      best_move = self.minimax(board, color, 2)
      return best_move 

   def minimax(self, board, color, search_depth):
      max_val = self.max_value(board, color, search_depth)   # returns state
      move = self.current_position(max_val[1], color)
      return (move // 5, move % 5), max_val[0]

   def current_position(self, board, color):
      for i in range(len(board)):
         for j in range(len(board[i])):
            if (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
               return i*5+j
      return -1

   def successors(self, board, color):
      successors = []
      moves = self.find_moves(board, color)
      current_position = self.current_position(board, color)
      for move in moves:
         successor = [x[:] for x in board]
         if current_position != -1:
            successor[current_position // 5][current_position % 5] = "W"
         successor[move // 5][move % 5] = 'X' if color == self.black else 'O'
         successors.append(successor)
      return successors

   def max_value(self, board, color, search_depth):
      # return value and state: (val, state)
      if search_depth <= 0 or self.terminal_test(board, color):
         return self.utility(board, color), board
      v = -99999
      result = board
      for successor in self.successors(board, color):
         min_val, min_state = self.min_value(successor, self.opposite_color[color], search_depth - 1)
         if v < min_val:
            v = min_val
            result = successor

      return v, result

   def min_value(self, board, color, search_depth):
      # return value and state: (val, state)



      if search_depth <= 0 or self.terminal_test(board, color):
         return self.utility(board, self.opposite_color[color]), board

      v = 99999
      result = board
      for successor in self.successors(board, color):
         max_val, max_state = self.max_value(successor, self.opposite_color[color], search_depth - 1)
         if v > max_val:
            v = max_val
            result = successor

      return v, result

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      return 1

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
                           possible_moves.add(curr_x*5+curr_y)
                     curr_x += direction[0]
                     curr_y += direction[1]

      return possible_moves
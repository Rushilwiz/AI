# Name: Rushil Umaretiya
# Date: 12/1/2020
import os, time, operator, copy

def solve(puzzle, neighbors): 
   ''' suggestion:
   # q_table is quantity table {'1': number of value '1' occurred, ...}
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  
   return recursive_backtracking(puzzle, variables, neighbors, q_table)
   '''
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  
   return recursive_backtracking(puzzle, variables, neighbors, q_table)

def initialize_ds(puzzle, neighbors):
   vars = {}
   q_table = {x: 0 for x in range(1, 10)}
   for i in range(len(puzzle)):
      if puzzle[i] == '.':
         vars[i] = list(range(1,10))
      else:
         q_table[int(puzzle[i])] += 1
   
   return vars, puzzle, q_table

def recursive_backtracking(puzzle, variables, neighbors, q_table):
   if check_complete(puzzle, neighbors, variables): return puzzle

   var = select_unassigned_var(puzzle, variables, neighbors)

   for value in ordered_domain(var, variables, q_table):
      if q_table[value] < 9 and isValid(value, var, puzzle, neighbors):
         puzzle = puzzle[:var] + str(value) + puzzle[var + 1:]
         q_table[value] += 1
         result = recursive_backtracking(puzzle, update_variables(value, var, puzzle, variables, neighbors), neighbors, q_table)
         if result != None: return result
         puzzle = puzzle[:var] + '.' + puzzle[var + 1:]
         q_table[value] -= 1

def ordered_domain(var, variables, q_table):
   return sorted(variables[var], key=lambda k: q_table[k], reverse=True)

def check_complete(puzzle, neighbors, variables):
   if len(variables) != 0: return False
   for index in range(len(puzzle)):
      for neighbor in neighbors[index]:
         if puzzle[index] == puzzle[neighbor]: return False
   return True
   
def select_unassigned_var(puzzle, variables, neighbors):
   min, index = 9999, -1
   for i in variables:
      if min > len(variables[i]):
         min = len(variables[i])
         index = i
   return index
   
   #return min(variables, key=lambda k: len(variables[k]))

def isValid(value, var_index, puzzle, neighbors):
   value_string = str(value)
   for i in neighbors[var_index]:
      if puzzle[i] == value_string:
         return False

   return True

def update_variables(value, var_index, puzzle, variables, neighbors):
   updated = {k: list(variables[k]) for k in variables}
   del updated[var_index]

   for i in neighbors[var_index]:
      if i in updated and value in updated[i]:
         updated[i].remove(value)
   
   return updated

def sudoku_neighbors(csp_table):
   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   neighbors = {}
   for i in range(81):
      temp = []
      for constraint in csp_table:
         if i in constraint:
            removed = list(constraint)
            removed.remove(i)
            temp += removed
      neighbors[i] = set(temp)
   
   return neighbors
   
def sudoku_csp(n=9):
   csp_table = [[k for k in range(i*n, (i+1)*n)] for i in range(n)] # rows
   csp_table += [[k for k in range(i,n*n,n)] for i in range(n)] # cols
   temp = [0, 1, 2, 9, 10, 11, 18, 19, 20]
   csp_table += [[i+k for k in temp] for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]] # sub_blocks
   return csp_table

def checksum(solution):
   return sum([ord(c) for c in solution]) - 48*81 # One easy way to check a valid solution

def main():
   #filename = input("file name: ")
   filename = ""
   if not os.path.isfile(filename):
      filename = "puzzles.txt"
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   
   
   puzzle = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
   import cProfile
   cProfile.runctx('g(puzzle, neighbors)', {'g': solve, 'puzzle': puzzle, 'neighbors': neighbors}, {})
   
   """
   for line, puzzle in enumerate(open(filename).readlines()):
      # if line == 50: break  # check point: goal is less than 0.5 sec
      line, puzzle = line+1, puzzle.rstrip()
      print ("Line {}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}({}, {})".format(" "*(len(str(line))+1), checksum(solution), solution))
   """
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
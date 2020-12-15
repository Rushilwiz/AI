# Name: Rushil Umaretiya
# Date: 11/17/20

import time
import copy as cp

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for area in csp_table:
      if len(set([assignment[i] for i in area])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   min_val, index = 9999, -1
   for i in range(len(assignment)):
      if assignment[i] == '.' and len(variables[i]) < min_val:
         min_val = len(variables[i])
         index = i
   return index

def isValid(value, var_index, assignment, variables, csp_table):
   csp_indexes = [i for i in range(len(csp_table)) if var_index in csp_table[i]]
   for index in csp_indexes:
      for i in csp_table[index]:
         if i != var_index and assignment[i] == str(value):
            return False

   return True

def ordered_domain(assignment, variables, csp_table):
   return [x for _,x in sorted(zip([assignment.count(str(i)) for i in range(1, 10)],list(range(1,10))), reverse=True)]

def update_variables(value, var_index, assignment, variables, csp_table):
   updated = cp.deepcopy(variables)
   csp_indexes = [i for i in range(len(csp_table)) if var_index in csp_table[i]]
   for index in csp_indexes:
      constraint_area = csp_table[index]
      for i in constraint_area:
         if i != var_index and i in updated and value in updated[i]:
            updated[i].remove(value)
   return updated

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment, csp_table):
      return assignment

   var = select_unassigned_var(assignment, variables, csp_table)

   for value in ordered_domain(assignment, variables, csp_table):
      if value in variables[var] and isValid(value, var, assignment, variables, csp_table):
         assignment = assignment[:var] + str(value) + assignment[var + 1:]
         copy = update_variables(value, var, assignment, variables, csp_table)
         #copy = cp.deepcopy(variables)
         result = recursive_backtracking(assignment, copy, csp_table)
         if result != None: return result
         assignment = assignment[:var] + '.' + assignment[var + 1:]

   return None

def display(solution):
   string = ""
   for i in range(9):
      for j in range(9):
         string += solution[(i*9)+j] + " "
         if j == 2 or j == 5:
            string += "  "
      string += '\n'
      if i == 2 or i == 5:
         string +='\n'
   return string

def sudoku_csp():
   table, square, col, row = [], [0,1,2,9,10,11,18,19,20], [0,9,18,27,36,45,54,63,72], list(range(9))
   for i in range(9):
       table.append([index+(i*3)+((i//3)*18) for index in square])
       table.append([index+i for index in col])
       table.append([index+(i*9) for index in row])
   return table
   
def initial_variables(puzzle, csp_table):
   vars = {}
   for i in range(len(puzzle)):
      if puzzle[i] == '.':
         vars[i] = list(range(1,10))
   
   return constrain_init(vars, puzzle, csp_table)

def constrain_init (vars, puzzle, csp_table):
   updated = dict(vars)
   for var_index in range(len(puzzle)):
      if puzzle[var_index] != '.':
         updated = update_variables(int(puzzle[var_index]), var_index, puzzle, vars, csp_table)
   
   return updated

def main():
   #puzzle = input("Type a 81-char string:") 
   #puzzle = ".21.7...63.9...5.......1...13...8....84...9....6...34......6.87.....36..7...8..9."
   #puzzle = "4.....3.....8.2......7........1...8734.......6........5...6........1.4...82......"
   #puzzle = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
   puzzle = "3..........5..9...2..5.4....2....7..16.....587.431.6.....89.1......67.8......5437"
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   start_time = time.time()
   #import cProfile
   #cProfile.runctx('g(puzzle, variables, csp_table)', {'g': backtracking_search, 'puzzle': puzzle, 'variables': variables, 'csp_table': csp_table}, {})
   solution = backtracking_search(puzzle,variables,csp_table)
   if solution != None: print ("solution\n + display(solution)" + display(solution))
   else: print ("No solution found.\n")
   print ("Duration:", (time.time() - start_time))
   
if __name__ == '__main__': main()

"""
..7369825632158947958724316825437169791586432346912758289643571573291684164875293
4 1 7   3 6 9   8 2 5
6 3 2   1 5 8   9 4 7
9 5 8   7 2 4   3 1 6

8 2 5   4 3 7   1 6 9
7 9 1   5 8 6   4 3 2
3 4 6   9 1 2   7 5 8

2 8 9   6 4 3   5 7 1
5 7 3   2 9 1   6 8 4
1 6 4   8 7 5   2 9 3

.3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.
1 3 7   2 5 6   8 4 9
9 2 8   3 1 4   5 6 7
4 6 5   8 9 7   3 1 2

6 7 3   5 4 2   9 8 1
8 1 9   6 7 3   2 5 4
5 4 2   1 8 9   7 3 6

2 5 6   7 3 1   4 9 8
3 9 1   4 2 8   6 7 5
7 8 4   9 6 5   1 2 3

....8....27.....54.95...81...98.64...2.4.3.6...69.51...17...62.46.....38....9....
1 3 4   5 8 7   2 9 6
2 7 8   1 6 9   3 5 4
6 9 5   2 3 4   8 1 7

3 5 9   8 1 6   4 7 2
8 2 1   4 7 3   5 6 9
7 4 6   9 2 5   1 8 3

9 1 7   3 4 8   6 2 5
4 6 2   7 5 1   9 3 8
5 8 3   6 9 2   7 4 1
"""
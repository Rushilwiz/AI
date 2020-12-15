# Name: Rushil Umaretiya
# Date: 11/12/2020

import time

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 6: return False
   return True
   
def select_unassigned_var(assignment, csp_table):
   if '.' in assignment: return assignment.find('.')
   else: return None
   
def isValid(value, var_index, assignment, csp_table):
   csp_indexes = [i for i in range(len(csp_table)) if var_index in csp_table[i]]
   for index in csp_indexes:
      hex = csp_table[index]
      for i in hex:
         if i != var_index and assignment[i] == str(value): return False
   
   return True

def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def recursive_backtracking(assignment, csp_table):
   if check_complete(assignment, csp_table): return assignment

   var = select_unassigned_var(assignment, csp_table)

   for value in range(1, 7):
      if isValid(value, var, assignment, csp_table):
         assignment = assignment[:var] + str(value) + assignment[var + 1:]
         result = recursive_backtracking(assignment, csp_table)
         if result != None: return result
         assignment = assignment[:var] + '.' + assignment[var + 1:]

   return None  

def display(solution):
   result = ""
   for i in range(len(solution)):
      if i == 0: result += "  "
      if i == 5: result += "\n"
      if i == 12: result += "\n"
      if i == 19: result += "\n  "
      result += solution[i] + " "
   return result

def main():
   csp_table = [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]] 
   string = input("24-char(. and 1-6) input: ")
   cur_time = time.time()
   solution = backtracking_search(string, csp_table)
   if solution != None:
      print (display(solution))
      print ('\n'+ solution)
      print (check_complete(solution, csp_table))
      print ('Duration:', (time.time() - cur_time))
   else: print ("It's not solvable.")

if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 

123121456451263123624546
True

Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 

612131345641562132534546
True
"""
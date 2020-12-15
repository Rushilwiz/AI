# Name: Rushil Umaretiya
# Period: 1

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   for i in vars:
      if i not in assignment: return False

   for assigned in assignment:
      if assigned in adjs:
         for adj in adjs[assigned]:
            if assignment[assigned] == assignment[adj]: return False

   return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   var, low = '', 999999
   for i in vars:
      if len(vars[i]) < low and len(vars[i]) > 0:
         var = i
         low = len(vars[i])

   
   return var if var != '' else None

   
def isValid(value, var, assignment, vars, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.

   if var not in adjs: return True

   for adj in adjs[var]:
      if adj in assignment and value in assignment[adj]: return False

   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, vars, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   if check_complete(assignment, vars, adjs): 
      draw_final_shapes(assignment, shapes, frame)
      return assignment

   var = select_unassigned_var(assignment, vars, adjs)

   for value in vars[var]:
      if isValid(value, var, assignment, vars, adjs):
         assignment[var] = value
         new_vars = dict(vars)
         new_vars[var] = {}
         if var in adjs:
            for i in adjs[var]:
               if value in new_vars[i]: new_vars[i].remove(value)
         result = recursive_backtracking(assignment, new_vars, adjs, shapes, frame)
         if result != None: return result
         assignment.pop(var)

   return None


def draw_final_shapes(assignment, shapes, frame):
   for node in assignment:
      draw_shape(shapes[node], frame, assignment[node])
      

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, vars, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   for line in open('mcNodes.txt', 'r'): regions.append(line.strip())
   

   # Fill variables by using regions list -- no additional code for this part
   for r in regions: vars[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   for line in open('mcEdges.txt', 'r'):
      line = line.strip().split()
      if line[0] not in adjacents: adjacents[line[0]] = [line[1]]
      else: adjacents[line[0]].append(line[1])

      if line[1] not in adjacents: adjacents[line[1]] = [line[0]]
      else: adjacents[line[1]].append(line[0])


   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(vars, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()

''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''
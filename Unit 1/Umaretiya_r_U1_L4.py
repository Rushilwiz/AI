# Name: Rushil Umaretiya
# Date: 10/11/2020
import random, time, math

class HeapPriorityQueue():
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) <= 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue)-1)

   # helper method for push      
   def heapUp(self, k):
      if k <= 1:
         return

      if len(self.queue) % 2 == 1 and k == len(self.queue) - 1: # no sibling
         if self.queue[k//2][1] > self.queue[k][1]:
            self.swap(k, k//2)
            self.heapUp(k//2)
         return

      if k % 2 == 0:
         parent, sibling = k//2, k+1
      else:
         parent, sibling = k//2, k-1

      if self.queue[k][1] > self.queue[sibling][1]:
         child = sibling
      else:
         child = k

      if self.queue[parent][1] > self.queue[child][1]:
         self.swap(child, parent)
         self.heapUp(parent)

               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2*k, 2*k+1

      if left == size and self.queue[k][1] > self.queue[size][1]: # One child
         self.swap(k, left)

      elif right <= size:
         child = (left if self.queue[left][1] < self.queue[right][1] else right)

         if self.queue[k][1] > self.queue[child][1]:
            self.swap(k, child)
            self.heapDown(child, size)
      
   # make the queue as a min-heap            
   def reheap(self):
      if self.isEmpty():
         return -1

      for k in range((len(self.queue)-1)//2, 0, -1):
         self.heapUp(k)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      if self.isEmpty():
         return -1
      self.swap (1, len(self.queue) - 1)
      val = self.queue.pop()
      self.heapDown(1, len(self.queue) - 1)
      return val
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      if self.isEmpty():
         return -1
      
      if len (self.queue) == 2:
         val = self.queue.pop()
         self.queue = []
         return val
      
      self.swap (index + 1, len(self.queue) - 1)
      val = self.queue.pop()
      self.heapDown(index + 1, len(self.queue) - 1)

      return val

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   inversion_count = 0
   for i in range(len(new_state)):
      for j in range(i, len(new_state)):
         if new_state[i] != '_':
            if new_state[i] > new_state[j]:
               inversion_count += 1

   if N % 2 == 0:
      blank = new_state.find('_')
      if (blank // width) % 2 == 0:
         return inversion_count % 2 == 0
      else:
         return inversion_count % 2 != 0
   else:
      return inversion_count % 2 == 0

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
'''precondition: i<j
    swap characters at position i and j and return the new state'''
def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return "".join(state)

'''Generate a list which hold all children of the current state
    and return the list'''
def generate_children(state, size=4):
    empty = state.find("_")
    children = []
    left, right = empty - 1, empty + 1
    up, down = empty - size, empty + size
    if right % size != 0:
        children.append(swap(state, empty, right))
    if left % size != size - 1:
        children.append(swap(state, empty, left))
    if up > -1:
        children.append(swap(state, empty, up))
    if down < len(state):
        children.append(swap(state, empty, down))

    return children

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   md = 0
   for i in range(len(state)):
      if state[i] != '_':
         md += abs(goal.find(state[i]) % size - i % size) + abs(goal.find(state[i]) // size - i // size) 

   return md

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b)

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   frontier = HeapPriorityQueue()
   explored = {}
   if start == goal: return []
   # We are pushing tuples of the (current_node, path_cost+heuristic, path)
   frontier.push((start, heuristic(start, goal, size), [start]))
   explored[start] = heuristic(start, goal, size)
   while not frontier.isEmpty():
      # Pop off the heapq
      state = frontier.pop()
      
      # Goal Test
      if state[0] == goal:
         return state[2]
      
      # Push children onto priority queue
      for i in generate_children(state[0], size):
         cost = heuristic(i, goal, size) + len(state[2]) + 1
         print(cost)
         if i not in explored.keys() or explored[i] > cost:
            explored[i] = cost
            frontier.push((i, cost, state[2] + [i]))

   return None

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''


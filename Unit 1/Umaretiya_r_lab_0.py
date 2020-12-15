# Name: Rushil Umaretiya
# Date: 09/18/2020

# Each Vertex object will have attributes to store its own name and its list of its neighboring vertices.
class Vertex:
   def __init__(self, name, vertices):
      self.name = name
      self.vertices = vertices

   def __str__(self):
      return f'{self.name} {self.vertices}'

   def __repr__(self):
      return str(self.name)


# If the file exists, read all edges and build a graph. It returns a list of Vertexes.
def build_graph(filename):
   try:
      file = open(filename, 'r')
   except:
      return []

   lines = file.read().strip().splitlines()
   vertices = []

  # Sorry about this solution Ms. Kim, it's not very efficient, but it makes sense.

  # Create all the source verticies
   for line in lines:
      line = line.strip().split()
      for vertex in vertices:
         if vertex.name == line[0]:
            break
      else:
         vertices.append(Vertex(line[0], []))

  # Create all the ending verticies
   for line in lines:
      line = line.strip().split()
      for vertex in vertices:
         if vertex.name == line[1]:
            break
      else:
         vertices.append(Vertex(line[1], []))

  # Link them!
   for line in lines:
      line = line.strip().split()
      source, end = None, None
      for vertex in vertices:
         if vertex.name == line[0]:
            source = vertex
         if vertex.name == line[1]:
            end = vertex
         if source != None and end != None:
            break
   
      source.vertices.append(end)

   return vertices

# prints all vertices and adjacent lists of the given graph.
def display_graph(graph):
   for vertex in graph:
      print (vertex)

# checks if two Vertexes are reachable or not.
def is_reachable(fromV, toV, graph):
   visited = []
   Q = [fromV]

   while len(Q) > 0:
      state = Q.pop(0)
   
      if state not in visited:
         if state == toV:
            return True
      
         visited.append(state)
         neighbours = state.vertices
      
         for neighbour in neighbours:
            Q.append(neighbour)

   return False

# returns the length of the path from a Vertex to the other Vertex.
# If the other Vertex is not reachable, return -1.  (Ex) Path cost of A to B to C is 2.
def path_cost(fromV, toV, graph):
   if fromV == toV:
      return 0

   if not is_reachable(fromV, toV, graph):
      return -1

   visited = []
   Q = [fromV]

   while len(Q) > 0:
      state = Q.pop(0)
      if state not in visited:
         if state == toV:
            return len(visited)
      
         visited.append(state)
         neighbours = state.vertices
      
         for neighbour in neighbours:
            Q.append(neighbour)
          
# Test cases
g = build_graph(input("filename: "))   # build a graph

# To check if you build the graph with object correctly
for v in g:
   print (v, v.vertices)
   
display_graph(g)                       # display the graph (edge list)
fromV, toV = None, None
print ("If you want to stop checking, type -1 for vertex values")
fromV_val, toV_val = input("From vertex value: "), input("To vertex value: ")    # Get vertex values from user

while fromV_val != '-1':
   # Find from and to Vertexes at graph
   for v in g:                         
      if v.name == fromV_val: fromV = v     
      if v.name == toV_val: toV = v

   if fromV is None or toV is None:
      print ("One or more vertex value does not exist.")
   else:
      print ("From {} to {} is reachable?".format(fromV_val, toV_val), is_reachable(fromV, toV, g))
      print ("Path cost from {} to {} is".format(fromV_val, toV_val), path_cost(fromV, toV, g))

   # Reset to test another case
   fromV_val, toV_val = input("\nFrom vertex value: "), input("To vertex value: ")
   fromV, toV = None, None

import random

def getInitialState():
    x = "_12345678"
    l = list(x)
    random.shuffle(l)
    y = ''.join(l)
    return y
    
'''precondition: i<j
    swap characters at position i and j and return the new state'''
def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return "".join(state)

'''Generate a list which hold all children of the current state
    and return the list'''
def generate_children(state):
    empty = state.find("_")
    children = []

    if empty == 4: # Center Case
        children.append(swap(state, empty, empty+1))
        children.append(swap(state, empty, empty+3))
        children.append(swap(state, empty, empty-1))
        children.append(swap(state, empty, empty-3))

    elif empty % 2 != 0: # Edge Case
        children.append(swap(state, empty, 4)) # Always attach center
        if empty - 3 >= 0 and empty + 3 < len(state):
            children.append(swap(state, empty, empty+3))
            children.append(swap(state, empty, empty-3))
        else:
            children.append(swap(state, empty, empty+1))
            children.append(swap(state, empty, empty-1))

    else: # Corner Case
        if empty < 4:
            children.append(swap(state, empty, empty+3))
            if empty < 1:
                children.append(swap(state, empty, empty+1))
            else:
                children.append(swap(state, empty, empty-1))
        else:
            children.append(swap(state, empty, empty-3))
            if empty > 7:
                children.append(swap(state, empty, empty-1))
            else:
                children.append(swap(state, empty, empty+1))

    return children

def display_path(n, explored): #key: current, value: parent
    l = []
    while explored[n] != "s": #"s" is initial's parent
        l.append((n, direction(n, explored[n])))
        n = explored[n]
    print ()
    l = l[::-1]
    for d in l:
        print (d[1], end = "     ")
    print()

    for i in l:
        print (i[0][0:3], end = "   ")
    print ()
    for j in l:
        print (j[0][3:6], end = "   ")
    print()
    for k in l:
        print (k[0][6:9], end = "   ")
    print ("\n\nThe shortest path length is :", len(l))
    return ""

def direction(parent, state):
    parent = parent.find("_")
    state = state.find("_")
    directions = {
        3: "D",
        1: "R",
        -1: "L",
        -3: "U" 
    }

    return directions[parent-state]


'''Find the shortest path to the goal state "_12345678" and
    returns the path by calling display_path() function to print all steps.
    You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):
    Q = [initial_state]
    explored = {}

    explored[initial_state] = 's' # Put init state in queue

    while Q:
        state = Q.pop(0) # Pop off current state
        
        if goal_test(state): # Check if we hit the goal
            return display_path(state, explored) # Show the path
        
        for neighbor in generate_children(state): # Add all the children to the queue
            if neighbor not in explored:
                Q.append(neighbor)
                explored[neighbor] = state # And make sure the children are explored

    return ("No solution")

def goal_test (state):
    return state == "_12345678"

'''Find the shortest path to the goal state "_12345678" and
    returns the path by calling display_path() function to print all steps.
    You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial): # Same exact code as BFS except pop() instead of pop(0)
    Q = [initial]
    explored = {}
    
    explored[initial] = 's'

    while Q:
        state = Q.pop()
        
        if goal_test(state):
            return display_path(state, explored)
        
        for neighbor in generate_children(state):
            if neighbor not in explored:
                Q.append(neighbor)
                explored[neighbor] = state

    return ("No solution")


def main():
    initial = getInitialState()
    print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print (BFS(initial))
    print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print (DFS(initial))

if __name__ == '__main__':
    main()
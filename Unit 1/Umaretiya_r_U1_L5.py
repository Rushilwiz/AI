# Name: Rushil Umaretiya     Date: 10/14/2020
import time, string

def generate_adjacents(current, words_set):
    ''' words_set is a set which has all words.
    By comparing current and words in the words_set,
    generate adjacents set of current and return it'''
    adj_set = set()
    
    for i in range(len(current)):
        for letter in string.ascii_lowercase:
            perm = current[:i]+letter+current[i+1:]
            if perm in words_set and perm != current:
                adj_set.add(perm)

    return adj_set

def check_adj(words_set):
    # This check method is written for words_6_longer.txt
    adj = generate_adjacents('listen', words_set)
    target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
    return (adj == target)

def bi_bfs(start, goal, words_set):
    '''The idea of bi-directional search is to run two simultaneous searches--
    one forward from the initial state and the other backward from the goal--
    hoping that the two searches meet in the middle. 
    '''
    if start == goal: return []

    Q = [[start],[goal]]
    visited = [{start:"s"},{goal:"s"}]

    flag = 0

    while Q[0] or Q[1]:
        flag = 1 - flag
        for i in range(len(Q[flag])):
            state = Q[flag].pop(0)
            adj_list = generate_adjacents(state, words_set)
            
            for adj in adj_list:
                if adj in visited[1 - flag]:
                    visited[flag][adj] = state
                    return build_path(visited, adj, start, goal)
            
            for neighbor in adj_list:
                if neighbor not in visited[flag]:
                    Q[flag].append(neighbor)
                    visited[flag][neighbor] = state

    return None

def build_path (visited, n, start, goal):
    start_path, goal_path, intersect = [], [], n

    while n != "s":
        goal_path.append(n)
        n = visited[1][n]

    n = intersect

    while n != "s":
        start_path.append(n)
        n = visited[0][n]

    return start_path[::-1] + goal_path[1:]

'''
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
'''


def main():
    filename = input("Type the word file: ")
    words_set = set()
    file = open(filename, "r")
    for word in file.readlines():
        words_set.add(word.rstrip('\n'))
    #print ("Check generate_adjacents():", check_adj(words_set))
    initial = input("Type the starting word: ")
    goal = input("Type the goal word: ")
    cur_time = time.time()
    path = (bi_bfs(initial, goal, words_set))
    if path != None:
        print (path)
        print ("The number of steps: ", len(path))
        print ("Duration: ", time.time() - cur_time)
    else:
        print ("There's no path")
 
if __name__ == '__main__':
    main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''
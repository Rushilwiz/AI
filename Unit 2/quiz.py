"""
def solve(board, col):
    if check_complete(board, col): return board
    for row in range(len(board)):
        if isValid(row,col,board):
            board[row][col] = 1
            result = solve(board, col+1)
            if result != None: return result
            board[row][col] = 0
    return None 


def check_complete(board, colNum):
    return len(board) == sum(map(sum,board))

def isValid(row,col,board):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for i, j in zip(range(row, -1,-1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board),1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def main():
    board = [[0 for i in range(8)] for j in range(8)]
    solution = solve(board,0)
    print(board)

if __name__ == "__main__":
    main()

"""

def check_complete(table, variables):
    total_vars = len(variables) + 2
    if len([i for i, x in enumerate(table) if x != ""]) != total_vars: return False
    distances, indicies = [], [i for i, x in enumerate(table) if x != ""]

    for i in range(len(indicies)):
        for j in range(i+1, len(indicies)):
            distances.append(abs(indicies[i]-indicies[j]))
    
    if len(set(distances)) != len(distances): return False
    else: return True

def isValid(table, index, current):
    distances, indicies = [], [i for i, x in enumerate(table) if x != ""]

    for i in range(len(indicies)):
        for j in range(i+1, len(indicies)):
            distances.append(abs(indicies[i]-indicies[j]))
    
    if len(set(distances)) != len(distances): return False
    else: return True


def search(table):
    table[0] = 'TA'
    # return backtrack(table, ['A','B','C','D'], 0)
    indicies = []
    for i in range(1, len(table)):
        copy = list(table)
        copy[i] = 'A'
        solution = backtrack(copy, ['B','C','D'], 0)
        if solution != None: indicies.append([i for i, x in enumerate(solution) if x != ""])
    distinct = set(tuple(x) for x in indicies)
    print(distinct)
    print(len(distinct), " distinct solutions")
    print()
    print()
    return indicies


def backtrack(table, variables, current):
    if check_complete(table, variables):
        return table
    for index in [i for i, x in enumerate(table) if x == ""]:
        if isValid(table, index, current):
            table[index] = variables[current]
            result = backtrack(table, variables, current+1)
            if result != None: return result
            table[index] = ""
    return None


def main():
    table = ['' for i in range(13)]
    solution = search(table)
    if solution != None:
        print(solution)
    else:
        print("sorry no solution and u failed the quiz")

if __name__ == "__main__":
    main()
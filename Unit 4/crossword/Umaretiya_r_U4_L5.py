import sys; args = sys.argv[1:]

# Name: Rushil Umaretiya
# Date: 3-18-2021

import re

BLOCKCHAR = '#'
OPENCHAR = '-'
PROTECTEDCHAR = '~'

def crossword(args):
    # parse input
    # args = ['13x13', '32', 'dct20k.txt', 'H1x4#Toe#', 'H9x2#', 'V3x6#', 'H10x0Scintillating', 'V0x5stirrup', 'H4x2##Ordained', 'V0x1Sums', 'V0x12Mah', 'V5x0pew']
    height, width, block_count, wordlist, words = parse_input(args)

    # initialize board
    board, width, height, block_count = initialize(width, height, words, block_count)

    print("init board:")
    display(board, width, height)

    # add blocking chars
    print("add blocks:")
    board = add_blocks(board, width, height, block_count)

    if board == None:
        print('Board is none.')
        raise Exception(f'Board is none.')

    # display(board, width, height)
    # remove border
    board, width, height = finish_board(board, width, height, words)

    #print(f'{block_count} {board.count(BLOCKCHAR)}')
    print(board.count(BLOCKCHAR))
    display(board, width, height)

def parse_input(args):
    tests = [r'^(\d+)x(\d+)$', r'^\d+$', r'^(H|V)(\d+)x(\d+)(.+)$']
    height, width, block_count, wordlist, words = 0, 0, 0, '', []

    for arg in args:
        # if os.path.isfile(arg):
        #     wordlist = arg
        # else:
        for i in range(len(tests)):
            match = re.search(tests[i], arg, re.I)
            if match == None: continue
            if i == 0:
                height = int(match.group(1))
                width = int(match.group(2))
            elif i == 1:
                block_count = int(match.group(0))
            elif i == 2:
                words.append((match.group(1).upper(), int(match.group(2)), int(match.group(3)), match.group(4).upper()))
    return height, width, block_count, wordlist, words

def initialize(width, height, words, block_count):
    board = OPENCHAR * height * width
    for word in words:
        index = word[1] * width + word[2]
        for letter in word[3]:
            new_char = BLOCKCHAR if letter == BLOCKCHAR else PROTECTEDCHAR
            board = board[:index] + new_char + board[index + 1 :]
            board = board[:(len(board) - 1) - index] + new_char + board[len(board) - index:]
            if word[0] == 'H':
                index += 1
            else:
                index += width
    block_count -= board.count(BLOCKCHAR)
    display(board, width, height)
    board = add_border(board, width, height)
    width += 2
    height += 2
    # display(board, width, height)
    board = protect(board, width, height)
    # display(board, width, height)
    return board, width, height, block_count

def protect(board, width, height):
    right_test = rf'({BLOCKCHAR}(\w|{PROTECTEDCHAR})(\w|{PROTECTEDCHAR})){OPENCHAR}'
    left_test = rf'{OPENCHAR}((\w|{PROTECTEDCHAR})(\w|{PROTECTEDCHAR}){BLOCKCHAR})'

    for i in range(2):
        board = re.sub(left_test, rf'{PROTECTEDCHAR}\1', board)
        board = re.sub(right_test, rf'\1{PROTECTEDCHAR}', board)
        board = transpose(board, width)
        width, height = height, width
        # display(board, width, height)
    
    return board

def transpose(board, width):
    return ''.join([board[col::width] for col in range(width)])

def add_border(board, width, height):
    border_board = BLOCKCHAR*(width+3)
    border_board +=(BLOCKCHAR*2).join([board[p:p+width] for p in range(0,len(board),width)])
    border_board += BLOCKCHAR*(width+3)
    return border_board

def remove_border(board, width, height):
    no_border = ''
    for i in range(len(board)):
        if (width <= i < width * (height - 1)) and ((i + 1) % width != 0) and (i % width != 0):
            no_border += board[i]
    return no_border, width - 2, height - 2

def blocking_heuristic(index, board, width):
    left = 0
    temp = index
    while board[temp] != BLOCKCHAR:
        left += 1
        temp += 1
    right = 0
    temp = index
    while board[temp] != BLOCKCHAR:
        right += 1
        temp -= 1
    up = 0
    temp = index
    while board[temp] != BLOCKCHAR:
        up += 1
        temp += width
    down = 0
    temp = index
    while board[temp] != BLOCKCHAR:
        down += 1
        temp -= width
    return up * down + left * right     

def add_blocks(board, width, height, block_count):
    if block_count == 0:
        return board

    if board.count(OPENCHAR) == block_count:
        return BLOCKCHAR * len(board)

    if block_count % 2 == 1:
        if width * height % 2 == 1:
            board = board[: len(board) // 2] + BLOCKCHAR + board[(len(board) // 2) + 1 :]
            block_count -= 1
        else:
            raise Exception("Cannot place an odd number of blockchars on an even sized board.")

    print(board)
    if re.search(f'#[{PROTECTEDCHAR+OPENCHAR}]{{1,2}}#', board) or re.search(f'#[{PROTECTEDCHAR+OPENCHAR}]{{1,2}}#', transpose(board, width)):
        
        display(board, width, height)

        for i in range(2):
            presub = board.count(BLOCKCHAR)
            board, num = re.subn(f'#([{PROTECTEDCHAR+OPENCHAR}][{PROTECTEDCHAR+OPENCHAR}]#)*', lambda x: '#' * len(x.group()), board)
            board, num = re.subn(f'#([{PROTECTEDCHAR+OPENCHAR}]#)*', lambda x: '#' * len(x.group()), board)
            block_count -= board.count(BLOCKCHAR) - presub
            
            board = transpose(board, width)
            width, height = height, width

        # print("yes.")
        display(board, width, height)
        # print("yes")
        possible = [i for i in range(len(board)) if board[i] != BLOCKCHAR]
        fills = {}

        for i in possible:
            fills[i] = area_fill(board, width, i)
      
        fill_counts = {}
        for fill in fills.keys():
            count = fills[fill].count('?')

            if count not in fill_counts.values():
                fill_counts[fill] = count
        
        fill_counts = {key: value for key, value in sorted(fill_counts.items(), key=lambda item: item[1])}
        for fill in fill_counts:
            if fill_counts[fill] < (width - 2) * (height - 2) - (board.count(PROTECTEDCHAR) + board.count(OPENCHAR)):
                board = area_fill(board, width, fill, char=BLOCKCHAR)
                board = area_fill(board, width, len(board) - 1 - fill, char=BLOCKCHAR)
                block_count -= fill_counts[fill] * 2
                break
    
    options = [i for i in range(len(board)) if board[i] == board[(len(board) - 1) - i] == OPENCHAR]
    return blocks_backtrack(board, width, height, block_count, options)

def blocks_backtrack(board, width, height, block_count, options):
    # print(options)
    # display(board, width, height)

    if block_count == 0 or len(options) == 0:
        return board
    
    for option in sorted(options, key=lambda i: blocking_heuristic(i, board, width)):
        if is_valid_blocking(board, width, height, option):
            copy = board[:option] + BLOCKCHAR + board[option + 1 :]
            copy = copy[: (len(copy) - 1) - option] + BLOCKCHAR + copy[len(copy) - option :]
            updated_options = [i for i in options if i != option]
            result = blocks_backtrack(copy, width, height, block_count - 2, updated_options)
            if result != None: return result

    return None

def is_valid_blocking(board, width, height, option):
    if board[option] != OPENCHAR: return False
    temp = board[:option] + BLOCKCHAR + board[option + 1:]
    temp = temp[:(len(temp) - 1) - option] + BLOCKCHAR + temp[len(temp) - option :]

    illegalRegex = rf"[{BLOCKCHAR}](.?({PROTECTEDCHAR}|{OPENCHAR})|({PROTECTEDCHAR}|{OPENCHAR}).?)[{BLOCKCHAR}]"
    if re.search(illegalRegex, temp) != None: return False
    if re.search(illegalRegex, transpose(temp, width)) != None: return False
    return True

def area_fill(board, width, sp, char='?'):
    dirs = [-1, width, 1, -1 * width] 
    if sp < 0 or sp >= len(board): return board
    if board[sp] in (OPENCHAR, PROTECTEDCHAR):
        board = board[0:sp] + char + board[sp+1:]
        for d in dirs:
            if d == -1 and sp % width == 0: continue
            if d == 1 and sp + 1 % width == 0: continue
            board = area_fill(board, width, sp + d, char)
    return board

def finish_board(board, width, height, words):
    # remove border
    board, width, height = remove_border(board, width, height)
    
    # add words
    for word in words:
        index = word[1] * width + word[2]
        for letter in word[3]:
            board = board[:index] + letter + board[index + 1 :]
            if word[0] == 'H':
                index += 1
            else:
                index += width

    # replace protected with open
    board = re.sub(PROTECTEDCHAR, OPENCHAR, board)

    return board, width, height

def display(board, width, height):
    for i in range(height):
        line = ""
        for letter in range(width):
            line += (board[(i * width) + letter] + " ")
        print(line)
    print()

def main():
    crossword(args)

if __name__ == '__main__':
    main()
import sys; args = sys.argv[1:]  #gets rid of the .py from the list, not needed to look at
import re
BLOCKCHAR = "#"  # blocked square (black square)
OPENCHAR = "-"  # open square (not decided yet)
PROTECTEDCHAR = "~"  #protected

def initialize(height, width, words ,numBlocks):
    xword = OPENCHAR * (int(height) * int(width))
    for word in words:
        startingIndex = int(int(word[1]) * width + int(word[2]))
        for letter in word[3]:
            xword = xword[:startingIndex] + letter + xword[startingIndex + 1:]
            if letter == BLOCKCHAR:
                numBlocks -= 1
            if word[0] == "V":
                startingIndex += int(width)
            else:
                startingIndex += 1
    return xword, numBlocks

def initialProtSymmetry(board):
    length = len(board)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
    for x in range(length):
        temp = x + 1
        if board[x] != OPENCHAR and board[x] != PROTECTEDCHAR and board[x] in alphabet:
            indexToReplace = length - temp + 1
            if board[indexToReplace-1] not in alphabet:
                board = board[:indexToReplace -1] + PROTECTEDCHAR + board[indexToReplace:]
    if length % 2 != 0:
        indexToReplace = (length // 2) + 1
        board = board[:indexToReplace -1] + PROTECTEDCHAR + board[indexToReplace:]
    return board

def horizontalProt(board, height, width):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for y in range(height):
        letterCount = 0
        #for x in range(width):
         #   if board[(y * height) + x] in alphabet:
          #      letterCount += 1
           # else:
            #    break
        #if letterCount < 3 and letterCount > 0:
         #   for x in range(3):
          #      if board[(y * height) + x] == OPENCHAR:
           #         board = board[:(y * height) + x] + PROTECTEDCHAR + board[(y * height) + x + 1:]
        for x in range(width):
            #print(y*width+x,board[y*width+x])
            if board[(y * width) + x] in alphabet or (board[(y*width)+x] == PROTECTEDCHAR and board[(y*width)+x-1] != PROTECTEDCHAR):
                letterCount += 1
            else:
                
                if letterCount < 3 and letterCount > 0 and x+1 < width:
                    for z in range(3-letterCount):
                        if board[(y * width) + x + z] == OPENCHAR:
                            board = board[:(y * width) + x + z] + PROTECTEDCHAR + board[(y * width) + x + z + 1:]  
                letterCount = 0  
    return board

def verticalProt(board, height, width):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(width):
        letterCount = 0
        for y in range(height):
            if board[(y * height) + x] in alphabet:
                letterCount += 1
            else:
                break
        if letterCount < 3 and letterCount > 0:
            for y in range(3):
                if board[(y * height) + x] == OPENCHAR:
                    board = board[:(y * height) + x] + PROTECTEDCHAR + board[(y * height) + x + 1:]
    return board

def symmetricalProt(board):
    length = len(board)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
    for x in range(length):
        temp = x + 1
        if board[x] == PROTECTEDCHAR and (board[length - temp] not in alphabet):
            indexToReplace = length - temp + 1
            board = board[:indexToReplace -1] + PROTECTEDCHAR + board[indexToReplace:]
    return board

def addBlocks(board, height, width, numBlocks):
    pos_list = [x for x in range(len(board)) if board[x] == OPENCHAR and board[len(board)-x-1] == OPENCHAR]
    return recursiveBacktrack(board,height,width,numBlocks, pos_list)

def recursiveBacktrack(board,height,width,numBlocks, pos_list):
    if len(pos_list) == 0 or numBlocks == 0: return board
    for option in pos_list:
        pos_list.remove(option)
        if isValid(board,option,height,width):
            newBoard = board[:option] + BLOCKCHAR + board[option+1:]
            newBoard = newBoard[:len(board)-option-1] + BLOCKCHAR + newBoard[len(board)-option:height*width]
            result = recursiveBacktrack(newBoard,height,width,numBlocks-2, pos_list)
            if result!= None:
                return result
            board = board[:option] + OPENCHAR + board[option+1:]
            board = board[:len(board)-option-1] + OPENCHAR + board[len(board)-option:]
            pos_list.insert(0, option)
            numBlocks += 2
    return None

def transpose(board, newWidth):
    return "".join([board[col:newWidth] for col in range(newWidth)])

def isValid(board,index,height,width):
    #checks if block can go there
    #ALSO KEEP IN MIND IT HAS TO BE SYMMETRIC
    if board[index] != OPENCHAR:
        return False
    tempBoard = board[:index] + BLOCKCHAR + board[index+1:]
    illegalRegex = "[{}](.?({}|{})|({}|{}).?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR,OPENCHAR, PROTECTEDCHAR,OPENCHAR, BLOCKCHAR)
    if re.search(illegalRegex, tempBoard) != None or re.search(illegalRegex, transpose(tempBoard, height)) != None:
        return False
    else:
        if board[len(tempBoard)-index-1] != OPENCHAR:
            return False
        tempBoard = tempBoard[:len(tempBoard)-index-1] + BLOCKCHAR + tempBoard[len(tempBoard)-index:]
        if re.search(illegalRegex, tempBoard) != None or re.search(illegalRegex, transpose(tempBoard, height)) != None:
            return False
    return True

def selectSpot(board,blockOptions,height,width):
    for option in blockOptions:
        if isValid(board,option,height,width):
            return option
    return -1

def subLettersForProctected(board):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index in range(len(board)):
        if board[index] in alphabet:
            board = board[:index] + PROTECTEDCHAR + board[index+1:]    
    return board

def display(board, height, width):
    startInd = 0
    for y in range(height):
        print(board[startInd:startInd + width])
        startInd = startInd + width

def processInput(args):
    dimmMatch = r"^(\d+)x(\d+)$"
    blockMatch = r"^\d+$"
    wordMatch = r"^(H|V)(\d+)x(\d+)(.+)$"
    height, width = 0, 0
    numBlocks = 0
    prePlacedWords = []
    for input in args:
        if re.match(dimmMatch, input) != None:
            indexOfX = input.index("x")
            height, width = int(input[:indexOfX]), int(input[indexOfX + 1:])
            args.remove(input)
            break
    for input in args:
        if re.match(blockMatch, input) != None:
            numBlocks = int(input)
            args.remove(input)
            break
    unprocessWords = []
    for input in args:
        if re.match(wordMatch, input, re.I) != None:
            unprocessWords.append(input)
    for word in unprocessWords:
        args.remove(word)
        orient = word[0].upper()
        word = word[1:]
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if "x" in word:
            indexOfX = word.index("x")
        else:
            indexOfX = word.index("X")
        finalIndex = indexOfX + 1
        row = word[:indexOfX]
        while word[finalIndex] in digits:
            finalIndex += 1
        col = word[indexOfX + 1:finalIndex]
        restOfWord = word[finalIndex:]
        prePlacedWords.append((orient, row, col, restOfWord.upper()))
    if len(args) > 0:
        file = args[0]
    return file,height, width, numBlocks, prePlacedWords

def removeOuter(board,height,width):
    toReturn = ""
    for i in range(len(board)):
        if (i > width) and ((i+1) % width != 0) and (i % width != 0) and (height*width-width > i):
            toReturn += board[i]
    return toReturn 

def finalize(xword, xw):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    toReturn = ""
    for i in range(len(xword)):
        if xword[i] in alphabet or xword[i] == BLOCKCHAR:
            toReturn += xword[i]
        elif xword[i] == PROTECTEDCHAR:
            toReturn += OPENCHAR
        elif xw[i] == BLOCKCHAR:
            toReturn += BLOCKCHAR
        else:
            toReturn += OPENCHAR
    return toReturn

def inputtedBlocksSym(board, numBlocks):
    length = len(board)
    for i in range(length):
        if board[i] == BLOCKCHAR and board[len(board)-i-1] != BLOCKCHAR:
            temp = i + 1
            indexToReplace = length - temp + 1
            board = board[:indexToReplace -1] + BLOCKCHAR + board[indexToReplace:]
            numBlocks -=1
    return board, numBlocks
def main():
    #USE ONLY THE BELOW LINE IN VSCODE, IF USING JGRASP COMMENT THE BELOW LINE!!!!!!!!!!!!!!!!!!!
    #COMMENT BELOW LINE OUT WHEN SUBMITTING!!!!!!!!!!!
    #GOOD RUNS:
    #sys.argv = ['Scavotto_z_U4_L4.py',"scrabble.txt","3x3","9"]
    #sys.argv =  ['Scavotto_z_U4_L4.py', "7x7", "6", "scrabble.txt", "v0x0come", "v0x1here", "h0x2ers"]
    #sys.argv = ['Scavotto_z_U4_L4.py', "9x13", "18", "xwords.txt", "V0x1Who"]
    #sys.argv = ['Scavotto_z_U4_L4.py',"9x9", "14", "xwords.txt", "V0x4con", "V6x4rum"]
    #NEED FIX
    #sys.argv = ['Scavotto_z_U4_L4.py',"15x15", "32", "dct20k.txt", "H0x0Mute", "V0x0mule", "V10x13Risen", "H7x5#", "V3x4#", "H6x7#", "V11x3#"]
    #sys.argv = ['Scavotto_z_U4_L4.py', "10x14", "32", "dct20k.txt", "V6x0#", "V9x3#", "H3x10#", "V0x6Indulgence"]
    #13x13 32 dct20k.txt H1x4#Toe# H9x2# V3x6# H10x0Scintillating V0x5stirrup H4x2##Ordained V0x1Pits V0x12Ffi V5x0orb
    #13x13 32 dct20k.txt V2x4# V1x9# V3x2# h8x2#moo# v5x5#two# h6x4#ten# v3x7#own# h4x6#orb# H12x4Vlan
    #13x13 25 dct20k.txt H6x4no#on v5x5rot v0x0ankles h0x4Trot H0x9Calf V0x12foot
    #9x22 36 dct20k.txt h4x8e# h3x5s# h2x5# v2x0pan V5x1#w V8x18c
    #args = sys.argv  #gets the sys args
    #args = args[1:]
    #COMMENT ALL ABOVE TO SUBMIT
    filetext,height, width, numBlocks, words = processInput(args)  #processes the inputs
    if numBlocks == height*width:
      xword = BLOCKCHAR * numBlocks
      display(xword, height,width)
    else:
      xword, numBlocks = initialize(height, width, words, numBlocks)
      display(xword, height, width)
      if numBlocks != 0:
        print("\nMaking Any Inputted Blocks Symmetrical")
        xword, numBlocks = inputtedBlocksSym(xword, numBlocks)
        display(xword, height, width)
        print("\nAdding Symmetrical Protected Characters")
        xword = initialProtSymmetry(xword)
        display(xword, height, width)
        print("\nHorizontal Protection")
        xword = horizontalProt(xword, height, width)
        display(xword, height, width)
        print("\nVertical Protection")
        xword = verticalProt(xword, height, width)
        display(xword, height, width)
        print("\nMaking Protection Symmetric")
        xword = symmetricalProt(xword)
        display(xword, height, width)
        xw = BLOCKCHAR*(width+3)
        xw +=(BLOCKCHAR*2).join([xword[p:p+width] for p in range(0,len(xword),width)])
        xw += BLOCKCHAR*(width+3)
        print("\nTurning into xw")
        xwHeight = height+2
        xwWidth = width+2 
        display(xw,xwHeight,xwWidth)
        print("\nSubbing Letters")
        subbedXW = subLettersForProctected(xw)
        display(subbedXW, xwHeight, xwWidth)
        print("\nAdding Blocks")
        xw = addBlocks(subbedXW, xwHeight, xwWidth, numBlocks)
        display(xw,xwHeight,xwWidth)
        print("\nRemoving Outer Border")
        xw = removeOuter(xw, xwHeight,xwWidth)
        display(xw, height, width)
        print("\nPutting in Letters and Replacing Protected With Open\n")    
        xword = finalize(xword, xw)
        print(xword)
        print("\nThe Displayed Board:")
        display(xword, height, width)
if __name__ == '__main__': main()
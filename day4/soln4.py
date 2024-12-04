def checkForward(x,y,puzzle):
    if y + 4 > len(puzzle[0]):
        return 0
    if puzzle[x][y:y+4] == "XMAS":
        return 1
    return 0

def checkBackward(x,y,puzzle):
    if y - 3 < 0:
        return 0
    if puzzle[x][y-3:y+1] == "SAMX":
        return 1
    return 0

def checkUp(x,y,puzzle):
    if x - 3 < 0:
        return 0
    targ = ""
    for i in range(x,x-4,-1):
        targ += puzzle[i][y]
    if targ == "XMAS":
        return 1
    return 0

def checkDown(x,y,puzzle):
    if x + 4 > len(puzzle):
        return 0
    
    targ = ""
    for i in range(x,x+4):
        targ += puzzle[i][y]
    if targ == "XMAS":
        return 1
    return 0

def checkDiagDownRight(x,y,puzzle):
    if x + 4 > len(puzzle):
        return 0
    if y + 4 > len(puzzle[0]):
        return 0
    
    targ = ""
    for i in range(y,y+4):
        targ += puzzle[x+i-y][i]
    if targ == "XMAS":
        return 1
    return 0

def checkDiagUpRight(x,y,puzzle):
    if x - 3 < 0:
        return 0
    if y + 4 > len(puzzle[0]):
        return 0
    
    targ = ""
    for i in range(y,y+4):
        targ += puzzle[x-i+y][i]
    if targ == "XMAS":
        return 1
    return 0

def checkDiagDownLeft(x,y,puzzle):
    if x + 4 > len(puzzle):
        return 0
    if y - 3 < 0:
        return 0
    
    targ = ""
    for i in range(x,x+4):
        targ += puzzle[i][y-i+x]
    if targ == "XMAS":
        return 1
    return 0

def checkDiagUpLeft(x,y,puzzle):
    if x - 3 < 0:
        return 0
    if y - 3 < 0:
        return 0
    
    targ = ""
    for i in range(y,y-4,-1):
        targ += puzzle[x+i-y][i]
    if targ == "XMAS":
        return 1
    return 0

def checkCrossLeft(x,y,puzzle):
    if x - 1 < 0:
        return 0
    if y - 1 < 0:
        return 0
    if x + 1 == len(puzzle):
        return 0
    if y + 1 == len(puzzle[0]):
        return 0
    
    if puzzle[x-1][y-1] == "M" and puzzle[x+1][y-1] == "M" and puzzle[x-1][y+1] == "S" and puzzle[x+1][y+1] == "S":
        return 1
    return 0

def checkCrossDown(x,y,puzzle):
    if x - 1 < 0:
        return 0
    if y - 1 < 0:
        return 0
    if x + 1 == len(puzzle):
        return 0
    if y + 1 == len(puzzle[0]):
        return 0
    
    if puzzle[x-1][y-1] == "S" and puzzle[x+1][y-1] == "M" and puzzle[x-1][y+1] == "S" and puzzle[x+1][y+1] == "M":
        return 1
    return 0

def checkCrossRight(x,y,puzzle):
    if x - 1 < 0:
        return 0
    if y - 1 < 0:
        return 0
    if x + 1 == len(puzzle):
        return 0
    if y + 1 == len(puzzle[0]):
        return 0
    
    if puzzle[x-1][y-1] == "S" and puzzle[x+1][y-1] == "S" and puzzle[x-1][y+1] == "M" and puzzle[x+1][y+1] == "M":
        return 1
    return 0

def checkCrossUp(x,y,puzzle):
    if x - 1 < 0:
        return 0
    if y - 1 < 0:
        return 0
    if x + 1 == len(puzzle):
        return 0
    if y + 1 == len(puzzle[0]):
        return 0
    
    if puzzle[x-1][y-1] == "M" and puzzle[x+1][y-1] == "S" and puzzle[x-1][y+1] == "M" and puzzle[x+1][y+1] == "S":
        return 1
    return 0


def checkXmas(x,y,puzzle):
    number = 0
    number += checkForward(x, y, puzzle)
    number += checkBackward(x, y, puzzle)
    number += checkUp(x, y, puzzle)
    number += checkDown(x, y, puzzle)
    number += checkDiagDownRight(x, y, puzzle)
    number += checkDiagUpRight(x, y, puzzle)
    number += checkDiagDownLeft(x, y, puzzle)
    number += checkDiagUpLeft(x, y, puzzle)
    return number

def checkCross(x,y,puzzle):
    number = 0
    number += checkCrossLeft(x,y,puzzle)
    number += checkCrossDown(x,y,puzzle)
    number += checkCrossRight(x,y,puzzle)
    number += checkCrossUp(x,y,puzzle)
    return number

puzzle = []
with open("inputd4.txt", "r") as f:
    for line in f:
        puzzle.append(line.rstrip())

xmas = 0
cross = 0
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j] == "X":
            xmas += checkXmas(i,j,puzzle)
        if puzzle[i][j] == "A":
            cross += checkCross(i,j,puzzle)

print(xmas)
print(cross)
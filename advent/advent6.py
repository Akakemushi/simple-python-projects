# I placed 4657 out of ??
import time, copy, csv
rawMap = '''.....#......................................................#...................#.........................................#..#....
.......................#.......#...............................................#.................#...#.......#..............#.....
.........#.................................................................#.....................##...............................
.....#..#.............#.......................#..#....#............#.............................................#................
............#................##............................................#.##..................#.................#.....#...#....
....................................................................#..#.................#.....#................#....#.....#......
.#.........##.................##................#..............................................#..................................
...................#..................#.......#......#......................#..#...................#.........#...............#.#..
.......................#.#.........#...............#....................#........#.............#..................................
......#...........#........................................#........#.........#...............#.#.........#.......................
...#...........................................................#...........#............................#.........................
...........#............................#.#........#...#........#........................................................#........
.........#................................................#...#..#........#............#................#.........................
..#.....................................................................#...............#.........#....#.......#..................
.......................#....#..#............#.........#.............#...................##....................................#...
..................#...................................................................#.....................#...................#.
............................#..........................#.....#...........##.......................................................
........................#.............................#...............#..............................#.........................#..
.....................#..........#...#.....#....#..............#...........................................#...............#.#.....
...................................#.................................#......#..................#..................................
.#.....#.......##......#..................#...............................................#.........................#.........#...
.................#...............#..............................#............................................#......#.............
...#.........#................#...#....................#......................#.#......#.............#............................
.............#..........##....#...#................#.............#.............#............................................#.....
.....#............................................................................................................#...............
........................#..........................##........#........................................#........#..................
..........................#.....##.#.............#.........#..............................#..............................#........
..............#.....................#...............................................#..................................#..........
...#................................................#.........#.....................#..........................................#..
.##..............#..........#......................................................................#.........#........#.........#.
...##.#.....#........#..........................#.............................#..........#.#..#...................................
..................................#...#......#......#................#..#.....................................#...#...............
.........................................................................................#..................#......#..............
.................#....................#..#....#..............................#........##...#.......#...............#..............
...#.................#................#..................................#..................##....##.....#............#...........
..........#...#....................##......................#.....#...........#......#......#.............##....#...#........#.#...
............................#......#.........#..............................................................#........#............
.........................................#.........................................................#...............#.............#
.....#..........#..#........#................................................................................##......#............
.#................#.....................................................................................#.....#...................
..............#........#..................................#..............................##.......................................
........................#.....................#..............................#..................#.............................#.##
#...........................................................#..##........#........................................................
..............#...............#.........#...........^.....................................................#...#.........##..#.....
......................................................#.......................................#..............#...............#....
...#....#..................#....#.......................#.#..........#.......#.................#................................#.
#.........................................................................................................#.......................
..........................#......................................................................#.............#..................
................#...............................................................#........#........................................
..........#............#...............#.#........................................................................................
....#.....#............#.....##.........#......##.................#.......#................#...............................#...#..
................................................................................#...#.......................................#.....
.#........................................#.................................................................#.#...................
.......#....#...................................................................................#...........#..#.............#....
...#...#...............................................................................................................#..........
..#....................................#......#.................#.........................................................#.......
...........................................#......#.........#.##........##..#.........#..........................#....##.#....#...
.........................#...............#............................................................................#...........
................................................#................#..................#..#...........#.......................#.....#
..........................................................#..........#........................................#...................
..................#...................#................##.........#...........................#...................................
............................#.................................................................#...........#.#.....................
................#.......................#.........................................................................#....#..........
#..........#..............#.#............................................................................................#........
..........................................................................................#.......#.........................#....#
...........................................#.......#................................................................#...#.........
..#...................#........................................#..............#.......................#...........................
.......................#..............................#...........................#......#......................#........#........
.....#................................................................................#....#......................................
..#..................................#.........#....#............#....#..............#.............#......#.........#......#....#.
.......##.................................................................................................#.#....#................
............................................#.....#...................#...........#.........#.....................................
...............#.........................................#.............................#.........................#............#...
..............................................##..................................................#........................#......
..................................................................................................#.................#............#
......................#.......................#.........#......................................................................#..
..#...........................#...........................................................................#.....#........#........
..........#....................#...........................##................................................................#....
.........#........#...........................................#........##.........................................................
....#.............................#....................#.................#..........................#........................#....
.......................................#...#....#...............................................#.................................
............#............................................#..............................#..........#......#.......................
.#..............................#...........#........#...............................#.#......#..................................#
#................#..#.............................................................................................................
................................#................#............#....#.#..................##.....................#...............#.#
#....##................#...........#....#..#..........#.....................#..........................#.....................#....
............................................................................................#.....................................
.......................#................................................##..................................#.....................
....#.....#..#................................................................................................##..................
..........................#......#...#...#..........#...#................#.................................................#......
............................#....#.#.......#..........#............................................#..............................
......#...........#......................#..#.....................................................................................
.........................................#...................................................##...............#............#...##.
...................................#.#............................................................................................
......................#........##..................................................#..............................................
...................#......................................................#......#.............................#...........#......
......#................#................................................................................#..................#......
..#.........................#.....#..............#.........#...................#.......................................#..........
..................#..............................................#......#.#.......................................................
...........#.....................................................................#.......................#........................
.......#.........###.....................#........................................................................................
...............#...#..........#........................#....................#......#............#..................#..............
.............#.......#.............#....................................................#.....................................#...
.............................................................................#.#...............................#..#...............
.........##..........#..#.#.................................................................................#................#....
.#..................#.....................................#...................#.#..............#...........................#......
........#.....#...........................#..........................#.............................#...............#..............
#.........#.#.......................................................................................................#.............
..#...................................................................#............#...#.........#................................
..................#......#........#...........#......................#........#..#.......................................#...#..#.
.......................................................#.............#...........#............................#............#......
..............................................#....................................................................#..............
.............#....................#.......................#.............#..........#.........#.............#....#.......#.....#...
...#...................#...............#........#.............#.................#..........#........#................#............
...........#...............#.....................#.................................................#...#.....#.....#..............
....#......................................#......#..............................#...........#.....#..................#...........
#.........#...................#.........#............#............#..............#..........#...........#...#.#..##...............
...........................................................#..................#......#..................#...............#.........
...........#.......................#.........................................................#.......#..............#..........#..
.................................#.....#.....#..............................#..........#..............#............#..............
...............#.......................................................................##.........#...........................#...
....#...............#.........#.#...........#.......#.#..#....#...................................................................
.........#.............................................#.......................................................#..........##......
......................................#...............#.......#..#..#.#...................#....................#.#................
.................#..................................................................#..........................#.....#......#.#...
..#...........#..................#..............#.....#......#.................#..............##.......#...#.......#.......#......
......................................#.....................#..........#............................................##.#..........
#......#................#........................................................#....#....##..................#.................#
............##..............##..........#........##.....................................#..........#..............................
.#.##............#.................#...................#....#...#...............................................#.................'''

rawMiniMap = '''.....#...#
#...#.....
......#..#
#.#.......
..........
......#...
..#....#..
....^...#.
.#.#..#...
.....#....'''

# miniMapStrings = rawMiniMap.split("\n")
# miniMap = []
# for string1 in miniMapStrings:
#     array = list(string1)
#     miniMap.append(array)
# miniWidth = len(miniMap[0])
# miniHeight = len(miniMap)

mapStrings = rawMap.split("\n")
map = []
for string in mapStrings:
    array = list(string)
    map.append(array)
width = len(map[0])
height = len(map)
spacesWalked = 1

def getPosition(matrix):
    for y, row in enumerate(matrix):
        for x, space in enumerate(row):
            if space in "^<>v":
                facing = space
                return [facing, x, y]

def getLocation(matrix):
    for y, row in enumerate(matrix):
        for x, space in enumerate(row):
            if space == "O":
                return [x, y]

def validateCoords(x, y):
    if x >= 0 and x <= width - 1:
        if y >= 0 and y <= height - 1:
            return True
        else:
            return False
    else:
        return False

file = open('path.csv')
fileReader = csv.reader(file)
guardPath = list(fileReader)

def walk(dir, x, y):
    global map
    global spacesWalked
    if dir == "^":
        if validateCoords(x, y - 1): # you can continue
            if map[y - 1][x] != "#": # there's nothing blocking your path
                if map[y - 1][x] == ".": #there's a new space in front of you
                    map[y][x] = "X" # mark the space you came from as walked
                    spacesWalked += 1 # increment the total spaces
                    map[y - 1][x] = "^" # set the guard's new position and direction.
                    outputWriter.writerow([x, y - 1])
                    return "Continue"
                else: # this is somewhere you've already walked, so don't increment.
                    map[y][x] = "X" # mark that space as walked again.
                    map[y - 1][x] = "^" # set the guard's new position and direction.
                    return "Continue"
            else: # you're about to hit a crate
                map[y][x] = ">" # just rotate yourself.
                return "Continue"
        else: # its the edge of the map and this is the last step
            map[y][x] = "X"
            return "Done"
    if dir == ">":
        if validateCoords(x + 1, y): # you can continue
            if map[y][x + 1] != "#": # there's nothing blocking your path
                if map[y][x + 1] == ".": #there's a new space in front of you
                    map[y][x] = "X" # mark the space you came from as walked
                    spacesWalked += 1 # increment the total spaces
                    map[y][x + 1] = ">" # set the guard's new position and direction.
                    outputWriter.writerow([x + 1, y])
                    return "Continue"
                else: # this is somewhere you've already walked, so don't increment.
                    map[y][x] = "X" # mark that space as walked again.
                    map[y][x + 1] = ">" # set the guard's new position and direction.
                    return "Continue"
            else: # you're about to hit a crate
                map[y][x] = "v" # just rotate yourself.
                return "Continue"
        else: # its the edge of the map and this is the last step
            map[y][x] = "X"
            return "Done"
    if dir == "v":
        if validateCoords(x, y + 1): # you can continue
            if map[y + 1][x] != "#": # there's nothing blocking your path
                if map[y + 1][x] == ".": #there's a new space in front of you
                    map[y][x] = "X" # mark the space you came from as walked
                    spacesWalked += 1 # increment the total spaces
                    map[y + 1][x] = "v" # set the guard's new position and direction.
                    outputWriter.writerow([x, y + 1])
                    return "Continue"
                else: # this is somewhere you've already walked, so don't increment.
                    map[y][x] = "X" # mark that space as walked again.
                    map[y + 1][x] = "v" # set the guard's new position and direction.
                    return "Continue"
            else: # you're about to hit a crate
                map[y][x] = "<" # just rotate yourself.
                return "Continue"
        else: # its the edge of the map and this is the last step
            map[y][x] = "X"
            return "Done"
    if dir == "<":
        if validateCoords(x - 1, y): # you can continue
            if map[y][x - 1] != "#": # there's nothing blocking your path
                if map[y][x - 1] == ".": #there's a new space in front of you
                    map[y][x] = "X" # mark the space you came from as walked
                    spacesWalked += 1 # increment the total spaces
                    map[y][x - 1] = "<" # set the guard's new position and direction.
                    outputWriter.writerow([x - 1, y])
                    return "Continue"
                else: # this is somewhere you've already walked, so don't increment.
                    map[y][x] = "X" # mark that space as walked again.
                    map[y][x - 1] = "<" # set the guard's new position and direction.
                    return "Continue"
            else: # you're about to hit a crate
                map[y][x] = "^" # just rotate yourself.
                return "Continue"
        else: # its the edge of the map and this is the last step
            map[y][x] = "X"
            return "Done"




def loopWalk(dir, x, y, miniMap):
    if dir == "^":
        if validateCoords(x, y - 1): # you can continue
            if miniMap[y - 1][x] != "#": # there's nothing blocking your path
                if miniMap[y - 1][x] == ".": #there's a new space in front of you
                    miniMap[y][x] = "^" # mark the space you came from as walked
                    miniMap[y - 1][x] = "O" # set the guard's new position and direction.
                    return ["Continue", "^", miniMap]
                elif miniMap[y - 1][x] == "^":
                    return ["Loop", "^", miniMap]
                else:
                    miniMap[y][x] = "^" # mark that space as walked.
                    miniMap[y - 1][x] = "O" # set the guard's new position and direction.
                    return ["Continue", "^", miniMap]
            else: # you're about to hit a crate
                miniMap[y][x] = "O" # just rotate yourself.
                return ["Continue", ">", miniMap]
        else: # its the edge of the miniMap and this is the last step
            miniMap[y][x] = "^"
            return ["Done", "^", miniMap]
    if dir == ">":
        if validateCoords(x + 1, y): # you can continue
            if miniMap[y][x + 1] != "#": # there's nothing blocking your path
                if miniMap[y][x + 1] == ".": #there's a new space in front of you
                    miniMap[y][x] = ">" # mark the space you came from as walked
                    miniMap[y][x + 1] = "O" # set the guard's new position and direction.
                    return ["Continue", ">", miniMap]
                elif miniMap[y][x + 1] == ">":
                    return ["Loop", ">", miniMap]
                else: # this is somewhere you've already walked, so don't increment.
                    miniMap[y][x] = ">" # mark that space as walked again.
                    miniMap[y][x + 1] = "O" # set the guard's new position and direction.
                    return ["Continue", ">", miniMap]
            else: # you're about to hit a crate
                miniMap[y][x] = "O" # just rotate yourself.
                return ["Continue", "v", miniMap]
        else: # its the edge of the miniMap and this is the last step
            miniMap[y][x] = ">"
            return ["Done", ">", miniMap]
    if dir == "v":
        if validateCoords(x, y + 1): # you can continue
            if miniMap[y + 1][x] != "#": # there's nothing blocking your path
                if miniMap[y + 1][x] == ".": #there's a new space in front of you
                    miniMap[y][x] = "v" # mark the space you came from as walked
                    miniMap[y + 1][x] = "O" # set the guard's new position and direction.
                    return ["Continue", "v", miniMap]
                elif miniMap[y + 1][x] == "v":
                    return ["Loop", "v", miniMap]
                else: # this is somewhere you've already walked, so don't increment.
                    miniMap[y][x] = "v" # mark that space as walked again.
                    miniMap[y + 1][x] = "O" # set the guard's new position and direction.
                    return ["Continue", "v", miniMap]
            else: # you're about to hit a crate
                miniMap[y][x] = "O" # just rotate yourself.
                return ["Continue", "<", miniMap]
        else: # its the edge of the miniMap and this is the last step
            miniMap[y][x] = "v"
            return ["Done", "v", miniMap]
    if dir == "<":
        if validateCoords(x - 1, y): # you can continue
            if miniMap[y][x - 1] != "#": # there's nothing blocking your path
                if miniMap[y][x - 1] == ".": #there's a new space in front of you
                    miniMap[y][x] = "<" # mark the space you came from as walked
                    miniMap[y][x - 1] = "O" # set the guard's new position and direction.
                    return ["Continue", "<", miniMap]
                elif miniMap[y][x - 1] == "<":
                    return ["Loop", "<", miniMap]
                else: # this is somewhere you've already walked, so don't increment.
                    miniMap[y][x] = "<" # mark that space as walked again.
                    miniMap[y][x - 1] = "O" # set the guard's new position and direction.
                    return ["Continue", "<", miniMap]
            else: # you're about to hit a crate
                miniMap[y][x] = "O" # just rotate yourself.
                return ["Continue", "^", miniMap]
        else: # its the edge of the miniMap and this is the last step
            miniMap[y][x] = "<"
            return ["Done", "<", miniMap]


# gameStatus = "Continue"
# while gameStatus == "Continue":
#     guard = getPosition(map)
#     gameStatus = walk(guard[0], guard[1], guard[2])
# print(spacesWalked)


loopCount = 0
rowCount = 0
for coordPair in guardPath:
    square = map[int(coordPair[1])][int(coordPair[0])]
    if square == ".":
        initialize = getPosition(map)
        direction = initialize[0]
        location = [initialize[1], initialize[2]]
        mapCopy = copy.deepcopy(map)
        mapCopy[int(coordPair[1])][int(coordPair[0])] = "#"
        loopStatus = ["Continue", direction, mapCopy]
        while loopStatus[0] == "Continue":
            loopStatus = loopWalk(direction, location[0], location[1], loopStatus[2])
            direction = loopStatus[1]
            location = getLocation(loopStatus[2])
        if loopStatus[0] == "Loop":
            loopCount += 1
        mapCopy[int(coordPair[1])][int(coordPair[0])] = "."
        del mapCopy
        print("Checking row #" + str(rowCount) + "  Loops found: " + str(loopCount))
        rowCount += 1

print(loopCount)
file.close()
# 26 loops found as of row 434, then stuck
# 95 loops found as of row 571, then stuck

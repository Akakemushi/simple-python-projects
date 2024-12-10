import copy
rawMap = '''.....................U.........w..................
l.................................................
...........o.a................U...w...............
............................................W.....
..........T....................s.............7....
.............................................W....
.........T..............4....n.d.H.........5......
......T.....oj...U.....n...w......H...........z...
.G..x..........................E.....V..H.........
.........a....................d....s.......7w.....
...j....r.............o.............V.......d...W.
.......r..J.Goa.U...............n................z
.........Jj.........M..........Pv.................
...J...........t..3..M..............sLV...........
...................t................n.............
....r...........X...........M........v............
...x....t......I......a.PM...............W........
...........1.Bj....I........vO.h.dL...............
.........6....Rr......B...X........h..5v.L..z.....
......1G...........x.....3B.......5...............
.................B....0..........4..E.............
.....................X.....5..h....P....f.....D...
.......1........J.....eK..........................
..................I....R....K...........k.........
......G..................O........................
...........H...9...............K8.P.4..k..E.......
............1....3.............8.F.............f..
.........................4........................
.l...........X............9.......................
....N.................R...t.e.....................
...g............3..R.........e....h.........f.....
...........................e......i...............
................2...I.7..9..O.....s.........k.....
....................6...9E.............F..O.......
........................KN........................
.......g......................Z.........F..f...Y..
...........................A....i.................
...........6g...b........8.......y.....S..........
..l.....6.....m...............8...................
....u..m...b...............p...A..................
..............b.p........................k........
....m......2...........Z..y....i..................
........g2.....b.........i....D..ZF...............
......2.0...........p............N..........A.....
...m.............S...y........A...Z...N...........
..S..l..........................................Y.
........S....0u.................y......DY.........
...........0.........................D............
.................u...................p...Y........
.......u..........................................'''

rawMiniMap = '''..........
..x....x..
.o........
..........
...x.o....
......o...
.o.x.x....
.....x....
......o...
..........'''

def matrixFromString(string):
    stringList = string.split("\n")
    matrix = []
    for string in stringList:
        rowList = list(string)
        matrix.append(rowList)
    return matrix

def calcDistance (point1, point2):  # returns the absolute (pos/neg not considered) value of difference between two points
    xDif = abs(point1[0] - point2[0])
    yDif = abs(point1[1] - point2[1])
    return [xDif, yDif]

def getBounds(matrix):
    width = len(matrix[0])
    height = len(matrix)
    return [width, height]

def makeTowerList(matrix):  # scrapes through a matrix, finding towers and adding them to a hash if they dont exist yet, counting them otherwise
    towerDict = {}
    for row in matrix:
        for square in row:
            if square != ".":
                if square not in towerDict.keys():
                    towerDict[square] = 1
                else:
                    towerDict[square] += 1
    return towerDict

def getAllTowerCoordsOf(towerSymbol, matrix):
    towerCoordsList = []
    for y, row in enumerate(matrix):
        for x, square in enumerate(row):
            if square == towerSymbol:
                newTower = [x, y]
                towerCoordsList.append(newTower)
    return towerCoordsList

def validateCoords(coordPair, matrix):
    bounds = getBounds(matrix)
    if coordPair[0] >= 0 and coordPair[0] <= bounds[0] - 1:
        if coordPair[1] >= 0 and coordPair[1] <= bounds[1] - 1:
            return True
        else:
            return False
    else:
        return False

def findNodes(tower1, tower2, matrix):
    gap = calcDistance(tower1, tower2)
    nodes = []
    x1 = tower1[0]
    x2 = tower2[0]
    y1 = tower1[1]
    y2 = tower2[1]
    if tower1[0] > tower2[0]:
        x1 = tower1[0] + gap[0]
        x2 = tower2[0] - gap[0]
    elif tower1[0] < tower2[0]:
        x1 = tower1[0] - gap[0]
        x2 = tower2[0] + gap[0]
    if tower1[1] > tower2[1]:
        y1 = tower1[1] + gap[1]
        y2 = tower2[1] - gap[1]
    elif tower1[1] < tower2[1]:
        y1 = tower1[1] - gap[1]
        y2 = tower2[1] + gap[1]
    if validateCoords([x1, y1], matrix):
        nodes.append([x1, y1])
    if validateCoords([x2, y2], matrix):
        nodes.append([x2, y2])
    return nodes

def findOrientation(point1, point2):
    if point1[0] > point2[0]:
        if point1[1] > point2[1]:
            return "declineback"
        elif point1[1] < point2[1]:
            return "inclineback"
        else:
            return "horizontalback"
    elif point1[0] < point2[0]:
        if point1[1] > point2[1]:
            return "inclineforward"
        elif point1[1] < point2[1]:
            return "declineforward"
        else:
            return "horizontalforward"
    else:
        if point1[1] > point2[1]:
            return "verticalup"
        elif point1[1] < point2[1]:
            return "verticaldown"



def superFindNodes(tower1, tower2, matrix):
    gap = calcDistance(tower1, tower2)
    nodes = []
    orientation = findOrientation(tower1, tower2)
    print("Orientation is " + orientation)
    if orientation == "inclineforward":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
            currentPos[1] += gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
            currentPos[1] -= gap[1]
    elif orientation == "horizontalforward":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
    elif orientation == "declineforward":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
            currentPos[1] -= gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
            currentPos[1] += gap[1]
    elif orientation == "verticaldown":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[1] -= gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[1] += gap[1]
    elif orientation == "inclineback":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
            currentPos[1] -= gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
            currentPos[1] += gap[1]
    elif orientation == "horizontalback":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
    elif orientation == "declineback":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] += gap[0]
            currentPos[1] += gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[0] -= gap[0]
            currentPos[1] -= gap[1]
    elif orientation == "verticalup":
        currentPos = tower1
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[1] += gap[1]
        currentPos = tower2
        while validateCoords(currentPos, matrix):
            nodes.append(currentPos[:])
            currentPos[1] -= gap[1]
    return nodes

bigMap = matrixFromString(rawMap)
littleMap = matrixFromString(rawMiniMap)

def main(matrix):
    masterTowerList = makeTowerList(matrix)
    uniqueNodes = []
    for towerType in masterTowerList.keys():
        print("Checking towerType " + towerType)
        towerCoords = getAllTowerCoordsOf(towerType, matrix)
        print("Locations of this towerType are: " + str(towerCoords))
        for i, coord1 in enumerate(towerCoords):
            for coord2 in towerCoords[i + 1:]:
                print("Finding nodes between locations " + str(coord1) + " and " + str(coord2))
                nodes = superFindNodes(coord1[:], coord2[:], matrix)
                print("Found these nodes: " + str(nodes))
                for node in nodes:
                    if node not in uniqueNodes:
                        print("Node " + str(node) + " is unique.")
                        uniqueNodes.append(node)
                    else:
                        print("Node " + str(node) + " is not unique.")
    return uniqueNodes

stuff = main(bigMap)
print(stuff)
print(len(stuff))

# unique = main(bigMap)
# print(len(unique))


rawMap = '''12109832101432101234107652158943210178765892
03078456210145696701218943067654396549456701
54562364345436789874327832107810387630345210
65401875696925210765498017656901234521254321
78078956787814321544567328943217890012189450
69101045698701055432123410812206921983098765
43232132509652566785010569701105435674549056
58943001419143478994321678983210304105678143
67653214328012988765690787894321213289437212
45654301037001089650787096765010034576524301
56789890156121072341256101896654123678915498
43276765243234561212345234987783210569206789
54109854312789870109012345676898765454106543
45610123203650105438721056765609674323287012
54781010154543216521635489832014589210398013
67898543269854107610544376541023008101296323
54987656576765678923455210458782112010387456
23122189983454989012966904349698103465456567
12033078012763210101877813234521098578956798
03944565430887654012109320121034787632347897
87856556021991047121238458945695698961036016
96587432110872338930347567232780087654105125
01498983321265427945656089101091109803234934
32327465456766016859890176232892256712107843
21012334569854105766763245001743343893256765
30503129678945234897854632122654872894349854
45614068798234012656906543213458961783210703
21765878907178723765417891008965450654125612
30854965416069654894328982567872342103054503
48903010325450560761237813450561003276543678
56012321210341981230106504341540214789432189
67329630121212870341012415432634345695321012
78478742198903965494543326998723456786540765
89569653087654654987696547889010567847830874
21052104676501723898587032378765676956921923
32343015685432810767698121459034982349650010
10478723794354903456567030760121061078744567
21569654891263212347450177898267877101233498
32108765430678903038321789783454978715012399
47899834320545676129012876012543269856101087
56938723011230983543903965987650156747801256
40127619654321012652874854107890349832954343
30034508763018723761765543236501212721096501
21065619012349654890101234565432301430787432'''

rawMiniMap = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

rawTest1 = '''0123
4567
8901
2345'''

rawTest2 = '''0123456789
1234567890
2345678901
3456789012
4567890123
5678901234
6789012345
7890123456
8901234567
9012345678'''

rawTest3 = '''9999999999999999999
9888888888888888889
9877777777777777789
9876666666666666789
9876555555555556789
9876544444444456789
9876543333333456789
9876543222223456789
9876543211123456789
9876543210123456789
9876543211123456789
9876543222223456789
9876543333333456789
9876544444444456789
9876555555555556789
9876666666666666789
9877777777777777789
9888888888888888889
9999999999999999999'''

rawTest4 = '''22222
21112
21012
21112
22222'''

def matrixFromString(string):
    stringList = string.split("\n")
    matrix = []
    for string in stringList:
        rowList = list(string)
        for i, num in enumerate(rowList):
            rowList[i] = int(num)
        matrix.append(rowList)
    return matrix

def getBounds(matrix):
    width = len(matrix[0])
    height = len(matrix)
    return [width, height]

def validateCoords(coordPair, matrix):
    bounds = getBounds(matrix)
    if coordPair[0] >= 0 and coordPair[0] <= bounds[0] - 1:
        if coordPair[1] >= 0 and coordPair[1] <= bounds[1] - 1:
            return True
        else:
            return False
    else:
        return False

# def pathFind(startCoord, map):
#     visitedCoords = [startCoord]
#     currentHeight = map[startCoord[1]][startCoord[0]]
#     surroundings = {"up": (startCoord[0], startCoord[1] - 1),
#     "down": (startCoord[0], startCoord[1] + 1),
#     "left": (startCoord[0] - 1, startCoord[1]),
#     "right": (startCoord[0] + 1, startCoord[1])}
#     for direction in surroundings.keys():
#         thisCoord = surroundings[direction]
#         if validateCoords(thisCoord) and thisCoord not in workingArray and map[thisCoord[1]][thisCoord[0]] == currentHeight + 1:

def getSurroundings(startCoord, map):  # This function takes a coord, and returns the surrounding coordinates that are within bounds of that map. TESTED AND WORKING
    surroundings = {}
    if validateCoords((startCoord[0], startCoord[1] - 1), map):
        surroundings["up"] = (startCoord[0], startCoord[1] - 1)
    if validateCoords((startCoord[0], startCoord[1] + 1), map):
        surroundings["down"] = (startCoord[0], startCoord[1] + 1)
    if validateCoords((startCoord[0] - 1, startCoord[1]), map):
        surroundings["left"] = (startCoord[0] - 1, startCoord[1])
    if validateCoords((startCoord[0] + 1, startCoord[1]), map):
        surroundings["right"] = (startCoord[0] + 1, startCoord[1])
    return surroundings

# def canProceed(current, next, map): # takes currend coordinate and possible next coordinate, returns True if the next one is exactly 1 height up.
#     if map[next[1]][next[0]] == map[current[1]][current[0]] + 1:
#         return True
#     else:
#         return False

def findSummits(max, map):
    summits = {}
    for y, row in enumerate(map):
        for x, num in enumerate(row):
            if map[y][x] == max:
                summits[(x, y)] = ""
    return summits

def extendPaths(startNum, map):
    global memos
    for y, row in enumerate(map):
        for x, num in enumerate(row):
            # print("Looking into map[" + str(y) + "][" + str(x) + "], found a " + str(map[y][x]))
            # print("Does " + str(map[y][x]) + " = " + str(startNum) + "?")
            if map[y][x] == startNum:
                # print("It does. Now generating udlr...")
                udlr = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                # print(udlr)
                for spot in udlr:
                    # print("Using coord from udlr, " + str(spot))
                    # print("Checking if the coord is on the map and if already listed as a key in memos...")
                    if not validateCoords(spot, map):  #coord is off the map so skip it.
                        # print("This coord is not on the map.")
                        continue
                    elif spot in memos.keys() and map[spot[1]][spot[0]] == startNum + 1:  #found a previous path
                        if (x, y) not in memos.keys():
                            memos[(x, y)] = []
                        if memos[spot] == "":
                            memos[(x, y)].append([spot])
                        else:
                            for path in memos[spot]:
                                newPath = path[:]
                                newPath.insert(0, spot)
                                memos[(x, y)].append(newPath)

def buildAllPaths(maxHeight, map):
    global memos
    memos = findSummits(maxHeight, map)
    for i in range(maxHeight - 1, -1, -1):
        # print("i = " + str(i))
        # print(memos)
        extendPaths(i, map)

def returnUniques(max):
    global memos
    results = []
    uniques = {}
    uniqueCount = {}
    for key in memos.keys():
        for path in memos[key]:
            if len(path) == max:
                completePath = [key] + path[:]
                results.append(completePath)
    for i, fullPath in enumerate(results):
        if fullPath[0] not in uniques.keys():
            uniques[fullPath[0]] = [fullPath[-1]]
            uniqueCount[fullPath[0]] = 1
        # elif fullPath[-1] in uniques[fullPath[0]]:
        #     continue
        elif fullPath[-1] not in uniques[fullPath[0]]:
            uniques[fullPath[0]].append(fullPath[-1])
            uniqueCount[fullPath[0]] += 1
    # print("Results")
    # print(results)
    # print("Unique Hash")
    # print(uniques)
    # print("Counts")
    # print(uniqueCount)
    return uniques




bigMap = matrixFromString(rawMap)
miniMap = matrixFromString(rawMiniMap)
test1 = matrixFromString(rawTest1)
test2 = matrixFromString(rawTest2)
test3 = matrixFromString(rawTest3)
test4 = matrixFromString(rawTest4)
memos = None
buildAllPaths(9, bigMap)
# print(memos)
totals = returnUniques(9)
grandTotal = 0
for uniqs in totals.values():
    grandTotal += len(uniqs)

print(grandTotal)

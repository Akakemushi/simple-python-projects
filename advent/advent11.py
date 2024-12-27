import itertools

rawData = '8069 87014 98 809367 525 0 9494914 5'
rawMini = '125 17'
rawTiny = '67'

def arrayFromRaw(data):
    a = data.split(" ")
    array = []
    for num in a:
        array.append((num, ""))
    return array

def annotate(tupleArray):    # takes an array of tuples, and marks each number with either A B or C, then returns that annotated array of tuples.
    for i, tuple in enumerate(tupleArray):
        if tuple[0] == "0":
            tupleArray[i] = ("0", "A")
        elif len(tuple[0]) % 2 == 0:
            tupleArray[i] = (tuple[0], "B")
        else:
            tupleArray[i] = (tuple[0], "C")
    return tupleArray

def processA(tupleArray):
    for i, tuple in enumerate(tupleArray):
        if tuple[1] == "A":
            tupleArray[i] = ("1", "")
    return tupleArray

def processB(tupleArray):
    for i, tuple in enumerate(tupleArray):
        if tuple[1] == "B":
            halfLen = int(len(tuple[0]) / 2)
            fhalf = int(tuple[0][:halfLen])
            fhalf = str(fhalf)
            bhalf = int(tuple[0][halfLen:])
            bhalf = str(bhalf)
            tupleArray[i] = (fhalf, "")
            tupleArray.insert(i + 1, (bhalf, ""))
    return tupleArray

def processC(tupleArray):
    for i, tuple in enumerate(tupleArray):
        if tuple[1] == "C":
            num = int(tuple[0]) * 2024
            tupleArray[i] = (str(num), "")
    return tupleArray

def blink(tupleArray, times):
    for i in range(times):
        annotate(tupleArray)
        tupleArray = processA(tupleArray)
        tupleArray = processB(tupleArray)
        tupleArray = processC(tupleArray)
    return tupleArray

def get_chunks(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]

def blinkOnce(dict):
    newDict = {}
    for num, count in dict.items():
        if num == "0":
            if "1" in newDict.keys():
                newDict["1"] += count
            else:
                newDict["1"] = count
            continue
        elif len(num) % 2 == 0:
            half = int(len(num) / 2)
            fhalf = int(num[:half])
            fhalf = str(fhalf)
            bhalf = int(num[half:])
            bhalf = str(bhalf)
            if fhalf in newDict.keys():
                newDict[fhalf] += count
            else:
                newDict[fhalf] = count
            if bhalf in newDict.keys():
                newDict[bhalf] += count
            else:
                newDict[bhalf] = count
            continue
        else:
            bigNum = int(num) * 2024
            if str(bigNum) in newDict.keys():
                newDict[str(bigNum)] += count
            else:
                newDict[str(bigNum)] = count
            continue
    return newDict

def multiBlink(stones, times):
    for _ in range(times):
        stones = blinkOnce(stones)
    return stones





tiny = arrayFromRaw(rawTiny)
mini = arrayFromRaw(rawMini)
big = arrayFromRaw(rawData)

stones = {}    #this code initializes the counting dictionary.
for tuple in big:
    if tuple[0] not in stones.keys():
        stones[tuple[0]] = 1
    else: stones[tuple[0]] += 1

finalStones = multiBlink(stones, 75)
print(sum(finalStones.values()))

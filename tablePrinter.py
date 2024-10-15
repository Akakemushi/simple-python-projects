tableData = [['cat', 'dog', 'chimpanzee', 'armadillo'],
             ['Jack', 'Jill', 'Jason', 'Jenny'],
             ['Africa', 'Antarctica', 'North America', 'Asia'],
             ['trombone', 'tuba', 'digeridoo', 'piano'],
             ['cake', 'ice cream', 'cookies', 'candy']]

def printTable(data):
    colCount = len(data[0])
    longestList = []
    for i in range(colCount):
        longest = 0
        for list in data:
            if len(list[i]) > longest:
                longest = len(list[i])
        longestList.append(longest)
    for list in data:
        for i in range(colCount):
            print(list[i].ljust(longestList[i]), end="    ")
        print("")

printTable(tableData)

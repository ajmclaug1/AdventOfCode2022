with open("input_example.txt") as f:
    fh = f.read().splitlines()


def forestfortheTrees(file):
    forest = []
    forest_height = 0
    for each in file:
        forest_height += 1 
        forest_list = [int(x) for x in str(each)]
        forest.append(forest_list)
    forest_lenght = len(str(file[0]))
    return forest, forest_height, forest_lenght

forestlists, forestH, forestL = forestfortheTrees(fh)

def visabilityCalc(flists, height , lenght):
    visable = (lenght + lenght) + ((height  + height ) - 4)
    i = 1
    while i < height :
        for postion in range(1, lenght - 1):
            visableTree = False
            tree = flists[i][postion]
            print(tree, postion)
            treeline = flists[i].copy()
            treeline.pop(postion)
            print(treeline)
            for each in treeline:
                if each < tree:
                    visableTree = True
            #Fix in morning
            forestHeigthList = list(range(0,lenght -1))
            forestHeigthList.remove(postion)
            print(forestHeigthList)
            for each in forestHeigthList:
                if each < tree:
                    visableTree = True
            if visableTree:
                visable += 1
  
        i += 1






    return visable


answer = visabilityCalc(forestlists, forestH, forestL)

print(answer)
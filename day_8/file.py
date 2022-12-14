with open("input.txt") as f:
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


def visabilityCalc(flists, height, lenght):
    visable = (lenght + lenght) + ((height + height) - 4)
    i = 1
    while i < height - 1:
        for postion in range(1, lenght - 1):
            visableTree = 0
            tree = flists[i][postion]
            # Left visable
            res = True in (ele >= tree for ele in flists[i][0:postion])
            if not res:
                visableTree += 1
            # Right visable
            res = True in (
                ele >= tree for ele in flists[i][postion + 1:len(flists[i])])
            if not res:
                visableTree += 1

            forestHeigthList = list(range(0, lenght))
            
            # Up visable
            up = [flists[each][postion] for each in forestHeigthList[0:i]]
            res = True in (ele >= tree for ele in up)
            if not res:
                visableTree += 1
            # Down visable
            down = [flists[each][postion]
                    for each in forestHeigthList[i + 1:len(forestHeigthList)]]
            res = True in (ele >= tree for ele in down)
            if not res:
                visableTree += 1

            if visableTree > 0:
                visable += 1

        i += 1

    return visable


answer = visabilityCalc(forestlists, forestH, forestL)

print("The Answer is %s " % answer)

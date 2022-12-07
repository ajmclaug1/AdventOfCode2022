with open("input.txt") as f:
        fh = f.read()



def findUniqueSeq(characters):
    code_lenght = 0    
    i = 0
    while code_lenght < characters:
        code_lenght = len(set(fh[i:i+characters]))
        if code_lenght == characters:
            print("number of characters processed is %s" % (i+characters))
            print(fh[i:i+characters])
        i += 1

findUniqueSeq(4)
findUniqueSeq(14)

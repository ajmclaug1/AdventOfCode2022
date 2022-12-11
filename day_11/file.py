from math import trunc


with open("input.txt") as f:
    fh = f.read().splitlines()

fh = list(filter(None, fh))


def monke(file, noMonke, noLines):
    monkeDict = {}
    i = 0
    start = 0
    end = noLines
    while i < noMonke + 1:
        currentMonke =file[start:end]
        monkeDict[i] = {"items" : currentMonke[1].strip(" Starting items: ").split(", ")}
        monkeDict[i].update({"worry" : currentMonke[2].strip("Operation: new = old ")})
        monkeDict[i].update({"test" : currentMonke[3].strip("Test: divisible by ")})
        monkeDict[i].update({"true" : currentMonke[4].strip("  If true: throw to monkey ")})
        monkeDict[i].update({"false" : currentMonke[5].strip("If false: throw to monkey ")})
        monkeDict[i].update({"inspection": 0})
        i += 1
        start += noLines
        end += noLines
    
    return monkeDict


monkObj = monke(fh, 7,6)

def fAround(monkeData, rounds):
    for each in range(0,rounds):
        print("round %s" % (each))
        for k, v in monkeData.items():
            print(k, v["items"])
            for stuff in v["items"]:
                print(stuff)
                monkeData[k]["inspection"] += 1
                monkeData[k]["items"].remove(stuff)
                if v["worry"] == "*":
                    worryLvl = int(stuff) * int(stuff)
                else:
                    v["worry"]
                    worryLvl =  eval(str(stuff) + v["worry"])
                worryLvl = trunc(worryLvl / 3)
                if worryLvl % int(v["test"]) == 0:
                    monkeData[int(v["true"])]["items"].append(worryLvl)
                else:
                    monkeData[int(v["false"])]["items"].append(worryLvl)   
    return monkeData
    


answer = fAround(monkObj, 20)

for k, v in answer.items():
    print(v["inspection"])




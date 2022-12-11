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
    i = 0
    while i < rounds:
        i += 1
        dictI = 0
        while dictI < len(monkeData):
            listI = 0
            while listI < len(monkeData[dictI]["items"]):
                monkeData[dictI]["inspection"] += 1
                if monkeData[dictI]["worry"] == '*':
                    worryLvl = int(monkeData[dictI]["items"][listI]) * int(monkeData[dictI]["items"][listI])
                else:
                    worryLvl =  eval(str(monkeData[dictI]["items"][listI]) + monkeData[dictI]["worry"])
                worryLvl = trunc(worryLvl / 3)
                if worryLvl % int(monkeData[dictI]["test"]) == 0:
                    monkeData[int(monkeData[dictI]["true"])]["items"].append(worryLvl)
                else:
                    monkeData[int(monkeData[dictI]["false"])]["items"].append(worryLvl)
                listI += 1
       
            monkeData[dictI]["items"] = []
            dictI += 1

    return monkeData
    


answer = fAround(monkObj, 20)

highanswer = []
for k, v in answer.items():
    highanswer.append(int(v["inspection"]))

highanswer.sort(reverse = True)
print(highanswer[0] * highanswer[1])

with open("input.txt") as f:
    fh = f.read().splitlines()

cycle = 0

sumofcycles = 0

x = 1

cyclesdict ={}

for each in fh:
    value = each.split(" ")
    cycle += 1
    cyclesdict[cycle] = x
    if value[0] == "addx":
        cycle += 1
        cyclesdict[cycle] = x
    if len(value) == 2:
        x += int(value[1])

for k,v in cyclesdict.items():
    if k in [20,60,100,140,180,220]:
        sumofcycles += (k *v)

print(sumofcycles)
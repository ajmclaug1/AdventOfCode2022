with open("input.txt") as f:
    fh = f.read().splitlines()

cycle = 0

cycles_to_sum = [20,60,100,140,180,220]

sumofsignalstrenghts = 0

running_total = 0

for each in fh:
    cycle +=1
    value = each.split(" ")
    if value[0] == "addx":
        cycle +=1
    if len(value) == 2:
        running_total += int(value[1])
    if cycle in cycles_to_sum:
        print(value)
        sumofsignalstrenghts += running_total

print(sumofsignalstrenghts)
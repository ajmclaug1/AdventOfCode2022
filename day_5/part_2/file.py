
with open("stack.txt") as f:
    fhstack = f.read().splitlines()

#create dict of stacks
mapping = [1]

i = 1
for each in range(0,8):
    i += 4
    mapping.append(i)

stacks = {}

for each in range(1,10):
    stacks[each] = []


for each in fhstack:
    stack_no = 1
    if each[1] != '1':
        for value in mapping:
            if each[value] != " ":
                stacks[stack_no].append(each[value])
                stack_no += 1
            else:
                stack_no += 1
            
#Create nested lists of movements
with open("movement.txt") as f:
    fhmove = f.read().splitlines()

movements = []

for each in fhmove:
    movelist = each.strip("move ")
    movelist = movelist.replace(" from ", ",")
    movelist = movelist.replace(" to", ",")
    movelist = movelist.split(",")
    movelist = list(map(int, movelist))
    movements.append(movelist)

#Apply movements to stack
def movement(stack_config, movement_inst):
    for m in movements:
        itemsstuff = stack_config[m[1]][0:m[0]]
        itemsstuff.reverse()
        for crate in itemsstuff:
            stack_config[m[2]].insert(0,crate)
        del stack_config[m[1]][:m[0]]

    return stack_config

final_stack = movement(stacks, movements)
print("Final topstack")

for k, v in final_stack.items():
    print(k,v)

for k, v in final_stack.items():
    print(v[0], end="")



        

    



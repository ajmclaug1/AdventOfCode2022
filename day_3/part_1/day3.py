letter_value = dict()

for each in range(1,27):
    letter_value[chr(ord('`') + each)] = each
    letter_value[chr(ord('@') + each)] = each + 26 

print(letter_value)

with open('input.txt') as f:
    fh = f.read().splitlines()


running_total = 0

def identify_value(three_rucksacks):
    print(three_rucksacks)
    duplicates = list(set(three_rucksacks[0]).intersection(three_rucksacks[1],three_rucksacks[2]))
    print(three_rucksacks[0])
    print(three_rucksacks[1])
    print(three_rucksacks[2])
    
    print(duplicates)
    return duplicates[0]

no_of_rucksacks = 1
three_rucksacks = []
running_total = 0
for each in fh:
    three_rucksacks.append(each)
    if no_of_rucksacks == 3:
        running_total += letter_value[identify_value(three_rucksacks)]
        no_of_rucksacks = 1
        three_rucksacks = []
    else:
        no_of_rucksacks += 1
        


print(running_total)
letter_value = dict()

for each in range(1,27):
    letter_value[chr(ord('`') + each)] = each
    letter_value[chr(ord('@') + each)] = each + 26 

print(letter_value)

with open('input.txt') as f:
    fh = f.read().splitlines()


running_total = 0

def identify_value(rucksack):
    lenght = len(rucksack)
    half = int(lenght / 2)
    first_container = rucksack[0:half]
    second_container = rucksack[half:lenght]
    duplicates = list(set(first_container).intersection(second_container))
    print(first_container)
    print(second_container)
    
    
    return duplicates[0]

for each in fh:
    running_total += letter_value[identify_value(each)]

print(running_total)
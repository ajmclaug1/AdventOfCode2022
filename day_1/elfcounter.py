fh = open("input.txt")

elfdict = {}

elf_no = 1

calories = 0

for each in fh:
    if each == "\n":
        elfdict["elf %s" %(elf_no)] = calories
        elf_no += 1
        calories = 0
    else:
        calories += int(each)

high_calories = 0

calories_list = []
for k, v in elfdict.items():
    if v > high_calories:
        high_calories = v
        name = k
        is_carrying = v
    calories_list.append(v)

print("%s is carrying %s calories" % (name, is_carrying))

calories_list.sort(reverse=True)

print("sum of three highest calories is %s" % (sum(calories_list[0:3])))
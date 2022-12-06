result_calculator = {"A X": 3, "A Y": 4,"A Z": 8,
                    "B X": 1, "B Y": 5,"B Z": 9,
                    "C X": 2, "C Y": 6,"C Z": 7 }

fh = open("./input.txt")

running_score = 0

for each in fh:
    running_score += result_calculator[each.rstrip()]

print(running_score)
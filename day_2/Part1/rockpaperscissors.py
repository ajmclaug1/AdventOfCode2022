result_calculator = {"A X": 4, "A Y": 8,"A Z": 3,
                    "B X": 1, "B Y": 5,"B Z": 9,
                    "C X": 7, "C Y": 2,"C Z": 6 }

fh = open("./input.txt")

running_score = 0

for each in fh:
    running_score += result_calculator[each.rstrip()]

print(running_score)
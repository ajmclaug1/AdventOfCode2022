with open("input.txt") as f:
    fh = f.read().splitlines()

setscontained = 0


for each in fh:
    ranges = each.split(',')
    r1 =ranges[0].split('-')
    r2 =ranges[1].split('-')
    if ((int(r1[0]) >= int(r2[0])) and (int(r1[1]) <= int(r2[1])) ) or ((int(r2[0]) >= int(r1[0])) and (int(r2[1]) <= int(r1[1]))):
        setscontained += 1
        print("True")
    



print(setscontained)

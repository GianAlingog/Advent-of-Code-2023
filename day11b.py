sum = 0
lines = []
galaxies = []
blank_columns = []
blank_rows = []

with open("day11.txt") as my_input:
    for line in my_input:
        lines.append(line)
    
    for i in range(len(lines)):
        blank_row = True
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                blank_row = False
        if blank_row:
            blank_rows.append(i)
    
    for j in range(len(lines)):
        blank_column = True
        for i in range(len(lines[i])):
            if lines[i][j] == "#":
                blank_column = False
        if blank_column:
            blank_columns.append(j)

blank_columns.reverse()
blank_rows.reverse()

for col, line in enumerate(lines):
    for row, char in enumerate(line):
        if char == "#":
            galaxies.append((col, row))

for blank in blank_columns:
    for galaxy in range(len(galaxies)):
        if galaxies[galaxy][1] > blank:
            galaxies[galaxy] = (galaxies[galaxy][0], galaxies[galaxy][1] + 1000000 - 1)

for blank in blank_rows:
    for galaxy in range(len(galaxies)):
        if galaxies[galaxy][0] > blank:
            galaxies[galaxy] = (galaxies[galaxy][0] + 1000000 - 1, galaxies[galaxy][1])

print(galaxies)

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(sum)        


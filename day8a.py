maps = {}

with open("day8.txt") as my_input:
    instructions, _, *init = my_input
    for i in init: 
        maps[i[:3]] = [i[7:10], i[12:15]]

    current = 'AAA'
    count = 0
    while current != 'ZZZ':
        for char in instructions:
            if current == 'ZZZ':
                break

            if char == 'L':
                current = maps[current][0]
                count += 1
            elif char == 'R':
                current = maps[current][1]
                count += 1
print(count)

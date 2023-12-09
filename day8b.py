import time
import math

start = time.time()

maps = {}
currents = []
ends = []

with open("day8.txt") as my_input:
    instructions, _, *init = my_input
    for i in init: 
        maps[i[:3]] = [i[7:10], i[12:15]]
        if i[2] == 'A':
            currents.append(i[:3])
        if i[2] == 'Z':
            ends.append(i[:3])

    counts = [0] * len(currents)

    for i in range(len(currents)):
        while currents[i] not in ends:
            for char in instructions:
                if char == 'L':
                    currents[i] = maps[currents[i]][0]
                    counts[i] += 1
                elif char == 'R':
                    currents[i] = maps[currents[i]][1]
                    counts[i] += 1

print(math.lcm(*counts))

end = time.time()
print(end - start)

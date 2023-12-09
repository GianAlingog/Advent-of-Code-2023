ans = 1

with open("day6.txt") as my_input:
    times, distances = my_input
    times = times.split(":")[1].split()
    distances = distances.split(":")[1].split()
    # print(times, distances)

    for i in range(len(times)):
        min = 0
        for j in range(1, int(times[i])):
            if (j * (int(times[i]) - j) > int(distances[i])):
                min = j
                break
        
        diff = int(times[i]) - 2 * min + 1
        ans *= diff
        
print(ans)
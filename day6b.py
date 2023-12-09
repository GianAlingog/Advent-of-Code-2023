with open("day6.txt") as my_input:
    times, distances = my_input
    times = times.split(":")[1].replace(" ", "")
    distances = distances.split(":")[1].replace(" ", "")

    min = 0
    for j in range(1, int(times)):
        if (j * (int(times) - j) > int(distances)):
            min = j
            break
        
    diff = int(times) - 2 * min + 1

        
print(diff)
sum = 0

with open("day2.txt") as my_input:
    for line in my_input:
        # colors = ['red', 'blue', 'green']
        game_id, games = line.split(":")
        game_id = game_id[4:]
        
        games = games.split(";")

        minimums = [0, 0, 0]

        for game in games:
            cubes = game.split(",")
            for cube in cubes:
                if cube.find('red') != -1:
                    if int(cube[1:-1-3]) > minimums[0]:
                        minimums[0] = int(cube[1:-1-3])
                elif cube.find('blue') != -1:
                    if int(cube[1:-1-4]) > minimums[1]:
                        minimums[1] = int(cube[1:-1-4])
                elif cube.find('green') != -1:
                    if int(cube[1:-1-5]) > minimums[2]:
                        minimums[2] = int(cube[1:-1-5])
        
        power = 1
        for minimum in minimums:
            power *= minimum
        
        sum += power

print(sum)
sum = 0

with open("day2.txt") as my_input:
    for line in my_input:
        # colors = ['red', 'blue', 'green']
        game_id, games = line.split(":")
        game_id = game_id[4:]
        
        games = games.split(";")

        
        possible = True

        for game in games:
            cubes = game.split(",")
            for cube in cubes:
                if cube.find('red') != -1:
                    if int(cube[1:-1-3]) > 12:
                        possible = False
                        break
                elif cube.find('blue') != -1:
                    if int(cube[1:-1-4]) > 14:
                        possible = False
                        break
                elif cube.find('green') != -1:
                    if int(cube[1:-1-5]) > 13:
                        possible = False
                        break
            
            if not possible:
                break
            
        if possible:
            sum += int(game_id)

print(sum)
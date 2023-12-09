sum = 0

with open("day4.txt") as my_input:
    for line in my_input:
        card_id, card = line.split(":")
        card_id = int(card_id[4:])
        
        wins, ours = card.split("|")
        wins = wins.split()
        ours = ours.split()

        count = 0

        for win in wins:
            if win in ours:
                count += 1
        
        if count > 0:
            sum += pow(2, count-1)
            # print(pow(2, count-1))

print(sum)

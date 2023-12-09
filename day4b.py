sum = 0
amts = []

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
        
        amts.append(count)

times = [1] * len(amts)

for i in range(len(amts)):
    for j in range(amts[i]):
        if (i+j < len(amts)):
            times[i+j+1] += 1

for k in times:
    sum += k
print(sum * 2)

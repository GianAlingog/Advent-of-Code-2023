import collections
import time

start = time.time()

sum = 0
current = 0
ranks = "AKQT98765432J"

ordered = [[], [], [], [], [], [], []]

with open("day7.txt") as my_input:
    for line in my_input:
        current += 1
        deck, bet = line.split()
        dupes = collections.defaultdict(int)

        for char in deck:
            dupes[char] += 1
        
        sorted_dupes = sorted(dupes, key=dupes.get, reverse=True)
        for dupe in sorted_dupes:
            if dupe == 'J' and dupes['J'] != 5:
                sorted_dupes.remove('J')
                dupes[sorted_dupes[0]] += dupes['J']

        print(dupes)

        for char in sorted_dupes:
            match dupes[char]:
                case 5:
                    ordered[0].append((deck, int(bet)))
                    break
                case 4:
                    ordered[1].append((deck, int(bet)))
                    break
                case 3:
                    if dupes[sorted_dupes[sorted_dupes.index(char)+1]] == 2:
                        ordered[2].append((deck, int(bet)))
                        break
                    else:
                        ordered[3].append((deck, int(bet)))
                        break
                case 2:
                    if dupes[sorted_dupes[sorted_dupes.index(char)+1]] == 2:
                        ordered[4].append((deck, int(bet)))
                        break
                    else:
                        ordered[5].append((deck, int(bet)))
                        break
                case 1:
                    ordered[6].append((deck, int(bet)))
                    break
for i in range(len(ordered)):
    ordered[i] = sorted(ordered[i], key=lambda deck: [ranks.index(c) for c in deck[0]])

for lists in ordered:
    for i in lists:
        sum += current * i[1]
        current -= 1

print(sum)

end = time.time()
print(end-start)
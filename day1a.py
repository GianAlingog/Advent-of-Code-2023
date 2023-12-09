sum = 0

with open("day1.txt") as my_input:
    for line in my_input:
        first_num = 0
        last_num = 0
        first_filled = False
        for char in line:
            if char.isnumeric():
                if not first_filled:
                    first_num = int(char) * 10
                    last_num = int(char)
                    first_filled = True
                else:
                    last_num = int(char)
        sum += first_num + last_num

print(sum)
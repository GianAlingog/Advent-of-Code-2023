sum = 0

with open("day1.txt") as my_input:
    for line in my_input:
        reversed_line = line[::-1]
        # print(line, reversed_line)
        search = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ]
        backwards = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'zero', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin'
        ]

        first = 0
        last = 0
        first_index = 2147483645 # false integer limit (-2)
        last_index = 2147483645 # less than 0 (first index)

        for i in search:
            if line.find(i) != -1:
                if line.find(i) < first_index:
                    first_index = line.find(i)
                    first = i
        if search.index(first) >= 10:
            first = search[search.index(first) - 10]
        
        for j in backwards:
            if reversed_line.find(j) != -1:
                if reversed_line.find(j) < last_index:
                    last_index = reversed_line.find(j)
                    last = j
        if backwards.index(last) >= 10:
            last = backwards[backwards.index(last) - 10]
        
        # print(first_index, last_index, first, last)
        sum += 10 * int(first) + int(last)



print(sum)
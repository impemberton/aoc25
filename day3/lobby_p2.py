sum_of_joltage = 0
with open("input.txt") as input:
    for line in input:
        max_left = line[0]
        max_left_i = 0
        rest_of_line = line
        max_joltage = ""
        for numbers_left in range(12, 0, -1):
            for i in range(0, len(rest_of_line) - numbers_left):
                if int(rest_of_line[i]) > int(max_left):
                    max_left_i = i
                    max_left = rest_of_line[i]
            max_joltage += max_left
            rest_of_line = rest_of_line[max_left_i+1:]
            max_left_i = 0
            max_left = rest_of_line[0]
            print(max_left)
            
        print(line, max_joltage)
        sum_of_joltage += int(max_joltage)

print(sum_of_joltage)

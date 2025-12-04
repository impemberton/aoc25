sum_of_joltage = 0
with open("input.txt") as input:
    for line in input:
        rest_of_line = line
        max_joltage = 0
        for num1 in line[:-1]:
            rest_of_line = rest_of_line[1:]
            for num2 in rest_of_line:
                if int(num1+num2) > max_joltage:
                    max_joltage = int(num1+num2)
        print(max_joltage)
        sum_of_joltage += max_joltage

print(sum_of_joltage)

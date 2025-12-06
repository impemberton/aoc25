input = open("input.txt")
num_lines = []
operators = []
for line in input:
    if "+" in line or "*" in line:
        for c in line:
            if c not in " \n":
                operators.append(c)
    else:
        nums_in_line = []
        cn = ""
        for c in line:
            if c in " \n":
                if len(cn) > 0:
                    nums_in_line.append(int(cn))
                    cn = ""
            else:
                cn += c
        num_lines.append(nums_in_line)

grandtotal = 0
for col in range(len(operators)):
    if operators[col] == "*":
        product = 1
        for row in range(len(num_lines)):
            product *= num_lines[row][col]
        grandtotal += product
    if operators[col] == "+":
        sum = 0
        for row in range(len(num_lines)):
            sum += num_lines[row][col]
        grandtotal += sum

print(grandtotal)


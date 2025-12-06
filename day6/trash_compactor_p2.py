input = open("input.txt").read()
input = input.strip().split("\n")
num_lines = input[:-1]
operators = [char for char in input[-1] if char != " "]
print(num_lines)
print(operators)
num_blocks = [[]]
i = 0
for n in range(len(num_lines[0])):
    current_num = ""
    for l in range(len(num_lines)):
         current_num += num_lines[l][n]
    if len(current_num.strip()) > 0:
        num_blocks[i].append(int(current_num))
    else:
        num_blocks.append([])
        i += 1
print(num_blocks)

grand_total = 0
for i in range(len(operators)):
    if operators[i] == "*":
        product = 1
        for num in num_blocks[i]:
            product *= num
        grand_total += product
    if operators[i] == "+":
        grand_total += sum(num_blocks[i])

print(grand_total)


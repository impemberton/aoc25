with open("input.txt") as input:
    input = input.read()

ids = input.split(",")

sum_of_ids = 0
for id_range in ids:
    first_id, last_id = id_range.split("-")
    for id in range(int(first_id), int(last_id)+1):
        string_id = str(id)
        if string_id[:len(string_id)//2] == string_id[len(string_id)//2:]:
            sum_of_ids += id

print(sum_of_ids)


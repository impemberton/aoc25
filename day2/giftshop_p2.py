def split_string_into_chunks(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

with open("input.txt") as input:
    input = input.read()

ids = input.split(",")
sum_of_ids = 0
for id_range in ids:
    first_id, last_id = id_range.split("-")
    for id in range(int(first_id), int(last_id)+1):
        string_id = str(id)
        factors = [i for i in range(1, len(string_id)) if len(string_id) % i == 0]
        for factor in factors:
            chunked_id = split_string_into_chunks(string_id, factor)
            if all([chunk == chunked_id[0] for chunk in chunked_id]):
                sum_of_ids += id
                break

print(sum_of_ids)

